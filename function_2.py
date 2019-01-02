# 返回字典
def build_person(first_name, last_name, age=""):
    person = {'first': first_name.title(),
              'last': last_name.title()}
    if age:
        person['age'] = age
    return person


if __name__ == '__main__':
    musician = build_person('kevin', 'chan', age=27)
    print(musician)


# 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello," + name.title()
        print(msg)


if __name__ == '__main__':
    usernames = ['kevin', 'lily', 'tom']
    greet_users(usernames)
