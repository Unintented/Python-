# 函数定义
def greet_user(username):
    """显示简单的问候语"""
    print("Hello! " + username.title())


def describe_pet(animal_type, pet_name):
    """描述宠物"""
    print("I have a " +
          animal_type +
          ", it's name is " +
          pet_name +
          ".")


greet_user('kevin')
# 位置实参
describe_pet('cat', 'hapoon')
# 关键字实参
describe_pet(animal_type='dog', pet_name='liam')


# 还可以给形参指定默认值，若对应位置无实参，则使用默认值
# 细节，将默认值放在后面（不要问为什么）
def make_pizza(color, size='medium'):
    print("I have ordered a " +
          color +
          ", " +
          size +
          " pizza.")


make_pizza('blue')
make_pizza('blue', 'small')
make_pizza(color='green', size='big')
make_pizza(size='big', color='green')


# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('kevin', 'chan')
print(musician)
musician = get_formatted_name('liam', 'lee', 'd')
print(musician)
