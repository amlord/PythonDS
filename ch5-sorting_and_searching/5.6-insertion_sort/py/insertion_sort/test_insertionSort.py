from unittest import TestCase
from insertion_sort import insertionSort

__author__ = 'Lawrence'


class TestInsertionSort(TestCase):
    def test_insertionSortEmptyList(self):
        original = []
        result = original
        supposed = []
        insertionSort(result)
        originalStr = "".join(str(e) for e in original)
        resultStr = "".join(str(e) for e in result)
        supposedStr = "".join(str(e) for e in supposed)
        self.assertEqual(
            result,
            supposed,
            "InsertionSort(" + originalStr + ") produces " + resultStr +
            ", rather than " + supposedStr + " which it supposed to be.")

    def test_insertionSortSingletonList(self):
        original = [1024]
        result = original
        supposed = [1024]
        insertionSort(result)
        originalStr = "".join(str(e) for e in original)
        resultStr = "".join(str(e) for e in result)
        supposedStr = "".join(str(e) for e in supposed)
        self.assertEqual(
            result,
            supposed,
            "InsertionSort(" + originalStr + ") produces " + resultStr +
            ", rather than " + supposedStr + " which it supposed to be.")

    def test_insertionSortMultiElementList(self):
        original = [54,26,93,17,77,31,44,55,20]
        result = original
        supposed = [17,20,26,31,44,54,55,77,93]
        insertionSort(result)
        originalStr = "".join(str(e) for e in original)
        resultStr = "".join(str(e) for e in result)
        supposedStr = "".join(str(e) for e in supposed)
        self.assertEqual(
            result,
            supposed,
            "InsertionSort(" + originalStr + ") produces " + resultStr +
            ", rather than " + supposedStr + " which it supposed to be.")