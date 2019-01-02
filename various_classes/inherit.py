class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 给里程表提供默认值，不需实参提供
        self.odometer = 0

    def get_descriptive_name(self):
        """获得车完整信息的方法"""
        descriptive_name = str(self.year) + " " + self.make + " " + self.model
        return descriptive_name

    def read_odometer(self):
        """读取里程表的方法"""
        print("This car has " +
              str(self.odometer) +
              " miles on it.")

    def update_odometer(self, mileage):
        """更新里程表的方法，禁止回调里程表"""
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")


# 创建子类时，父类必须包含在当前文件中且位于子类之前
# 定义子类时，必须在括号内指定父类的名称
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        #  super()是一个特殊函数，调用父类的__init__()，让实例包含父类的所有属性
        super().__init__(make, model, year)
        # 定义子类的属性
        self.battery_size = 70

    def describe_battery(self):
        # 子类特有方法
        print("This car has a " +
              str(self.battery_size) +
              "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
