import sorting
import generate
import numpy
import random
from element import Element
import test
# 
# 
# # def partition(arr,low,high): 
# #     i = ( low-1 )         # index of smaller element 
# #     pivot = arr[low]     # pivot 
# #   
# #     for j in range(low , high): 
# #   
# #         # If current element is smaller than or 
# #         # equal to pivot 
# #         if   arr[j] <= pivot: 
# #           
# #             # increment index of smaller element 
# #             i = i+1 
# #             arr[i],arr[j] = arr[j],arr[i] 
# #   
# #     arr[i],arr[low] = arr[low],arr[i] 
# #     return ( i ) 
# # 
# # 
# # t = [5,2,7,8,1,3,4]
# # partition(t, 0, len(t))
# def cmp (self,other):
#         if self.value == other.value:
#             return 0
#         elif self.value < other.value:
#             return -1
#         else:
#             return 1
#         
# def partition (s, p, cmp):
#     t = s["data"]
#     left = s["left"]
#     right = s["right"]
#     i = ( left-1 )         # index of smaller element 
#     pivot = t[p]     # pivot
#     t[0],t[p] = t[p], t[0]
#     if left == right:
#         print("ERROR")
#         return (s,s)
#     else:
#         for j in range(left , right+1): 
#             # If current element is smaller than or 
#             # equal to pivot
#             c = cmp(t[j], pivot)
#             if (c == -1) or (c == 0):
#                 # increment index of smaller element 
#                 i = i+1 
#                 t[i],t[j] = t[j],t[i] 
#         t[i],t[left] = t[left],t[i]
#     s1 = { "data" : t, "left" : left, "right" : i-1 }
#     s2 = { "data" : t, "left" : i+1, "right" : right }
#     return (s1,s2)
# 
# # t = generate.random_array(30)
# # partition({ "data" : t, "left" : 0, "right" : len(t) - 1}, cmp)
# #
# # t = np.array([Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
# # print(t)
# # p = {'left':0,'right':len(t)-1,'data':t}
# # p1,p2 = partition(p,cmp)
# # p1['data'][p1['left']:p1['right']+1]
# # p2['data'][p2['left']:p2['right']+1]
# 
# 
# def quicksort_slice(s, rand,cmp):
#     if rand == True:
#         c = random_pivot(s)
#     else:
#         c = 0
#     t = s["data"]
#     left = s["left"]
#     right = s["right"]
#     c = random_pivot(s)
#     if left != right: 
#         # pi is partitioning index, arr[p] is now 
#         # at right place 
#         s1, s2 = goodPartition(s, c, cmp) 
#         # Separately sort elements before 
#         # partition and after partition
#         quicksort_slice(s2,rand, cmp)
#         quicksort_slice(s1, rand,cmp)
#     
# def quicksort (t,rand,cmp):
#     p = dict()
#     p["data"] = t
#     p["left"] = 0
#     p["right"] = len(t) - 1
#     return quicksort_slice (p,rand, cmp)
# 
# def random_pivot(s):
#     return random.randint(s["left"], s["right"])
#  
# 
# # t = np.array([Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
# # print(t)
# # p = {'left':0,'right':len(t)-1,'data':t}
# # c = random_pivot(p)
# # s1, s2= partition(p, c, cmp)
# # print(c)
# # print(t)
# #quicksort(t, cmp)
# 
# #t = np.array([Element(i) for i in [6, 1, 3, 4, 2, 5, 8, 9, 7]])
# 
# #c = random_pivot(p)
# #quicksort(t, cmp)
# 
# 
# 
# 
# 
# 
# 
# 
# 
def goodPartition(s, cmp):
    t = s["data"]
    low = s["left"]
    hi = s["right"]
    p = random_pivot(s)
    pivotValue = t[p]
    t[p], t[low] = t[low], t[p]
    border = low
    
    for i in range(low, hi+1):
        c = cmp(t[i], pivotValue)
        if c == -1:
            border += 1
            t[i], t[border] = t[border], t[i]
    t[low], t[border] = t[border], t[low]
    if border == low:
        border +=1
    s1 = { "data" : t, "left" : low, "right" : border-1 }
    s2 = { "data" : t, "left" : border, "right" : hi }
    return (s1,s2)    


def quicksort (t,cmp):  
    p = dict()
    p["data"] = t
    p["left"] = 0
    p["right"] = len(t) - 1
    return quicksort_slice (p,cmp)


def quicksort_slice (s, cmp):
    t = s["data"]
    left = s["left"]
    right = s["right"]
    if left != right: 
        # pi is partitioning index, arr[p] is now 
        # at right place 
        s1, s2 = goodPartition(s,cmp) 
        # Separately sort elements before 
        # partition and after partition 
        quicksort_slice(s1, cmp)
        quicksort_slice(s2, cmp)



def random_pivot(s):
    return random.randint(s["left"], s["right"])


def cmp (x,y): 
    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1

t = numpy.array([Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
quicksort(t,cmp)





t = numpy.array([Element(i) for i in [5, 6, 1, 3, 4, 9, 8, 2, 7]])
p = {'left':0,'right':len(t)-1,'data':t}
quicksort_slice (p, cmp)



p = {'left':0,'right':len(t)-1,'data':t}
p1,p2 = goodPartition(p,cmp)
p1['data'][p1['left']:p1['right']+1]


"""
>>> p1,p2 = partition(p, c,cmp)
>>> p1['data'][p1['left']:p1['right']+1]
array([2, 1, 3, 4], dtype=object)
>>> p2['data'][p2['left']:p2['right']+1]
array([5, 9, 8, 6, 7], dtype=object)
"""



