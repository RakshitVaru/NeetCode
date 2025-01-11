class Solution:
    def merge_sort_divider (self, pairs:List[Pair], s: int, e: int) -> List[Pair]:
        if e-s+1 <=1:
            return pairs
        m= (s+e)//2
        self.merge_sort_divider(pairs,s,m) 
        self.merge_sort_divider(pairs,m+1,e)
        self.merge(pairs,s,m,e)
        return pairs

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_sort_divider(pairs,0,len(pairs)-1)
    
    def merge(self, arr: List[Pair], s:int, m:int, e:int) ->None:
        left=arr[s: m + 1]
        right=arr[m + 1: e+1]
        i,j,k=0,0,s
        
        while i<len(left) and j<len(right):
            if left[i].key <= right[j].key:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        
        while j <len(right):
            arr[k]=right[j]
            j+=1
            k+=1