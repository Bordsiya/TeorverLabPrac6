from collections import defaultdict
from dataclasses import dataclass
import scipy
from scipy import stats
from scipy.stats import norm
from Interval import Interval


@dataclass
class Selection:
    n: int
    x_arr: []
    n_arr: list[int]
    reliability: float

    def get_mean(self) -> float:
        mean = 0
        for i in range(len(self.x_arr)):
            mean += self.x_arr[i] * self.n_arr[i]
        return round(mean / self.n, 3)

    def get_dispersion(self) -> float:
        sum = 0
        x_mean = self.get_mean()
        for i in range(len(self.x_arr)):
            sum += (self.x_arr[i] - x_mean) ** 2 * self.n_arr[i]
        return round(sum / self.n, 3)

    def get_unbiased_dispersion(self) -> float:
        return round(self.get_dispersion() * self.n / (self.n - 1), 3)

    def get_standart_deviation(self) -> float:
        return round(self.get_dispersion() ** 0.5, 3)

    def get_unbiased_standart_deviation(self) -> float:
        return round(self.get_unbiased_dispersion() ** 0.5, 3)

    def get_mean_interval(self) -> Interval:
        if self.n > 30:
            quantile = round(norm.ppf((1 + self.reliability) / 2), 4)
        else:
            quantile = round(scipy.stats.t.ppf((1 + self.reliability) / 2, self.n - 1), 4)
        print("Квантиль стьюдента = ", quantile)
        x_mean = self.get_mean()
        s = self.get_unbiased_standart_deviation()
        left = round(x_mean - ((quantile * s) / (self.n ** 0.5)), 3)
        right = round(x_mean + ((quantile * s) / (self.n ** 0.5)), 3)
        return Interval(left, right)


@dataclass
class SelectionInfo:
    n: int
    sum_x: float
    sum_x2: float
    reliability: float

    def get_mean(self) -> float:
        return round(self.sum_x / self.n, 3)

    def get_dispersion(self) -> float:
        return round((self.sum_x2 / self.n) - self.get_mean()**2, 3)

    def get_standart_deviation(self) -> float:
        return round(self.get_dispersion() ** 0.5, 3)

    def get_mean_interval(self) -> Interval:
        if self.n > 30:
            quantile = round(norm.ppf((1 + self.reliability) / 2), 4)
        else:
            quantile = round(scipy.stats.t.ppf((1 + self.reliability) / 2, self.n - 1), 4)
        print("Квантиль стьюдента = ", quantile)
        x_mean = self.get_mean()
        s = self.get_standart_deviation()
        left = round(x_mean - ((quantile * s) / (self.n ** 0.5)), 3)
        right = round(x_mean + ((quantile * s) / (self.n ** 0.5)), 3)
        return Interval(left, right)


def get_selection(arr: list[float], reliability: float) -> Selection:
    m = defaultdict(int)
    for i in range(len(arr)):
        m[arr[i]] += 1
    m = sorted(m.items())
    x_arr = []
    [x_arr.append(i[0]) for i in m]
    n_arr = []
    [n_arr.append(i[1]) for i in m]
    return Selection(len(arr), x_arr, n_arr, reliability)
