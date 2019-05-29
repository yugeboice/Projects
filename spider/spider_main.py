## -*- coding: utf-8 -*-
# from spider import url_manager, html_downloader, html_parser, html_outputer


import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    
    def __init__(self):
        #Initial the module I will use in whole project: downloader, parser, outputer
        self.download = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
       

    def craw(self, root_url): 
       
        try:
          
            new_url = root_url
            print('craw from root : %s' % (new_url)) 
            # download html data from the root url
            
            html_cont = self.download.download(new_url)
            # filter html elements to the data I need
            list = self.parser.state_parser(new_url, html_cont)
            
            # output as csv file
            self.outputer.output_html(list)
            print('after outputer.collect in main')

#                 
        except Exception as error:
            print('crew failed:',format(error))

        

if __name__ == "__main__":
    #root_url = 'http://ent.sina.com.cn/y/yrihan/2019-05-26/doc-ihvhiews4697613.shtml'
    root_url = 'https://www.apple.com/retail/storelist/'
   # root_url = 'https://zh.wikipedia.org/wiki/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) # start
