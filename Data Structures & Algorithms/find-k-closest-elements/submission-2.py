class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = self.binarySearch(arr, x)
        j = i+1

        res = []
        while ( k > 0 and i>=0 and j<len(arr)):
            if ( abs(arr[i] - x) <= abs(arr[j]-x)):
                res.append(arr[i])
                i-=1
            else:
                res.append(arr[j])
                j+=1
            k-=1
        while ( k>0 and i >=0):
            res.append(arr[i])
            i-=1
            k-=1
        while ( k>0 and j< len(arr)):
            res.append(arr[j])
            j+=1
            k-=1
        res.sort()
        return res
    

    def binarySearch(self, arr, x):
        l=0
        r = len(arr)-1
        res = 0
        while l <=r:
            mid = (l+r)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                res = mid
                l= mid+1
            else:
                r= mid-1
        return res
        

        