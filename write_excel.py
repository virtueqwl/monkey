#!usr/bin/env python
#-*-coding:utf-8-*-

import xlwt

def write_excel(contents):
	workbook = xlwt.Workbook(encoding="utf-8")
	sheet = workbook.add_sheet("logresult", cell_overwrite_ok=True)
	style = xlwt.easyxf(
	"align: wrap off,vert centre, horiz centre;"
	"font: bold on;"  #字体
	"borders: left medium,right medium,top medium,bottom medium;"
	"pattern: pattern solid, fore_colour gray40;"
	)
	style1 = xlwt.easyxf(
	"align: wrap off, vert centre, horiz left;"
	"borders: left medium,right medium,top medium,bottom medium;"
	)
	style2 = xlwt.easyxf(
	"align: wrap off, vert centre, horiz centre;"
	"borders: left medium,right medium,top medium,bottom medium;"
	)
	title_rows = ["SN(pakeage)","issues","counts"]
	for i,t in enumerate(title_rows):
		sheet.write(0, i, t, style)
	for ix,x in enumerate(contents,start=1):
		for i,t in enumerate(x):
			new_style = style2
			if i == 1:
				new_style = style1
			sheet.write(ix, i, t, new_style)
	first_col=sheet.col(0)
	sec_col=sheet.col(1)
	thri_col=sheet.col(2)
	first_col.width=256*15
	sec_col.width=256*50
	thri_col.width=256*10
	workbook.save("logresult.xls")

if __name__ == '__main__':
	write_excel()
