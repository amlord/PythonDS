from unittest import TestCase
from queue import Queue

__author__ = 'Lawrence'


class TestQueue(TestCase):
    def test_isEmpty(self):
        q = Queue()
        self.assertEqual(
            len(q.items),
            0,
            "Queue s is not empty on initialization.")
        self.assertTrue(q.isEmpty(), "Queue q is not empty.")

    def test_enqueue(self):
        q = Queue()

        q.enqueue(4)
        self.assertEqual(
            len(q.items),
            1,
            "Queue q doesn't contain 1 element after enqueuing element 4.")
        self.assertEqual(
            q.items[0],
            4,
            "Queue q doesn't contain element 4 at its rear after enqueuing " +
            "element 4.")

        q.enqueue("dog")
        self.assertEqual(
            len(q.items),
            2,
            "Queue q doesn't contain 2 elements after enqueuing element 'dog'.")
        self.assertEqual(
            q.items[0],
            "dog",
            "Queue q doesn't contain element 'dog' at its rear after " +
            "enqueuing element 'dog'.")
        self.assertEqual(
            q.items[1],
            4,
            "Queue q doesn't contain element 4 at its front after enqueuing " +
            "element 'dog'.")

        q.enqueue(True)
        self.assertEqual(
            len(q.items),
            3,
            "Queue q doesn't contain 3 elements after enqueuing element True.")
        self.assertEqual(
            q.items[0],
            True,
            "Queue q doesn't contain element True at its rear after " +
            "enqueuing element True.")
        self.assertEqual(
            q.items[1],
            "dog",
            "Queue q doesn't contain element 'dog' at its middle after " +
            "enqueuing element True.")
        self.assertEqual(
            q.items[2],
            4,
            "Queue q doesn't contain element 4 at its front after enqueuing " +
            "element True.")


    def test_dequeue(self):
        q = Queue()
        q.enqueue(4)
        q.enqueue("dog")
        q.enqueue(True)
        q.enqueue(8.4)

        self.assertEqual(
            q.dequeue(),
            4,
            "Queue q doesn't return element on the first dequeuing.")
        self.assertEqual(
            len(q.items),
            3,
            "Queue q doesn't remove element 4 at its front after the first " +
            "dequeuing.")
        self.assertEqual(
            q.items[2],
            "dog",
            "Queue q doesn't contain element 'dog' at its front after the " +
            "first dequeuing.")
        self.assertEqual(
            q.items[1],
            True,
            "Queue q doesn't contain element True at its middle after the " +
            "first dequeuing.")
        self.assertEqual(
            q.items[0],
            8.4,
            "Queue q doesn't contain element 8.4 at its rear after the first " +
            "dequeuing.")

        self.assertEqual(
            q.dequeue(),
            "dog",
            "Queue q doesn't return element 'dog' on the second dequeuing.")
        self.assertEqual(
            len(q.items),
            2,
            "Queue q doesn't remove element 'dog' at its front after the " +
            "second dequeuing.")
        self.assertEqual(
            q.items[1],
            True,
            "Queue q doesn't contain element True at its front after the " +
            "second dequeuing.")
        self.assertEqual(
            q.items[0],
            8.4,
            "Queue q doesn't contain element 8.4 at its rear after the "
            "second dequeuing.")

        self.assertEqual(
            q.dequeue(),
            True,
            "Queue q doesn't return element True on the third dequeuing.")
        self.assertEqual(
            len(q.items),
            1,
            "Queue q doesn't remove element True at its front after the " +
            "third dequeuing.")
        self.assertEqual(
            q.items[0],
            8.4,
            "Queue q doesn't contain element 8.4 at its front after the "
            "third dequeuing.")

        self.assertEqual(
            q.dequeue(),
            8.4,
            "Queue q doesn't return element 8.4 on the fourth dequeuing.")
        self.assertEqual(
            len(q.items),
            0,
            "Queue q doesn't remove element 8.4 at its front after the " +
            "third dequeuing.")

    def test_size(self):
        q = Queue()
        self.assertEqual(
            q.size(),
            0,
            "The size of empty Queue q is not 0.")

        q.enqueue(4)
        self.assertEqual(
            q.size(),
            1,
            "The size of Queue q doesn't expand to 1 after enqueuing element " +
            "4.")

        q.enqueue("dog")
        self.assertEqual(
            q.size(),
            2,
            "The size of Queue q doesn't expand to 2 after enqueuing element " +
            "'dog'.")

        q.dequeue()
        self.assertEqual(
            q.size(),
            1,
            "The size of Queue q doesn't shrink to 1 after dequeuing once.")

        q.dequeue()
        self.assertEqual(
            q.size(),
            0,
            "The size of Queue q doesn't shrink to 0 after dequeuing twice.")