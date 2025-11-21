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
