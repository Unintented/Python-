# 导入整个模块，调用函数要加模块名
import function_4
# 导入部分函数，直接使用函数名
from function_2 import greet_users

# 若导入的文件中有直接的函数调用语句，加载到内存会直接执行，无if __name__ == '__main__':
function_4.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

usernames = ['kevin', 'lily', 'tom']
greet_users(usernames)
