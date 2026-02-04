# Write a program to count word frequency in a string

# s = input("Enter a sentence: ")

# words = s.split()
# freq = {}

# for w in words:
#     freq[w] = freq.get(w, 0) + 1

# print(freq)



# st=s.split()

# fre={}
# for word in st:
#   if word in fre:
#     fre[word]+=1
#   else:
#     fre[word] =1
# print(fre)

# Given a list of integers and a target, return indices of two numbers whose sum equals the target. [1,2,6,7,4] target = 10
# def targetSum(numbers, target):
#     x = {}
#     for i, n in enumerate(numbers):
#         if 10 -n in x:
#             return [x[target - n], i]
#         x[n] = i

# print(targetSum([1,2,6,7,4], 10))

# enumerate([1,2,6,7,4]) -> [(0, 1), (1, 2), (2, 6), (3, 7), (4, 4)]
# x ={
#     1:0,
#     2:1,
#     6:2,
#     7:3,
#     4:4
# }


#Remove duplicates from sorted list and return lenght after removing duplicate elements
#[3,4,4,5,6,7,7,8] [3,4,5,6,7,8]

# lst = [3,4,3,4,5,6,7,2,7,8]
# lst.sort()
# print(lst)

# newlst = set(lst)
# print(len(newlst))

# def removeDuplicates(lst):
#     count = 0
#     for i in range(1, len(lst)):
#         if lst[i] != lst[count]:
#             count += 1
#             lst[count] = lst[i]
#     return count +1

# print(removeDuplicates(lst))

# def removeDupl(lst):
#     uniq = []
#     for i in lst:
#         if i not in uniq:
#             uniq.append(i)  
#     return uniq

# print(removeDupl([3,4,3,4,5,6,7,2,7,8]))
# print(len(removeDupl([3,4,3,4,5,6,7,2,7,8])))