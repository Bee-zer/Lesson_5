import json


def get_statistics():
    try:
        with open('text_7.txt', 'r+', encoding='utf-8') as file:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in file:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('text_77.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()