"""Категоризация расходов по уровням

Представьте, что вы ведете учет своих ежедневных расходов в течение недели. У вас есть список расходов за каждый день.
Вы хотите категоризировать каждый день по уровню затрат:
- низкий уровень затрат: менее 100 рублей;
- средний уровень затрат: от 100 до 300 рублей;
- высокий уровень затрат: более 300 рублей;

Распечатать список категорий трат по дням недели.
"""


def get_expense_categories(expenses: list[float]) -> list[str]:
    categories = []
    for expense in expenses:
        if isinstance(expense, (int, float)):
            if expense >= 0:
                if expense < 100:
                    categories.append("низкий уровень")
                elif 100 <= expense < 300:
                    categories.append("средний уровень")
                else:
                    categories.append("высокий уровень")
            else:
                raise ValueError("Трата не должна быть отрицательной")
        else:
            raise TypeError("Трата должна быть целым числом")

    return categories


if __name__ == "__main__":
    expenses = [50, 200, 400, 150, 80, 350, 100]
    print(get_expense_categories(expenses))
