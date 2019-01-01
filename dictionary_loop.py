# 遍历字典item()
user_0 = {
    'username': 'Unintented',
    'first_name': 'kevin',
    'last_name': 'chan',
}
for key, value in user_0.items():
    print("Key:" + key)
    print("Value:" + value + '\n')

# 遍历所有键key(),若不用此函数，因为for后只有一个变量，因此结果不变
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi!" +
              name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# key()并非只能用来遍历，实际上，它返回一个列表，包含字典中所有的键
# 同时还可以用sorted(favorite_languages.keys())对所有值进行排序
if 'kevin' not in favorite_languages.keys():
    print("kevin".title() + ", please take our poll!")
# 遍历字典中所有的值
print("\nThe following languages has been mentioned.")
for language in favorite_languages.values():
    print(language.title())
# 遍历所有值同时剔除重复项set()
print("\nUnique language")
for language in set(favorite_languages.values()):
    print(language.title())

# 嵌套
# 列表中存储字典
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
for alien in aliens[:7]:
    print(alien)
# 字典中存储列表
pizza = {'crust': 'thick', 'toppings': ['mushroom', 'cheese']}
print("You ordered a " +
      pizza['crust'] +
      " pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping)
# 字典中嵌套字典
