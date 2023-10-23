# List
# List Slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[3:5]) # [4, 5]
print(a[:4]) # [1, 2, 3, 4]
print(a[7:]) # [8, 9, 10]

print(a[len(a)-1]) # 10
print(a[-1]) # 10
print(a[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::2]) # [1, 3, 5, 7, 9]
print(a[-1::-2]) # [10, 8, 6, 4, 2]

print(a[len(a)-1::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[-1::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print() # List Comprehension
c = [1, 2, 3, 4, 5]
c_square = [n**2 for n in c]
print(c_square) # [1, 4, 9, 16, 25]

print(); print() # Numpy: NUMerical PYthon
# 배열 생성
import numpy as np
a1 = np.arange(10)
print(a1) # [0 1 2 3 4 5 6 7 8 9]
print(a1.shape) # (10,)

a2 = np.arange(0, 10, 2)
print(a2) # [0 2 4 6 8]
print(a2.shape) # (5,)

a3 = np.zeros(5)
print(a3) # [0. 0. 0. 0. 0.]
print(a3.shape) # (5,)

a4 = np.zeros((2, 3)) # 실수로 초기화 됨
print(a4)
# [[0. 0. 0.]
#  [0. 0. 0.]]
print(a4.shape) # (2, 3) 2행 3열
a4
# array([[0., 0., 0.],
#        [0., 0., 0.]])
# print(a4)와 a4 : a4는 array()로 print(a4)를 감싸고 쉼표 추가됨

a5 = np.full((2, 3), 8)
print(a5)
# [[8 8 8]
#  [8 8 8]]
print(a5.shape) # (2, 3)

a6 = np.eye(4)
print(a6)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
print(a6.shape) #(4, 4)

a7 = np.random.random((2, 4)) # 2행 4열 array 생성 후 [0.0, 1.0) 범위에서 랜덤값 초기화
print(a7)

print() # Array Indexing
list1 = [1, 2, 3, 4, 5]
r1 = np.array(list1)
print(r1) # [1 2 3 4 5]
print(list1) # [1, 2, 3, 4, 5]

list2 = [6, 7, 8, 9, 0]
r2 = np.array([list1, list2])
print(r2)
# [[1 2 3 4 5]
#  [6 7 8 9 0]]
print(r1[[2, 4]]) # [3 5], r1의 2번 요소와 4번 요소

print() # Boolean Indexing
print(r1>2) # [False False  True  True  True]
print(r1[r1>2]) # [3 4 5]
nums = np.arange(20)
print(nums) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
odd_nums = nums[nums%2 == 1]
print(odd_nums) # [ 1  3  5  7  9 11 13 15 17 19]

a = np.array([[1,2,3,4,5],
            [4,5,6,7,8],
            [9,8,7,6,5]])
print(a)

b1 = a[1:3, :3]
print(b1)
# [[4 5 6]
#  [9 8 7]]
b2 = a[-2:, -2:]
print(b2)
# [[7 8]
#  [6 5]]
b3 = a[1:, 2:]
print(b3)
# [[6 7 8]
#  [7 6 5]]
b4 = a[2:, :]
print(b4)
# [[9 8 7 6 5]]
print(b4.shape) #(1, 5)

print() # Dot Product, 행렬의 곱셈
x2 = np.array([[1,2,3], [4,5,6]])
y2 = np.array([[7,8], [9,10], [11,12]])
print(np.dot(x2,y2))
# [[ 58  64]
#  [139 154]]

print() # Numpy Sorting
ages = np.array([34, 12, 37, 5, 13])
sorted_ages = np.sort(ages)
print(sorted_ages) # [ 5 12 13 34 37]
print(ages) # [34 12 37  5 13]
ages.sort()
print(ages) # [ 5 12 13 34 37]
ages = np.array([34,12,37,5,13])
print(ages.argsort()) # [3 1 4 0 2] 인덱스 소트
