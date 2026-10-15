#!/usr/bin/env python3
"""Add a problem note after day 30.

Usage:
    python scripts/new_problem.py NUMBER "Title" CARD [--slug SLUG] [--day N] [--role bonus]

Creates 03 Problems/NNNN Title.md from the problem skeleton, builds the
LeetCode URL from the slug (derived from the title if not given), and adds
the problem to its card note's static Problems list.
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVALID = '<>:"/\\|?*'


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s


def card_note_name(card_num):
    matches = glob.glob(os.path.join(ROOT, "02 Cards", "Card %02d *.md" % card_num))
    if not matches:
        sys.exit("No card note found for card %d in 02 Cards/." % card_num)
    return os.path.splitext(os.path.basename(matches[0]))[0]


def build_note(num, title, url, card_link, day, role):
    daylink = "[[Day %02d]]" % day if day else "—"
    fm = [
        "---", "type: problem", "number: %d" % num, "title: %s" % title,
        "url: %s" % url, 'card: "%s"' % card_link,
        "day: %s" % (day if day else ""), "role: %s" % role,
        "status: todo", "attempts: 0", "last_result:", "familiarity:",
        "last_attempt:", "next_review:", "tags: [problem]", "---",
    ]
    body = [
        "> [!info] Problem",
        "> [Open on LeetCode](%s) · Card: %s · Day: %s · Role: %s" % (url, card_link, daylink, role),
        "", "## Trigger", "", "## Approach", "",
        "## Solution", "", "```python", "```", "",
        "## Complexity", "", "- Time:", "- Space:", "",
        "## Mistakes and blank moments", "", "- ", "",
        "## Attempts", "",
        "| Date | Day | Result | Minutes | Familiar (1–5) | Note |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    return "\n".join(fm) + "\n\n" + "\n".join(body) + "\n"


def add_to_card(card_path, note_name):
    text = open(card_path, encoding="utf-8").read()
    lines = text.split("\n")
    try:
        pi = lines.index("## Problems")
    except ValueError:
        sys.exit("Card note has no '## Problems' section.")
    bullet = "- [[%s]]" % note_name
    # Replace the placeholder line if present, else append after the last bullet.
    for i in range(pi + 1, len(lines)):
        if lines[i].startswith("- None yet"):
            lines[i] = bullet
            break
        if lines[i].strip().startswith("```") or lines[i].startswith("## "):
            # End of the static list: insert just before this line.
            j = i
            while j > pi and not lines[j - 1].strip():
                j -= 1
            lines.insert(j, bullet)
            break
    open(card_path, "w", encoding="utf-8", newline="").write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("number", type=int)
    ap.add_argument("title")
    ap.add_argument("card", type=int)
    ap.add_argument("--slug")
    ap.add_argument("--day", type=int, default=0)
    ap.add_argument("--role", default="bonus", choices=["guided", "solo", "bonus"])
    args = ap.parse_args()

    slug = args.slug or slugify(args.title)
    url = "https://leetcode.com/problems/%s/" % slug
    card_name = card_note_name(args.card)
    card_link = "[[%s]]" % card_name

    safe_title = "".join(c for c in args.title if c not in INVALID)
    note_name = "%04d %s" % (args.number, safe_title)
    prob_path = os.path.join(ROOT, "03 Problems", note_name + ".md")
    if os.path.exists(prob_path):
        sys.exit("Problem note already exists: %s" % note_name)

    open(prob_path, "w", encoding="utf-8", newline="").write(
        build_note(args.number, args.title, url, card_link, args.day, args.role))
    add_to_card(os.path.join(ROOT, "02 Cards", card_name + ".md"), note_name)

    print("Created 03 Problems/%s.md" % note_name)
    print("Linked it under %s" % card_name)
    print("Run: py scripts/check_vault.py")


if __name__ == "__main__":
    main()
