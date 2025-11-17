"""Категоризация расходов по уровням

Представьте, что вы ведете учет своих ежедневных расходов в течение недели. У вас есть список расходов за каждый день.
Вы хотите категоризировать каждый день по уровню затрат:
- низкий уровень затрат: менее 100 рублей;
- средний уровень затрат: от 100 до 300 рублей;
- высокий уровень затрат: более 300 рублей;

Распечатать список категорий трат по дням недели.
"""


def get_expense_category(expense: float) -> str:
    """
    1. Валидация
    2. Категорирование
    :param expense:
    :return:
    """
    if isinstance(expense, (int, float)):
        if expense >= 0:
            if expense < 100:
                return "низкий уровень"
            elif 100 <= expense < 300:
                return "средний уровень"
            else:
                return "высокий уровень"
        else:
            raise ValueError("Трата не должна быть отрицательной")
    else:
        raise TypeError("Трата должна быть целым числом")


def get_expense_categories(expenses: list[float]) -> list[str]:
    """Формирование итогового результата.

    :param expenses: Набор трат
    :return: Категории трат
    """
    return [get_expense_category(expense) for expense in expenses]


if __name__ == "__main__":
    expenses = [50, 200, 400, 150, 80, 350, 100]
    print(get_expense_categories(expenses))
