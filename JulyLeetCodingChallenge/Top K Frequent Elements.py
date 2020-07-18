"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
- It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        answer = []
        for x in nums:
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        sort_frequency = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        for key, value in sort_frequency:
            if(k==0):
                break
            answer.append(key)
            k = k - 1
        return answer