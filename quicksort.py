class Solution(object):
    def partition(self,nums, start, end):
        pivot = nums[end]
        print "pivot: " + str(pivot) + " nums: " + str(nums)
        i = start - 1
        for j in range(start, end):
            if nums[j] <= pivot:
                i = i + 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[end],nums[i+1] = nums[i+1], nums[end]
        return i+1

    def hoarePartition(self, nums, start, end):
        pivot = nums[start]
        print "pivot: " + str(pivot) + " nums: " + str(nums)
        i = start-1
        j = end+1
        while True:
            while True:
                j = j-1
                if nums[j] <= pivot: break
            while True:
                i = i+1
                if nums[i] >= pivot: break
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
            else: return j

    def quickSort(self, nums, start, end):
        if start >= end: return
        #q = self.partition(nums, start, end)
        q = self.hoarePartition(nums, start, end)
        self.quickSort(nums, start, q)
        self.quickSort(nums, q+1, end)

    def sort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums)-1)

list = [2,8,7,1,3,5,6,4]

print list
Answer = Solution();
Answer.sort(list)
print list
