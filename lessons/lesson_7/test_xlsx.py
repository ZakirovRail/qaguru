from openpyxl import load_workbook

workbook = load_workbook("file_example_XLSX_10.xlsx")
sheet = workbook.active
print(sheet.cell(row=3, column=2).value)
