per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Вводите сумму, которую желаете положить под проценты:"))

ТКБ = int((per_cent['ТКБ']) * (money/100))
СКБ = int((per_cent['СКБ']) * (money/100))
ВТБ = int((per_cent['ВТБ']) * (money/100))
СБЕР = int((per_cent['СБЕР']) * (money/100))

deposit = [ТКБ, СКБ, ВТБ, СБЕР]
print("Накопленные средства за год в каждом из банков =", deposit)
#Добавьте в программу поиск максимального значения и его вывод на экран
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
print(per_cent)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
