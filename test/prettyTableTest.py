from prettytable import PrettyTable

# 最简单的

headers = ["姓名", "年龄", "身高", "体重"]

table = PrettyTable(["姓名", "年龄", "身高", "体重"])
table.add_row(["Tom1", 26, "178cm", "80kg"])
table.add_row(["Tom2", 27, "178cm", "80kg"])
table.add_row(["Tom3", 28, "178cm", "80kg"])
table.add_row(["Tom4", 29, "178cm", "80kg"])
print(table)


def color1(text):
    prefix = "\033[1;31;40m"
    suffix = "\033[0m"
    return "".join([prefix, text, suffix])


def color2(text):
    color_tmp = "\033[1;33m{value}\033[0m"
    return color_tmp.format(value=text)


# 加样式

table2 = PrettyTable()
table2.field_names = headers
table2.add_row([color1("Tom1"), color1("26"), color1("178cm"), color1("80kg")])
table2.add_row([color2("Tom2"), color2("27"), color2("178cm"), color2("80kg")])

print(table2)
