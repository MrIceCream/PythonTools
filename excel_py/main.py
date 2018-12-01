#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from openpyxl import Workbook
from openpyxl import load_workbook


INVOICE_TEMPLATE_PATH = './template/invoice_template.xlsx'
PROCUREMENT_PATH = './input/procurement.xlsx'


'''
读取采购单
'''
def read_procurement_excel(path):
    result = []

    workbook = load_workbook(path)
    sheet = workbook.active
    rows = sheet.rows
    for row in rows:
        line = [col.value for col in row]
        result.append(line)

    result.pop(0)

    return result


'''
读取发票模板
'''
def read_invoice_template():
    workbook = load_workbook(INVOICE_TEMPLATE_PATH)
    sheet = workbook.active

    temp = sheet.cell(row=3, column=1).value

    print(temp)



'''
导出发票信息
'''
def export_invoice(file):
    excel_date = read_procurement_excel(file)

    cg_dict = {}
    for row in excel_date:
        cg_key = row[0]
        if cg_key in cg_dict:
            cg_dict[cg_key].append(row)
        else:
            cg_dict[cg_key] = [row]


    for cg_key in cg_dict:
        cd_data = cg_dict[cg_key]
        sku_data = deal_cg_data(cd_data)
        write_invoice_file(cg_key, sku_data)
        print(cg_key, len(sku_data))


'''
处理同一cg信息
'''
def deal_cg_data(cg_data):
    sku_dict = {}
    for row in cg_data:
        sku_key = row[1]
        if sku_key in sku_dict:
            sku_dict[sku_key]["count"] += row[3]
            sku_dict[sku_key]["total"] += row[6]
        else:
            sku_dict[sku_key] = {"name":    row[8],
                                 "count":   row[3],
                                 "unit":    row[2],
                                 "price":   row[5],
                                 "total":   row[6],
                                 "sku":     row[1]}
    return sku_dict

'''
导出发票excel
'''
def write_invoice_file(cg_key, cg_data):

    workbook = load_workbook(INVOICE_TEMPLATE_PATH)
    worksheet = workbook.active
    worksheet.title = u'发票'

    worksheet.cell(row=3, column=1, value='Contract No.：'+cg_key)

    row = 8
    for sku_key in cg_data:
        sku_data = cg_data[sku_key]
        worksheet.cell(row=row, column=1).value = sku_data["name"]
        worksheet.cell(row=row, column=2).value = sku_data["count"]
        worksheet.cell(row=row, column=3).value = sku_data["unit"]
        worksheet.cell(row=row, column=4).value = sku_data["price"]
        worksheet.cell(row=row, column=5).value = sku_data["total"]
        worksheet.cell(row=row, column=6).value = sku_data["sku"]
        row += 1

    workbook.save('./output/invoice/'+cg_key+'.xlsx')


def test():
    read_invoice_template()


if __name__ == '__main__':

    test()

    # export_invoice(PROCUREMENT_PATH)

    # type = raw_input('1.导出发票\n2.test\n')
    #
    # if type == "1":
    #     export_invoice(PROCUREMENT_PATH)
    # elif type == "2":
    #     test()
