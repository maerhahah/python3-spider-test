import importlib
import sys
import time

importlib.reload(sys)
time1 = time.time()
print("初始时间为：", time1)

text_path = r'file/phone_list.pdf'

import tabula


def parse(pdf_file):
    path = pdf_file

    df = tabula.read_pdf(path, encoding='gbk', pages='all')
    for indexs in df.index:
        print(df.loc[indexs].values)

    tabula.convert_into(path, path + '.csv', pages='all')
    tabula.convert_into(path, path + '.ods', pages='all')


if __name__ == '__main__':
    parse(text_path)
    time2 = time.time()
    print("总共消耗时间为:", time2 - time1)
