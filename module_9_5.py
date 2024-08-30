class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен нулю')
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self

    """Здесь я не совсем верно, скорее всего, выполнил 2 условия - я дописал +1 и -1 к атрибуту stop, 
    но без них не хочет наша переменная i в цикле for выводить последний элемент из result"""

    def __next__(self):
        result = self.pointer
        self.pointer += self.step
        if self.step > 0 and self.pointer > self.stop + 1 or self.step < 0 and self.pointer < self.stop - 1:
            raise StopIteration
        return result


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
