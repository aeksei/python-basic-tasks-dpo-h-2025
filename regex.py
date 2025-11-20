import re
from datetime import datetime


def is_valid_date(date_str, format_) -> bool:
    try:
        datetime.strptime(date_str, format_)
    except ValueError:
        return False

    return True


regex = r"\d\d\d\d-\d\d\-\d\d"

test_str = "Сегодня: 2025-11-20\nНовый год: 2025-12-31\nЗлая шутка: 2025-02-30\n"

for text_date in re.findall(regex, test_str, re.M):
    if is_valid_date(text_date, "%Y-%m-%d"):
        print(text_date, "Корректная дата")
    else:
        print(text_date, "Некорректная дата")


# matches = re.finditer(regex, test_str, re.MULTILINE)
#
# for matchNum, match in enumerate(matches, start=1):
#
#     print("Соответствие {matchNum} было найдено в {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
#                                                                                  end=match.end(), match=match.group()))
#
#     for groupNum, _ in enumerate(match.groups(), start=1):
#
#         print(
#             "Группа {groupNum} найдена в {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
#                                                                         end=match.end(groupNum),
#                                                                         group=match.group(groupNum)))
