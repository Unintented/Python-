# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """模拟打印每个模型，打印后将其移到另一列表中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """打印出已完成的模型"""
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_models = ['iphone', 'sumsung', 'nokia']
completed_models = []
print_models(unprinted_models, completed_models)
show_completed_models(completed_models)
# 若想保证原来的数组不发生变化，可以将数组的切片当做实参：unprinted_models[:]
