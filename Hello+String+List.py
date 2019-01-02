message = "Hello Python world!"
print(message)

message = "Ada "
print(message.title())  # 首字母大写
print(message.lower())  # 全部小写 upper...大写

# +表示字符拼接
first_name = message
last_name = "Lovelace"
full_name = first_name + " " + last_name
message = "Hello," + full_name.title()
print(message)

# 去空格
favorite_language = " hapoon "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

print(0.2 + 0.1)
print(3 // 2)
print(3 / 2)

print("Happy " + str(23) + "rd Birthday!")
# import this

# 列表，下标为正或负
month = ['january', 'february', 'march', 'april', 'may', 'june']
print(month)
print(month[0])
print(month[-1])
message = "I like " + month[1].title()
print(message)
# 插入元素
month.append('july')
print(month)
month.insert(8, 'august')  # 大于等于7都插在7处
print(month)
print(month[7])  # 因为7后无元素，若输出下标大于7，则不输出
# 删除元素
# 删除后不可访问
del month[2]
print(month)
# 删除后可以访问
remove_month = month.pop()
print(month)
print(remove_month)
remove_month = month.pop(1)
print(month)
print(remove_month)
# 根据值删除，只删除第一个匹配的
month.remove('january')
print(month)

# 永久排序及逆序
month.sort()
print(month)
month.sort(reverse=True)
print(month)
# 临时排序
print(sorted(month))
print(sorted(month, reverse=True))
print(month)

# 永久倒序
month.reverse()
print(month)
print(month.__len__())
