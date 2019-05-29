## -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.parse
import html_downloader

class HtmlParser(object):
    def __init__(self):
        self.download = html_downloader.HtmlDownloader()
        self.list = []
   # the main parser process
    def _get_new_data(self, page_url, soup):
        print('inside get new data in parser')
        #filter all the stores
        nodes = soup.find_all('div', class_="toggle-section")
        flag = 1
        for area_node in nodes:
            res_data = {}
            if area_node == None:
                res_data['state'] = ''
                res_data['city'] = ''
                self.list.append(res_data)
                return self.list
            else:
                state_node = area_node.find('h3', class_="toggle")
                res_data['state'] = state_node.get_text()
    
                city_node = area_node.find('ul').find('li')
                if city_node == None:
                    res_data['city'] = ''
                    self.list.append(res_data)
                    return self.list
                    
                else:
                    res_data['city'] = city_node.get_text()
                    #parser city link information to scrape details
                    link = city_node.find('a', href=re.compile(r'/retail/'))
                    new_url = link['href']
                    # joint new_url like page_url 
                    link_full_url = urllib.parse.urljoin(page_url, new_url)
                    res_data['link'] = link_full_url
                    #Start to scraw detail based on city link
                    html_content = self.download.download(res_data['link'])
                    full_data = self.detail_parser(new_url, html_content,res_data)
                    #save 1 city-state data in list
                    self.list.append(full_data)
        
#             if flag == 10:
#                 break
#             flag+=1            
        return self.list
    
    def _get_detail(self, page_url, soup, data):
        print('inside getdetail in parser')
        #<div class="column large-12 medium-5 small-12">
        address_node = soup.find('div', class_="column large-12 medium-5 small-12")
    
        if address_node == None:
            data['address'] = ''
            
            return data
        else:
            #check whether this page contains detailed street, local, region, postal,phone info
            street_node = address_node.find('span', class_ = 'store-street typography-body')
            local_node = address_node.find('span', class_ = 'store-locality typography-body')
            region_node = address_node.find('span', class_ = 'store-region typography-body')
            if street_node == None:
                street = ''
            else:
                street = street_node.get_text()
                
            if local_node == None:
                local = ''
            else:
                local = local_node.get_text()
                
            if region_node == None:
                region = ''
            else:
                region = region_node.get_text()
               
            postal_node = address_node.find('span', class_ = 'store-postal-code typography-body')
            if postal_node == None:
                postal = ''
            else:
                postal = postal_node.get_text()
                
            phone_node = address_node.find('span', class_ = 'store-phone typography-body')
            if phone_node == None:
                phone = ''
            else:
                phone = phone_node.get_text()
            #joint and save data in dict
            data['address'] = street + local + region
            data['postal'] = postal
            data['phone'] = phone
            
        return data

    def state_parser(self, page_url, html_cont):
        print('inside state_parser')
        if page_url is None or html_cont is None:
            return
        #new beautifulsoup object to search data in html
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
       
        list_item = self._get_new_data(page_url, soup)
        
        return list_item
    
    def detail_parser(self, page_url, html_cont,data):
        print('inside detail_parser')
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
      
        alist = self._get_detail(page_url, soup, data)
        return alist

