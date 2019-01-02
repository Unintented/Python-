promt = "Please enter keyword, end with 'quit'."
message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)
# 一般多个结束条件，可设置标志判断循环是否结束（flag）
# 也有break(结束当前循环),continue（直接进行下次循环）
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)
# 使用用户输入填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("Please enter your name:")
    response = input("Which mountain would you like to clime someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\nPolling results:")
for name, response in responses.items():
    print(name + " would like to climb " + response)
