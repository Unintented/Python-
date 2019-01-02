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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 可通过实例直接访问属性并进行更改
print(my_new_car.odometer)
my_new_car.read_odometer()
# 可通过类中方法修改属性
my_new_car.update_odometer(500)
my_new_car.read_odometer()
