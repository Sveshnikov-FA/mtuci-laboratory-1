from L3 import CashCalculator, Record


def test_day_calc():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="123"))
    result = cash_calculator.get_today_cash_remained('RUB')
    assert result == 710.0
