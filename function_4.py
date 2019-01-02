# 传递任意数量的实参,将其封装到一个元组中
# 若有非接收任意数量的形参，则放在最前面(结合位置实参)


def make_pizza(size, *toppings):
    print("The following toppings in a " +
          str(size) +
          "-inch pizza:")
    for topping in toppings:
        print("-" + topping)


# 此if保证了只有在执行当前文件才会调用函数，其他通过引入方式的不会调用
if __name__ == '__main__':
    make_pizza(15, 'pepperoni')
    make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


# 将接收到的额外键值对封装到user_info的空字典中，对其的操作同正常的字典
def build_profile(first_name, last_name, **user_info):
    """"""
    profile = {}
    profile['first'] = first_name
    profile['last'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile


if __name__ == '__main__':
    user_profile = build_profile('albert', 'einstein',
                                 loction='princeton',
                                 field='physics')
    print(user_profile)
