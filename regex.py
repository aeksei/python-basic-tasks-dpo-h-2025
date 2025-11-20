import re
from datetime import datetime, timedelta

INPUT_DATE_FORMAT = "%Y-%m-%d"
OUTPUT_DATE_FORMAT = "%y/%m/%d"


def is_valid_date(date_str, format_) -> bool:
    try:
        datetime.strptime(date_str, format_)
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    regex = r"\d\d\d\d-\d\d\-\d\d"

    with open("src_file.txt") as f:
        for test_str in f:
            for text_date in re.findall(regex, test_str):
                if is_valid_date(text_date, INPUT_DATE_FORMAT):
                    next_day = datetime.strptime(
                        text_date, INPUT_DATE_FORMAT
                    ) + timedelta(days=1)
                    print(
                        text_date,
                        "Корректная дата. Следующий день -",
                        next_day.strftime(OUTPUT_DATE_FORMAT),
                    )
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
