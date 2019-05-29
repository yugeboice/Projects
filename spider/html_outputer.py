## -*- coding: utf-8 -*-
import csv
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def output_html(self,list):
        if list is None:
           return
        self.datas = list
        count = 1;
        print('RESULT:')
        #print data directly to debug
#         for data in self.datas:
#             if data == None:
#                 continue
#             else:
#                 print(count)
# #                 print(data['url'])
#                 print(data['state'])
#                 print(data['city'])
#                 print(data['link'])
#                 print(data['address'])
#                 count += 1
            ####write data into csv file
        try:
            with open('result.csv', 'w', newline = '') as csvfile:
                
                headers = ["state","city","link","address","postal","phone"]
                #user dict writer to write into csv file
                csv_writer = csv.DictWriter(csvfile, headers)
                csv_writer.writeheader()
                
                for item in self.datas:
                  csv_writer.writerow(item)
          
            print('success!')
        except Exception as error:
            print('output failed:',format(error))
