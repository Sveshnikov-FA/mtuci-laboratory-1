from L3 import CaloriesCalculator, CashCalculator, Record


def test_day_calc():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="123"))
    result = cash_calculator.get_today_cash_remained('RUB')
    assert result == 710.0


def test_week_calc():
    cal_calculator = CaloriesCalculator(1000)
    cal_calculator.add_record(Record(amount=145, comment="123"))
    cal_calculator.add_record(Record(amount=150, comment="123"))
    cal_calculator.add_record(Record(amount=145, date="2022-02-18"))
    cal_calculator.add_record(Record(amount=999, date="2022-01-15"))
    assert cal_calculator.get_week_stats() == 440

