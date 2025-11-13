"""Подсчет расходов на продукты

Представьте, что вы ведете учет своих расходов на продукты в течение недели.
У вас есть список расходов за каждый день.

Напишите программу, которая подсчитывает сумму расходов за неделю.
Проверьте с помощью `assert` результат
"""
from task_5 import total_expense

expenses = [
    [150, 300, 50, 400, 250, 100, 500],
    [250, 100, 450, 200, 550, 150, 550]
]  # расходы на продукты в течение недели

total_expenses = 0
for week_expenses in expenses:
    total_expenses += sum(week_expenses)

print(total_expenses)
#
# print(sum(expenses, start=[]))
# print(sum(sum(expenses, start=[])))
