class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #variables
        if nums1==[] or nums2==[]:
            return []
        f={}
        s={}
        result={}
        final=[]
        while nums1!=[]:
            temp=nums1.pop()
            if temp in f:
                f[temp]+=1
            else:
                f[temp]=1
        while nums2!=[]:
            temp=nums2.pop()
            if temp in s:
                s[temp]+=1
            else:
                s[temp]=1
        #routine
        for key in f.keys() + s.keys():
            try:
                result[key]=min(f[key], s[key])
            except:
                continue
        for key in result.keys():
            while result[key]>0:
                final.append(key)
                result[key]-=1
        return final
