print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям. 
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, 
# чтобы понять динамику роста или падения дохода. И так за каждый год. 
# 
# Надя решила, 
# что быстрее будет написать простую программу, которая сделает всё за неё.
# 
# 
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.
first = int(input('Введите доход за первый квартал: '))
second = int(input('Введите доход за второй квартал: '))
third = int(input('Введите доход за третий квартал: '))
fourth= int(input('Введите доход за четвертый квартал: '))

summ_first = first + second
summ_last =  third + fourth

print('Результат =', summ_first / summ_last)