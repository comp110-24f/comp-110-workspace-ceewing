"""Exercise 08."""
from __future__ import annotations
__author__ = "730566374"


class Node:


    """Definition of a class names Node."""
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):


        """Makes new instance of a node."""
        #  basic call
        self.value = val
        self.next = next

    def __str__(self) -> str:


        """Makes a str representation of a linked list."""
        #  called automatically, magic method.
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"

two: Node = Node(2, None)
one: Node = Node(1, two)
one_two: Node = Node(1, Node(2, None))
courses: Node = Node(110, Node(210, Node(301, None)))
#  prints one
#  print (str(courses))
#  print (courses)

def to_str(head: Node | None) -> str:


    """Turns head to str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:


    """Return the last value of a non-empty list."""
    #  Base case for when the head is the last node -> return its value
    print(f"Enter last({head.value})")
    if head.next is None:
        print (f"Return base case: {head.value}")
        return head.value
    #  Recursive case, to figure out the last node (recursive call) -> return that value
    else:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest    

    print(last(one)) #  should print 2
    print(last(courses)) #  should print 301
    print(last(two)) #  should print 2

    def recursive_range(start: int, end: int) -> Node | None:


        """Build a list recursivly from start to end."""
        #  recursive range function that makes a list from a start to an end point
        #  TODO: Can you handle an edge case? what is it?
        #  if so raise a ValueError("invalid arguments, start > end")
        if start > end:
            raise ValueError("invalid arguments")
        if start == end:
            #  base case
            return None
        else: 
            #  recursive case
            #  1. handle the first value in your new list here!
            first: int = start
            #  2. let the rest of the list be handled recursivly!
            rest: Node | None = recursive_range(start + 1, end)
            return Node(first, rest)
    
    a_list: Node | None = recursive_range(110, 113)
    print(a_list)

def value_at(head: Node | None, index: int) -> int:


    """Returns the value that in in a node given at an index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    else:
       return value_at(head.next, index - 1)
    
def max(head: Node | None) -> int:


    """Given a Node, return the largest value in the list."""
    if head is None:
        #  base case
        raise ValueError("Cannot call max with None")
    if head.next is None:
            return head.value
    rest: int = max(head.next)
        #  variable for recursion
    return head.value if head.value > rest else rest

def linkify(items: list[int]) -> Node | None:


    """Makes linked nodes from a list."""
    if items == []:
        #  checks to see if list if empty
        return None
    return Node(items[0], linkify(items[1:]))

def scale(head: Node | None, factor: int) -> Node | None:


    """Makes a new linked list from the given node by the factor given."""
    if head is None:
        #  base case
        return None
    return Node(head.value * factor, scale(head.next, factor))