#! /usr/bin/env python3
from prettytable import PrettyTable


class TrainCollection(object):
    header = ["车次", "出发\到达站", "出发\到达时间", "历时", "一等座", "二等座", "软卧", "硬卧", "软座", "硬座", "无座"]

    def __init__(self, rows):
        self.rows = rows

    # 获取车次运行时间
    @classmethod
    def _get_duration(cls, row):
        duration = row.get('lishi').replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[3:]
        if duration.startswith('0'):
            return duration[0:]
        return duration

    @classmethod
    def colored(cls, color, text):
        table = {
            'red': '\033[91m',
            'green': '\033[92m',
            # no color
            'nc': '\033[0m'
        }
        cv = table.get(color)
        nc = table.get('nc')
        return ''.join([cv, text, nc])

    @property
    def trains(self):
        for row in self.rows:
            train = [
                # 车次
                row['station_train_code'],

                # 出发、到达站
                '\n'.join([self.colored('green', row['from_station_name']),
                           self.colored('red', row['to_station_name'])]),

                # 出发、到达时间
                '\n'.join([self.colored('green', row['start_time']),
                           self.colored('red', row['arrive_time'])]),

                # 历时
                self._get_duration(row),

                # 一等坐
                row['zy_num'],

                # 二等坐
                row['ze_num'],

                # 软卧
                row['rw_num'],

                # 硬卧
                row['yw_num'],

                # 软坐
                row['yw_num'],

                # 硬坐
                row['yz_num'],

                # 无座
                row['wz_num']
            ]
            yield train

    def pretty_print(self):
        pt = PrettyTable()
        # 设置每一列的标题
        pt.field_names = self.header
        for train in self.trains:
            pt.add_row(train)
        print(pt)
