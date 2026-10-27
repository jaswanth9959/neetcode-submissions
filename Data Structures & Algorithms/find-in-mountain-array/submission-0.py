class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l=1
        r = length - 2

        while l <= r:
            m = (l+r)//2
            left,mid,right = mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)

            if left < mid < right:
                l = m +1
            elif left > mid > right:
                r = m-1
            else:
                break
        peak = m


        l = 0
        r = peak

        while l <= r:
            mid = (l+r)//2
            midVal = mountainArr.get(mid)
            if midVal < target:
                l = mid +1
            elif midVal > target:
                r = mid -1
            else:
                return mid
        
        l = peak+1
        r = length -1

        while l <= r:
            mid = (l+r)//2
            midVal = mountainArr.get(mid)
            if midVal > target:
                l = mid +1
            elif midVal < target:
                r = mid -1
            else:
                return mid
        return -1
        