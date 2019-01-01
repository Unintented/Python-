# 迭代列表中每个元素，通过缩进判断是否属于for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + '.\n')
print("Thank you, every one!")
# 顺序打印数字，不包括最后一个
for value in range(1, 5):
    print(value)
# 将一连串数字转化成列表
numbers = list(range(1, 6))
print(numbers)
# 从2开始，每次加2，超过11停止
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# 创建需要的数字列表
square_numbers = []
for value in range(1, 11):
    squre = value ** 2
    square_numbers.append(squre)
print(square_numbers)
# 最值、求和
print(max(square_numbers))
print(min(square_numbers))
print(sum(square_numbers))
# 列表解析
square_numbers_2 = [value ** 2 for value in range(11, 21)]
print(square_numbers_2)
# 列表的一部分称为切片，下标从0开始，不包括最后一个元素，可省略起始或终止索引
print(square_numbers_2[2:5])
print(square_numbers_2[-3:])
# 遍历切片
for value in square_numbers_2[-5:-3]:
    print(value)
# 列表复制
my_foods = ['pizza', 'ice cream', 'noodles']
# 此种方式是将原列表的备份赋给新列表，二者独立变化；若无中括号，则表示将新列表关联到原列表上，二者一变全变
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)


