import datetime
import requests
import logging


class Calculator:
    """
        Калькулятор для подсчёта записей.
        :parameter
        limit: Целое число, лимит по операциям
        records: Массив целых чисел с операциями
    """
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """
            Добавляет операцию в массив
            :parameter
            records: объект класса Record
        """
        self.records.append(record)

    def get_today_stats(self):
        """
            Подсчёт операций за сегодняшний день
            :return:
            total: Целое число, сумма всех операций
        """
        total = 0
        for item in self.records:
            if datetime.date.today() == item.date:
                total += item.amount
            else:
                break

        return total

    def get_week_stats(self):
        """
            Подсчёт операций за предыдущие 7 дней
            :return:
            total: Целое число, сумма всех операций
        """
        total = 0
        for wd in range(7):
            for item in self.records:
                if datetime.date.today() - datetime.timedelta(days=wd) == item.date:
                    total += item.amount
                else:
                    break
        return total


class CaloriesCalculator(Calculator):
    """
        Калькулятор для подсчёта калорий. Наследует методы и параметры класса Calculator
    """
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        """
            Определяет, превышен ли лимит калорий на сегодня
        """
        received = self.get_today_stats()
        if received < self.limit:
            logging.warning(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - received} кКал")
        else:
            logging.info("Хватит есть!")


class CashCalculator(Calculator):
    """
        Калькулятор для подсчёта денег. Наследует методы и параметры класса Calculator
    """
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        """
            Определяет, сколько денег осталось на счету за сегодня по указанному курсу
            :parameter
            currency: строка, обозначающая тип валюты
            :return
            result: действительное число, остаток на счету в указанной валюте
        """
        curr_mapping = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=bf6cf289b53ad57e768c3cabc9630636").json()["rates"]
        for i in curr_mapping:
            curr_mapping[i] = round(curr_mapping[i]/curr_mapping["RUB"], 2)
        logging.debug(curr_mapping)
        remaining = self.limit - self.get_today_stats()
        if remaining < 0:
            return 0
        return round(remaining/curr_mapping[currency], 2)


class Record:
    """
        Объект произведённой операции
        :parameter
        amount: целое число, количество задействованных у.е. в операции
        date: datetime.date, дата произведения операции
        comment: строка, комментарий к операции
    """
    def __init__(self, amount=0, date=datetime.date.today(), comment=""):
        self.amount = amount
        self.date = datetime.datetime.strptime("%Y-%m-%d").date() if type(date) is str else date
        self.comment = comment


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="123"))
    logging.info(cash_calculator.get_today_cash_remained('RUB'))
    
    calorie_calculator = CaloriesCalculator(1000)
    calorie_calculator.add_record(Record(amount=145, comment="123"))
    calorie_calculator.add_record(Record(amount=999, comment="123"))
    calorie_calculator.add_record(Record(amount=145, comment="2022-01-18"))
    calorie_calculator.get_calories_remained()


def test_day_calc():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="123"))
    result = cash_calculator.get_today_cash_remained('RUB')
    assert result == 710.0


def test_week_calc():
    cal_calculator = CaloriesCalculator(1000)
    cal_calculator.add_record(Record(amount=145, comment="123"))
    cal_calculator.add_record(Record(amount=150, comment="123"))
    cal_calculator.add_record(Record(amount=145, comment="2022-02-15"))
    assert cal_calculator.get_week_stats() == 440
    
    