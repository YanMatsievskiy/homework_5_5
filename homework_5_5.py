'''Задача 5. Два водителя'''

driver_1 = input('Введите названия городов маршрута первого водителя: ')
driver_2 = input('Введите названия городов маршрута второго водителя: ')

driver_1 = driver_1.split()
driver_2 = driver_2.split()

intersection = set(driver_1) & set(driver_2)

intersection_lexic = sorted(intersection)
print('Cписок городов, в которых водители потенциально могли бы встретиться '
      '\nв лексикографическом порядке:')
print(intersection_lexic)
