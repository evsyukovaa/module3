print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.
min = int(input('Введите число - минуты: '))

print(min / 60, '= часа')
print('Осталось', min % 60, 'минут')
