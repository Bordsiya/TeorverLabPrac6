from Selection import Selection, get_selection, SelectionInfo


def read_data():
    ans = input("Хотите ввести выборку (a) или только информацию о ней? (b): ")
    if ans == 'a':
        return read_selection()
    elif ans == 'b':
        return read_info_selection()
    else:
        print("Ошибка: введены неверные данные - ", ans)
        exit(1)


def read_info_selection() -> SelectionInfo:
    n = input("Введите количество элементов в выборке: ")
    try:
        n = int(n)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)

    sum_x = input("Введите сумму элементов выборки: ").strip().replace(',', '.')
    try:
        sum_x = float(sum_x)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)

    sum_x2 = input("Введите сумму квадратов элементов выборки: ").strip().replace(',', '.')
    try:
        sum_x2 = float(sum_x2)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)

    reliability = input("Введите надежность для построения доверительного интервала: ").strip().replace(',', '.')
    try:
        reliability = float(reliability)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)

    return SelectionInfo(n, sum_x, sum_x2, reliability)


def read_selection() -> Selection:
    n = input("Введите количество элементов в выборке: ")
    try:
        n = int(n)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)

    print("Введите элементы выборки построчно: ")
    selection = []
    try:
        for i in range(n):
            elem = float(input().strip().replace(',', '.'))
            selection.append(elem)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)

    reliability = input("Введите надежность для построения доверительного интервала: ").strip().replace(',', '.')
    try:
        reliability = float(reliability)
    except ValueError:
        print("Ошибка: введены данные неверного типа")
        exit(1)
    return get_selection(selection, reliability)





