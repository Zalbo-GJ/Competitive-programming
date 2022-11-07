
class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        large = i
        l = 2*i+1
        r = 2*i+2

        if (l < n and arr[l] > arr[large]):
            large = l
        if (r < n and arr[r] > arr[large]):
            large = r
        if large != i:
            arr[i], arr[large] = arr[large], arr[i]
            self.heapify(arr, n, large)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n-2, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
