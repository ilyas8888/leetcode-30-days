#!/usr/bin/env python3
"""Check the vault and print progress. Standard library only.

Fails (exit 1) if any wikilink points to a missing note, a required
property is missing, or a tracked value is outside its allowed set.
Otherwise exits 0 and prints a short status.
"""
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Allowed values per note type (empty string always allowed for optional fields).
REQUIRED = {
    "problem": ["type", "number", "title", "url", "card", "day", "role",
                "status", "attempts", "tags"],
    "session": ["type", "day", "week", "kind", "focus", "status", "tags"],
    "card": ["type", "card", "name", "days", "tags"],
    "mock": ["type", "mock", "day", "status", "tags"],
}
ENUMS = {
    "problem": {"role": {"guided", "solo", "bonus"},
                "status": {"todo", "learning", "done"},
                "last_result": {"", "alone", "hints", "solution"}},
    "session": {"kind": {"learn", "review", "mixed", "final"},
                "status": {"planned", "done", "minimum"}},
    "mock": {"status": {"planned", "done"}},
}

FENCE = re.compile(r"```.*?```", re.DOTALL)
LINK = re.compile(r"\[\[([^\]]+)\]\]")


def parse_frontmatter(text):
    """Tiny YAML-ish parser: key: value lines and inline [a, b] lists."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].split("\n"):
        line = line.rstrip()
        if not line.strip() or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key, val = key.strip(), val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [x.strip().strip('"').strip("'") for x in inner.split(",")] if inner else []
        else:
            fm[key] = val.strip('"').strip("'")
    return fm


def link_target(raw):
    """Resolve a wikilink body to its target note name."""
    raw = raw.split("#", 1)[0]
    raw = raw.replace("\\|", "|").split("|", 1)[0]
    return raw.strip()


def main():
    # Skeletons and the archived setup prompt are not real notes.
    SKIP_DIRS = (".git", ".obsidian", "99 Templates")
    SKIP_FILES = ("setup-prompt.md", "claude-code-setup.md")
    md_files, targets = [], set()
    for dirpath, _dirs, files in os.walk(ROOT):
        if any(s in dirpath for s in SKIP_DIRS):
            continue
        for name in files:
            stem, ext = os.path.splitext(name)
            if ext in (".md", ".canvas"):
                targets.add(stem)
                targets.add(name)
            if ext == ".md" and name not in SKIP_FILES:
                md_files.append(os.path.join(dirpath, name))

    broken = []           # (relpath, missing target)
    problem_issues = []   # (note name, message)
    counts = {"problem": 0, "session": 0, "card": 0, "mock": 0}
    by_status, by_result = {}, {}
    sessions_done, planned_days, due = 0, [], []
    today = date.today().isoformat()

    for path in md_files:
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)

        # Broken-link check (ignore fenced code blocks).
        for raw in LINK.findall(FENCE.sub("", text)):
            tgt = link_target(raw)
            if tgt and tgt not in targets:
                broken.append((rel, tgt))

        ntype = fm.get("type", "")
        if ntype in counts:
            counts[ntype] += 1

        # Property validation for tracked note types.
        if ntype in REQUIRED:
            label = fm.get("title") or os.path.splitext(os.path.basename(path))[0]
            for key in REQUIRED[ntype]:
                if key not in fm:
                    problem_issues.append((label, "missing property '%s'" % key))
            for key, allowed in ENUMS.get(ntype, {}).items():
                val = fm.get(key, "")
                if val not in allowed:
                    problem_issues.append((label, "%s='%s' not in %s" % (key, val, sorted(allowed))))
            if ntype == "problem":
                fam = fm.get("familiarity", "")
                if fam not in ("", "1", "2", "3", "4", "5"):
                    problem_issues.append((label, "familiarity='%s' must be blank or 1-5" % fam))

        # Status tallies.
        if ntype == "session":
            if fm.get("status") == "done":
                sessions_done += 1
            elif fm.get("status") == "planned" and fm.get("day", "").isdigit():
                planned_days.append(int(fm["day"]))
        if ntype == "problem":
            by_status[fm.get("status", "")] = by_status.get(fm.get("status", ""), 0) + 1
            lr = fm.get("last_result", "") or "(none)"
            by_result[lr] = by_result.get(lr, 0) + 1
            nr = fm.get("next_review", "")
            if nr and nr <= today:
                due.append(label if (label := fm.get("title")) else rel)

    ok = not broken and not problem_issues

    print("=" * 56)
    print("VAULT CHECK")
    print("=" * 56)
    print("Notes: %d problems, %d sessions, %d cards, %d mocks"
          % (counts["problem"], counts["session"], counts["card"], counts["mock"]))

    if broken:
        print("\nBROKEN LINKS (%d):" % len(broken))
        for rel, tgt in broken:
            print("  %s -> [[%s]]" % (rel, tgt))
    if problem_issues:
        print("\nPROPERTY ISSUES (%d):" % len(problem_issues))
        for label, msg in problem_issues:
            print("  %s: %s" % (label, msg))

    print("\nPROGRESS")
    print("  Sessions done: %d of 30" % sessions_done)
    print("  Next planned day: %s" % ("Day %02d" % min(planned_days) if planned_days else "none"))
    print("  Problems by status: " + ", ".join("%s=%d" % (k or "(blank)", v)
                                               for k, v in sorted(by_status.items())))
    print("  Problems by last result: " + ", ".join("%s=%d" % (k, v)
                                                    for k, v in sorted(by_result.items())))
    print("  Re-solves due today or earlier: %s" % (", ".join(due) if due else "none"))

    print("\n%s" % ("OK — nothing broken." if ok else "FAILED — fix the items above."))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
