#Ex1
# text = input("Enter here: ")
# for char in text:
#     print(char)

#Ex2
# text = input("Enter here: ")
# for i in range(len(text)):
#     print(i)

#Ex3
# text = input("Enter your text: ")
# index = 0
# result = "No"
# while index < len(text):
#     if text[index].isupper():
#         result = "Yes"
#         index = len(text)
#     index += 1  
# print(result)

#Ex4
# text = "3 4 5 6"
# total = 0
# for char in text.replace(" ", ""):
#     print(char)
#     total += int(char)
# print(total)

#Ex5
# text = "454639"
# odd_num = 0
# even_num = 0
# total_num = 0
# sum_even = 0
# for char in text:
#     num = int(char)
#     if num % 2 == 0:
#         even_num += 1
#         sum_even += num
#     else:
#         odd_num += 1
#     total_num += num
# print(odd_num)
# print(even_num)
# print(total_num)
# print(sum_even)
# print(text[::-1])

#Ex6
# num = int(input("Enter num here: "))
# if num % 2 == 1:
#     print("odd number")
# else:
#     print("even number")

#Ex7
# in_range = True
# while in_range:
#     number = int(input("Enter a number: "))
#     if 10 <= number <= 20:
#         print("Continue")
#     else:
#         print("Out of range")
#         in_range = False

#Ex8
# text = "9394884039"
# count_8 = 0
# first_index_8 = -1
# index = 0
# while index < len(text):
#     if text[index] == '8':
#         count_8 += 1
#         if first_index_8 == -1:
#             first_index_8 = index
#     index += 1
# print("count_8:", count_8)
# print("first_index_8:", first_index_8)

#Ex9
# string = "3 4 5 6"
# no_space= string.replace(" ", "")
# print(no_space)
# numbers = string.split()
# doubled_numbers = [str(int(num) * 2) for num in numbers]
# result_doubled = " ".join(doubled_numbers)
# print( result_doubled)

#Ex10
# max_num = 0
# min_num = 0
# for i in range(5):
#     num = int(input("Enter here: "))
# else:
#     if num > max_num:
#         max_num = num
#     elif num < min_num:
#         min = num
# print("Max_num:", max_num)
# print("Min_num:", min_num)


