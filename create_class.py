# 形参self必不可少，而且必须位于最前面
class Dog():
    def __init__(self, name, age):
        """初始化属性name和age(出现即定义)"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        # 类内访问属性用self.
        print(self.name.title() + " is sitting now.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " is rolling over.")


# 创建类的实例
my_dog = Dog('jinx', 2)
# 访问类的属性用实例名.
print("My dog's name is " +
      my_dog.name.title() +
      ".")
print("My dog is " +
      str(my_dog.age) +
      " years old.")
# 调用类中方法
my_dog.sit()
my_dog.roll_over()
