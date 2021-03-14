

class NokCounter:

    def __init__(self, file_name, result_file_name):
        self.file_name = file_name
        self.result_file_name = result_file_name
        self.NOKS_list = None  # чтобы не проходиться по файлу циклами несколько раз,
        # сохраняем логи NOK в списке списков
        # вида [[log, n], ...], где log - лог, n - количество
        # повторений

    def retrieve_NOKS(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if self._checking_NOK(chr=line[29]):
                    line = line[:17]
                    if self.NOKS_list is None:
                        self.NOKS_list = [[line, 1]]
                    elif self.NOKS_list[-1][0] == line:
                        self.NOKS_list[-1][1] += 1
                    else:
                        self.NOKS_list.append([line, 1])

    def _checking_NOK(self, chr):
        return chr == 'N'

    def create_new_file_with_NOKS(self):
        with open(self.result_file_name, mode='w', encoding='utf8') as file:
            for log in self.NOKS_list:
                line = log[0] + '] {}'.format(log[1])
                file.write(line + '\n')


class NokCounterHour(NokCounter):

    def retrieve_NOKS(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if self._checking_NOK(chr=line[29]):
                    line = line[:14]
                    if self.NOKS_list is None:
                        self.NOKS_list = [[line, 1]]
                    elif self.NOKS_list[-1][0] == line:
                        self.NOKS_list[-1][1] += 1
                    else:
                        self.NOKS_list.append([line, 1])


class NokCounterMonth(NokCounter):

    def retrieve_NOKS(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if self._checking_NOK(chr=line[29]):
                    line = line[:8]
                    if self.NOKS_list is None:
                        self.NOKS_list = [[line, 1]]
                    elif self.NOKS_list[-1][0] == line:
                        self.NOKS_list[-1][1] += 1
                    else:
                        self.NOKS_list.append([line, 1])


class NokCounterYear(NokCounter):

    def retrieve_NOKS(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                if self._checking_NOK(chr=line[29]):
                    line = line[:5]
                    if self.NOKS_list is None:
                        self.NOKS_list = [[line, 1]]
                    elif self.NOKS_list[-1][0] == line:
                        self.NOKS_list[-1][1] += 1
                    else:
                        self.NOKS_list.append([line, 1])


# test = NokCounter('events.txt', 'result.txt')
# test.retrieve_NOKS()
# test.create_new_file_with_NOKS()
# print(test.NOKS_list)





