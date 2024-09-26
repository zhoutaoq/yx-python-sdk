import time
from datetime import datetime
from enum import StrEnum


class FormatType(StrEnum):
    FORMAT_FULL = "%Y-%m-%d %H:%M:%S"  # 完整的日期和时间
    FORMAT_FULL_CN = "%Y年%m月%d日 %H时%M分%S秒"  # 完整的日期和时间
    FORMAT_DATE = "%Y年%m月%d日"  # 只有日期
    FORMAT_TIME = "%H时%M分%S秒"  # 只有时间
    FORMAT_ISO = "%Y-%m-%d"  # 年-月-日（ISO 8601格式）
    FORMAT_US = "%m/%d/%Y"  # 月/日/年（美国常用格式）
    FORMAT_CHINESE = "%m月%d日%Y年"  # 月日年（中文常用格式）
    FORMAT_TIME_12H = "%I:%M:%S %p"  # 12小时制的时间（包括AM/PM）
    FORMAT_ISO8601 = "%Y-%m-%dT%H:%M:%S"  # 完整的日期和时间（ISO 8601格式）
    FORMAT_WITH_TZ = "%Y-%m-%d %H:%M:%S%z"  # 完整的日期和时间（带时区信息）
    FORMAT_YEAR = "%Y年"  # 只有年
    FORMAT_MONTH = "%m月"  # 只有月
    FORMAT_DAY = "%d日"  # 只有日
    FORMAT_HOUR = "%H时"  # 只有小时
    FORMAT_MINUTE = "%M分"  # 只有分钟
    FORMAT_SECOND = "%S秒"  # 只有秒


def get_formatted_date(input=None, format: FormatType = FormatType.FORMAT_FULL) -> str:
    if input is None:
        input = datetime.now()
    real_type = type(input)
    if real_type == int:
        date = datetime.fromtimestamp(input)
    elif real_type == datetime:
        date = input
    else:
        raise ValueError(f"only support datetime or int input, got {real_type}")
    return date.strftime(format)


if __name__ == '__main__':
    input = int(time.time())
    print(f"input is {input}")
    print(get_formatted_date(input=input, format=FormatType.FORMAT_FULL))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_FULL_CN))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_DATE))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_TIME))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_ISO))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_US))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_CHINESE))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_TIME_12H))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_ISO8601))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_WITH_TZ))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_YEAR))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_MONTH))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_DAY))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_HOUR))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_MINUTE))
    print(get_formatted_date(input=input, format=FormatType.FORMAT_SECOND))
