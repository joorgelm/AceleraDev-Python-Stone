from datetime import datetime

DAY_START = 6
NIGHT_START = 22
FIXED_COST = 0.36
COST_PER_MINUTE = 0.09

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def classify_by_phone_number(calls_report: list) -> list:
    
    print('TEEEESTANDO')

    classification_report = {}

    for call in calls_report:

        if is_day(call['start']) and is_day(call['end']):
            call_duration = get_call_minutes(start=call['start'], end=call['end'])
            call_cost = get_call_cost(duration=call_duration)

            add_cost_to_final_report(classification_report, call['source'], call_cost)

        elif not is_day(call['start']) and not is_day(call['end']):
            add_cost_to_final_report(classification_report, call['source'], FIXED_COST)
        else:

            six_hours, twenty_two_hours = get_edges_of_day(call['start'])

            if is_day(call['start']):
                call_duration = get_call_minutes(start=call['start'], end=twenty_two_hours)
                call_cost = get_call_cost(call_duration)

            else:
                call_duration = get_call_minutes(start=six_hours, end=call['end'])
                call_cost = get_call_cost(call_duration)

            add_cost_to_final_report(classification_report, call['source'], call_cost)

    return format_report(classification_report)


def format_report(report: dict) -> list:

    final_report = []

    for item in sorted(report, key=report.get, reverse=True):

        cost = "{:.2f}".format(report[item])
        final_report.append({'source': item, 'total': float(cost)})

    return final_report


def add_cost_to_final_report(report: dict, source: str, cost: float) -> None:
    if source in report:
        report[source] = report[source] + cost
    else:
        report[source] = cost


def get_call_cost(duration: int, night=False) -> float:
    if night:
        return FIXED_COST

    call_cost = duration * COST_PER_MINUTE + FIXED_COST
    return call_cost


def is_day(timestamp: int) -> bool:
    six_hours, twenty_two_hours = get_edges_of_day(timestamp)

    return six_hours <= timestamp < twenty_two_hours


def get_call_minutes(start: int, end: int) -> int:
    call_start = datetime.fromtimestamp(start)
    call_end = datetime.fromtimestamp(end)

    duration = (call_end - call_start).total_seconds()

    return int(duration / 60)


def get_edges_of_day(timestamp: int) -> tuple:
    call_date = datetime.fromtimestamp(timestamp)

    night_call_date = datetime(year=call_date.year, month=call_date.month, day=call_date.day, hour=NIGHT_START)
    day_call_date = datetime(year=call_date.year, month=call_date.month, day=call_date.day, hour=DAY_START)

    night_timestamp = int(datetime.timestamp(night_call_date))
    day_timestamp = int(datetime.timestamp(day_call_date))

    # 6h, 22h
    return day_timestamp, night_timestamp
