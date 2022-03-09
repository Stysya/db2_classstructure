import os
import xlsxwriter
import ibm_db_dbi as db
from dotenv import load_dotenv
load_dotenv()
db_name = os.getenv("DATABASE")
hostname = os.getenv("HOSTNAME")
port = os.getenv("PORT")
username = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
# print(db_name, hostname, port, username, password)
connection = db.connect(f'DATABASE={db_name};'
                        f'HOSTNAME={hostname};'
                        f'PORT={port};'
                        'PROTOCOL=TCPIP;'
                        f'UID={username};'
                        f'PWD={password};', '', '')

curs = connection.cursor()
query = "SELECT * FROM CLASSSTRUCTURE"
curs.execute(query)
# print([i[0] for i in curs.description])
# PARENT index = 4
# CLASSSTRUCTUREID index = 0
rs = curs.fetchall()
curs.close()
connection.close()

report_dict = {}
for item in rs:
    curr_item = item
    if curr_item[0] == curr_item[4] or not curr_item[4]:
        report_dict[item[0]] = item[4] if item[4] else item[0]
        continue
    lst = []
    while True:
        lst.append(curr_item[0])
        if curr_item[0] == curr_item[4] or curr_item[4] is None:
            break
        for i in rs:
            if curr_item[4] == i[0]:
                curr_item = i
                break
    report_dict[item[0]] = ' / '.join(lst[::-1])

workbook = xlsxwriter.Workbook('classification.xls')
worksheet = workbook.add_worksheet()
counter = 0
for row_num, k_v in enumerate(report_dict.items()):
    for col_num, col_data in enumerate(k_v):
        worksheet.write(row_num, col_num, col_data)

workbook.close()
