cars = ['audi', 'bmw', 'subaru', 'toyota']
# if用法，注意几个冒号
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# 字符串区分大小写
car = 'BMW'
print(car == 'bmw')
print(car.lower() == 'bmw')

# 多个条件判断
age_1 = 15
age_2 = 23
if age_1 > 13 and age_2 > 13:
    print('all above 13')
if age_1 > 18 or age_2 > 18:
    print('at least one prove above 18')

# 判断特定值是否在列表中
banned_users = ['sam', 'kevin', 'peter']
user = 'choloe'
if user not in banned_users:
    print(user.title() + ', you can post a respond if you wish.')
else:
    print(user.title() + ',you are not allowed to comment.')

# if-elif-else
age = 13
if age < 5:
    price = 0
elif age < 12:
    price = 10
else:
    price = 20
print("Your admission cost is $" + str(price) + ".")

# 判断列表是否为空
requested_topping = []
if requested_topping:
    print("We still have pizza.")
else:
    print("Sorry,there is no pizza left.")
