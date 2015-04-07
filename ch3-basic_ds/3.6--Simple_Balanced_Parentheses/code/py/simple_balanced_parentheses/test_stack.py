from unittest import TestCase
from stack import Stack

__author__ = 'Lawrence'


class TestStack(TestCase):
    def test_is_empty(self):
        s = Stack()
        self.assertEqual(len(s.items),
            0,
            "Stack s is not empty on initialization.")
        self.assertTrue(s.is_empty(),"Stack s is not empty.")

    def test_push(self):
        s = Stack()
        self.assertTrue(s.is_empty(),"Stack s is not empty on initialization.")

        s.push(4)
        self.assertEqual(
            len(s.items),
            1,
            "Stack s doesn't contain 1 element after the first pushing.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 on its top after the " +
            "first pushing.")

        s.push("dog")
        self.assertEqual(
            len(s.items),
            2,
            "Stack s doesn't contain 2 elements after the second pushing.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom after the " +
            "second pushing.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' on its top after the " +
            "second pushing.")

        s.push(True)
        self.assertEqual(
            len(s.items),
            3,
            "Stack s doesn't contain 3 elements after the third pushing.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom after the " +
            "third pushing.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' at its middle after the " +
            "third pushing.")
        self.assertEqual(
            s.items[2],
            True,
            "Stack s doesn't contain element True on its top after the " +
            "third pushing.")

    def test_pop(self):
        s = Stack()
        s.push(4)
        s.push("dog")
        s.push(True)
        self.assertEqual(
            len(s.items),
            3,
            "Stack s doesn't contain 3 elements on initialization.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 on its bottom on " +
            "initialization.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' at its middle on " +
            "initialization.")
        self.assertEqual(
            s.items[2],
            True,
            "Stack s doesn't contain element True on its top on " +
            "initialization.")

        self.assertEqual(
            s.pop(),
            True,
            "Stack s doesn't cast element True on popping once.")
        self.assertEqual(
            len(s.items),
            2,
            "Stack s doesn't contain 2 elements after popping once.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom after " +
            "popping once.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' on its top after " +
            "popping once.")

        self.assertEqual(
            s.pop(),
            "dog",
            "Stack s doesn't cast element `dog' on popping twice.")
        self.assertEqual(
            len(s.items),
            1,
            "Stack s doesn't contain 1 element after popping twice.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 on its top after " +
            "popping twice.")

        self.assertEqual(
            s.pop(),
            4,
            "Stack s doesn't cast element 4 on popping for the third time.")
        self.assertEqual(
            len(s.items),
            0,
            "Stack s isn't empty after popping for the third time.")

    def test_peek(self):
        s = Stack()
        s.push(4)
        s.push("dog")
        s.push(True)
        self.assertEqual(
            len(s.items),
            3,
            "Stack s doesn't contain 3 elements on initialization.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom on " +
            "initialization.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' at its middle on " +
            "initialization.")
        self.assertEqual(
            s.items[2],
            True,
            "Stack s doesn't contain element True on its top on " +
            "initialization.")

        self.assertEqual(
            s.peek(),
            True,
            "Stack s doesn't return element True on the first peeking.")
        self.assertEqual(
            len(s.items),
            3,
            "Stack s doesn't contain 3 elements after the first peeking.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom after the " +
            "first peeking.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' at its middle after the " +
            "first peeking.")
        self.assertEqual(
            s.items[2],
            True,
            "Stack s doesn't contain element True on its top after the " +
            "first peeking.")

        s.pop()
        self.assertEqual(
            len(s.items),
            2,
            "Stack s doesn't contain 2 elements after popping once.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom after " +
            "popping once.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' on its top after " +
            "popping once.")

        self.assertEqual(s.peek(),
            "dog",
            "Stack s doesn't return element `dog' on the second peeking.")
        self.assertEqual(
            len(s.items),
            2,
            "Stack s doesn't contain 2 elements after the second peeking.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at its bottom after the " +
            "second peeking.")
        self.assertEqual(
            s.items[1],
            "dog",
            "Stack s doesn't contain element `dog' on its top after the " +
            "second peeking.")

        s.pop()
        self.assertEqual(
            len(s.items),
            1,
            "Stack s doesn't contain 1 elements after popping twice.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 on its top after popping " +
            "twice.")

        self.assertEqual(
            s.peek(),
            4,
            "Stack s doesn't return element 4 on the third peeking.")
        self.assertEqual(
            len(s.items),
            1,
            "Stack s doesn't contain 1 element after the third peeking.")
        self.assertEqual(
            s.items[0],
            4,
            "Stack s doesn't contain element 4 at on its top after the " +
            "third peeking.")

        s.pop()
        self.assertEqual(
            len(s.items),
            0,
            "Stack s isn't empty after popping for 3 times.")


    def test_size(self):
        s = Stack()
        self.assertEqual(
            len(s.items),
            0,
            "Stack s is not empty on initialization.")
        self.assertEqual(
            s.size(),
            0,
            "Stack s is not empty on initialization.")

        s.push(4)
        self.assertEqual(
            s.size(),
            1,
            "The size of Stack s is not 1 after pushing once.")
        s.push("dog")
        self.assertEqual(
            s.size(),
            2,
            "The size of Stack s is not 2 after pushing twice.")
        s.pop()
        self.assertEqual(
            s.size(),
            1,
            "The size of Stack s is not 1 after pushing twice and popping " +
            "once.")
        s.pop()
        self.assertEqual(
            s.size(),
            0,
            "The size of Stack s is not 0 after pushing twice and popping " +
            "twice.")