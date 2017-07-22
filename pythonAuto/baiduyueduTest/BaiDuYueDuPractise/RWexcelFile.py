import  requests
import  json
import xlrd
import xlwt

#读取excel文件中数据
# data = xlrd.open_workbook('test.xls') # 打开xls文件
# table = data.sheets()[0] # 打开第一张表
# nrows = table.nrows # 获取表的行数
# for i in range(nrows): # 循环逐行打印
#     if i == 0: # 跳过第一行
#         continue
#     print(table.row_values(i)[:13]) # 取前十三列


# 写到excel文件中
# 创建workbook和sheet对象
workbook = xlwt.Workbook() #注意Workbook的开头W要大写;相当于新建一个excel文件
sheet1 = workbook.add_sheet('sheetaa',cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('sheetbb',cell_overwrite_ok=True)
#向sheet页中写入数据
sheet1.write(0,0,'this should overwrite1')
sheet1.write(0,1,'aaaaaaaaaaaa')
sheet2.write(0,0,'this should overwrite2')
sheet2.write(1,2,'bbbbbbbbbbbbb')
workbook.save('D:\\wenjian\\pythonStudy\\pythonAuto\\baiduyueduTest\\BaiDuYueDuPractise\\test2.xls')
print('创建excel文件完成！')

#读取文件xlrd
book=xlrd.open_workbook('D:\\wenjian\\pythonStudy\\pythonAuto\\baiduyueduTest\\BaiDuYueDuPractise\\test2.xls')
# 得到sheet对象
sheet0 = book.sheet_by_index(0)     # 通过sheet索引获得sheet对象
sheet_name = book.sheet_names()[0]  # 获得指定索引的sheet名字
print(sheet_name)     #输出sheet
sheet1 = book.sheet_by_name(sheet_name)     # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
sheet1_name=book.sheet_names()[1]
print(sheet1_name)
# # 获得行数和列数
# nrows = sheet0.nrows    # 行总数
# ncols = sheet0.ncols    # 列总数
# # 获得指定行、列的值，返回对象为一个值列表
# row_data = sheet0.row_values(0)     # 获得第1行的数据列表
# print(row_data)
# col_data = sheet0.col_values(0)     # 获得第1列的数据列表
# # 通过坐标读取表格中的数据
# cell_value1 = sheet0.cell_value(0, 0)
# print(cell_value1)
# cell_value2 = sheet0.cell_value(0, 1)
# print(cell_value2)

