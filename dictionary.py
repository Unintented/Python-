# 字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 修改键值对
alien_0['color'] = 'yellow'
print(alien_0['color'])

alien_0['speed'] = 'medium'
print("Original x-position:" + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 0
elif alien_0['speed'] == 'medium':
    x_increment = 1
else:
    x_increment = 2
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))

# 删除键值对(永久删除)
del alien_0['points']
print(alien_0)


