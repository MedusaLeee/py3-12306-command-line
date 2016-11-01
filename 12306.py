#! /usr/bin/env python3

"""12306 tickets query via command-line.

Usage:
    12306.py <from> <to> <date>

Options:
    -h,--help   显示帮助菜单

Example:
    12306.py 泰安 北京 2016-10-25
"""
from docopt import docopt
from Tickets import Tickets
import requests
import re

requests.packages.urllib3.disable_warnings()


def cli():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8970"
    r = requests.get(url, verify=False)
    stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
    station = dict(stations)

    arg = docopt(__doc__)
    from_station = station.get(arg['<from>'])
    to_station = station.get(arg['<to>'])
    date = arg['<date>']
    url = "https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date={}" \
          "&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT"
    url = url.format(
        date, from_station, to_station
    )
    r = requests.get(url, verify=False)
    rows = r.json()['data']
    tickets = Tickets(rows)
    tickets.pretty_print()


if __name__ == '__main__':
    cli()
