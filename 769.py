"""769. Max Chunks To Make Sorted"""

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        min_index_for_chunk_end = arr[0]
        chunks = 0

        for i in range(len(arr)):
            min_index_for_chunk_end = max(min_index_for_chunk_end, arr[i])
            if i == min_index_for_chunk_end:
                chunks += 1

        return chunks
