---
type: card
card: 12
name: Linked lists
days: [13, 15]
tags: [card]
---

> [!tip] Use when
> Reverse a list, build one behind a dummy head, detect a cycle. Solves #206 and #141.

## Card

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next                 # 1. save
        cur.next = prev                # 2. flip
        prev = cur                     # 3. move prev
        cur = nxt                      # 4. move cur
    return prev

# Dummy node: a fake head, so the first real node is not a special case
dummy = tail = ListNode()
# ...each time: tail.next = node, then tail = tail.next
# at the end: return dummy.next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:          # slow moves 1, fast moves 2
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0206 Reverse Linked List]]
- [[0021 Merge Two Sorted Lists]]
- [[0083 Remove Duplicates from Sorted List]]
- [[0141 Linked List Cycle]]
- [[0876 Middle of the Linked List]]
- [[0019 Remove Nth Node From End of List]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
