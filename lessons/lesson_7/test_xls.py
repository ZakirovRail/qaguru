import xlrd

book = xlrd.open_workbook("file_example_XLS_10.xls")

print(f'Количество листов {book.nsheets}')
print(f'Имена листов {book.sheet_names()}')
sheet = book.sheet_by_index(0)
print(f'Количество столбцов {sheet.ncols}')
print(f'Количество строк {sheet.nrows}')
print(sheet.cell_value(rowx=0, colx=1))
for rx in range(sheet.nrows):
    print(sheet.row(rx))

