per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = int(input("Enter the deposit amount: "))  # вводим сумму 100000
for value in per_cent:  # для каждого значения ставки из словаря:
    deposit.append(round(per_cent[value] * money / 100))  # вычисляем заработок за год в разных банках
print("deposit =", deposit)  # выводим список заработков
print("The maximum amount you can earn: ", max(deposit))  # максимальный заработок

# еще один вариант решения (но сначала определяем максимальную ставку, и с ней считаем):
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = float(input("Enter the deposit amount: "))   # вводим сумму 100000
# deposit_var = list(per_cent.values())    # список годовых процентных ставок
# max_perc = max(deposit_var)   # это максимальная годовая процентная ставка из всех
# deposit = max_perc / 100 * money   # вычисляем прибыль за год
# print("The maximum amount you can earn: ", int(deposit))
