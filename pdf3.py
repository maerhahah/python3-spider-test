import pdfplumber

path = r'file/phone_list.pdf'
# path = r'file/4.pdf'
pdf = pdfplumber.open(path)

for page in pdf.pages:
    # 获取当前页面的全部文本信息，包括表格中的文字
    # print(page.extract_text())

    for table in page.extract_tables():
        for row in table:
            print(row)
        print('---------- 分割线 ----------')

pdf.close()