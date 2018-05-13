#!/bin/python3

"""
Link: https://www.hackerrank.com/challenges/ctci-contacts/problem

Approach:

ContactBook contains:
    the number of entries at that node and a list of 26 dictionaries, one for each letter
    every entry is key = letter, value = ContactBook referring to the second letter
    every ContactBook in the tree stores the amount of names it contains

when storing, the tree is examined basing on the name, every time a new node is visited the first letter is removed from the name
and if the name is empty the count of the node that reached empty name is incremented, also all the nodes before it are incremented.
Otherwise the corresponding ContactBook child is visited with the reduced name until a match is found or the appropriate child node
is created.

when the number of contacts with a name is asked the tree is examined based on the name, in the same way the name gets reduced
until it reaches zero, if it reaches zero we have a match in the whole contact book and return the count at that node.
If a node with no suitable child is reached before the name reaches zero chars then we have no match.
"""


class ContactBook:
    def __init__(self):
        self.contacts = dict()
        self.count = 0

    def add_contact(self, contact):
        # If the name reached zero chars then this is the node where to store it.
        if len(contact) == 0:
            self.count += 1
            return

        # Otherwise keep going deeper in the tree.
        first_char = contact[:1]
        if first_char not in self.contacts:
            self.contacts[first_char] = ContactBook()

        # Visit the next node and increment the count of this node.
        self.contacts[first_char].add_contact(contact[1:])
        self.count += 1

    def find_contact(self, contact):
        # If the name reached zero chars then this is the node we need.
        if len(contact) == 0:
            return self.count

        # Otherwise keep going deeper in the tree if possible.
        first_char = contact[:1]
        if first_char not in self.contacts:
            return 0
        else:
            return self.contacts[first_char].find_contact(contact[1:])


contact_book = ContactBook()


def add(contact):
    contact_book.add_contact(contact)


def find(contact):
    return contact_book.find_contact(contact)


def main():
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op == 'add':
            add(contact)
        elif op == "find":
            print(str(find(contact)))


if __name__ == "__main__":
    main()
