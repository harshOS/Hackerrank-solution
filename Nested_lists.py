#problem link - https://www.hackerrank.com/challenges/nested-list/problem
# if __name__ == '__main__':
#     arr = []
#     max1 = 0
#     def sortSecond(val):
#         return val[1]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         if max1 < score:
#             max1 = score
#         arr.append([name,score])
#         arr.sort()
#         itr = len(arr)
#
#     while(itr !=0 ):
#         for i in range(itr):
#             if arr[i][1] == max1:
#                 arr.pop(i)
#                 itr -= 1
#         itr -= 1
#     arr2 = arr
#     for i in range(len(arr)):
#         if arr[i][1] == max(arr):
#             print(arr[i][0])

if __name__ == '__main__':
    score_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]
    new_list = []
    for i in score_list:
        new_list.append([i, score_list[i]])
    new_list.sort()
    result = new_list[1][1]
    result.sort()
    print (*result, sep = "\n")