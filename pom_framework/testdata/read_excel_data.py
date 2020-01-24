import xlrd
def get_data():
    wb=xlrd.open_workbook(r"C:\Users\naveen.s\PycharmProjects\pytest-tutorial\pom_framework\testdata\PayeeDetails.xlsx")
    sheet=wb.sheet_by_name("PayeeDetails")
    datali=[]
    for i in range(1,sheet.nrows):
        data=[]
        for j in range(0,sheet.ncols):
            data.append(sheet.cell_value(i,j))
        datali.append(data)
    return datali

