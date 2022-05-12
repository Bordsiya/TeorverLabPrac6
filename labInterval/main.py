
from IOMethods import read_data
from Selection import Selection

selection = read_data()
print("X^ = ", selection.get_mean())
if isinstance(selection, Selection):
    print("S^2 = ", selection.get_unbiased_dispersion())
    print("S = ", selection.get_unbiased_standart_deviation())
else:
    print("D = ", selection.get_dispersion())
    print("q = ", selection.get_standart_deviation())

interval = selection.get_mean_interval()
print("Доверительный интервал для X^ = (", interval.left, ";", interval.right, ")")

