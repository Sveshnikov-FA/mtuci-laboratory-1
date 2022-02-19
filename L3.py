import datetime


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        total = 0
        for item in self.records:
            if str(datetime.date.today()) == item.date:
                total += item.amount
            else:
                break

        return total

    def get_week_stats(self):
        total = 0

        for wd in range(0,7):
            for item in self.records:
                if str((datetime.date.today() - datetime.timedelta(days=wd)).date()) == item.date:
                    total += item.amount
                else:
                    break
        return total


class CaloriesCalculator(Calculator):

    def __init__(self):
        super().__init__()

    def get_calories_remained(self):
        received = self.get_today_stats()
        if received > self.limit:
            print("Above limit")
        else:
            print("Below limit")


class CashCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        curr_mapping = {
            'EUR': 80,
            'USD': 70,
            'RUB': 1
        }
        remaining = limit = self.get_today_stats()
        if(remaining<0):
            return 0
        return remaining/curr_mapping[currency]


class Record:
    def __init__(self, amount=0, date=str(datetime.date.today()), comment=""):
        self.amount = amount
        self.date = date
        self.comment = comment


if __name__ == "__main__":
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="123"))
    cash_calculator.add_record(Record(amount=145, comment="123"))
    cash_calculator.add_record(Record(amount=145, comment="2022-01-18"))
    print(cash_calculator.get_today_cash_remained('RUB'))
