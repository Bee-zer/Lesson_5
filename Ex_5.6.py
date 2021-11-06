def count_subjects():
    try:
        # Информатика: 100(л) 50(пр) 20(лаб).
        mydict = {}
        with open("text_6.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')  # name = Информатика, stats = 100(л) 50(пр) 20(лаб).
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f"{mydict}")  # вывод:{'Информатика': 170}
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()