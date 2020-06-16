'''
ให้เขียนโปรแกรมดึงข้อมูลจำกเว็บ https://www.nice.org.uk/guidance/ng155/history โดยดึงข้อมูล Documents ตำมรูป
ด้ำนล่ำง


เครื่องมือที่ให้ใช้
1. Requests
2. beautifulsoup4
โดยข้อมูลที่ดึงได้ ให้อยู่ในรูปแบบ json และเขยนขอมลทงหมดลงไฟล.json

ข้อมูลที่ต้องกำรตำมภำพด้ำนล่ำง

โดยตัวอย่ำงผลลัพธ์ที่ต้องกำรดูที่ไฟล์data.json ที่แนบมำ


To write programs to retrieve information from the web https://www.nice.org.uk/guidance/ng155/history by extracting the documents as shown
Below


Tools to use
1. Requests
2. beautifulsoup4
Which the information can be retrieved To be in json format and request to use all the files in the json file

Information that is required as below

By example, the desired result is to look at the attached data.json file

'''

import json 
import requests
from bs4 import BeautifulSoup

def get_data_history():
    data = requests.get('https://www.nice.org.uk/guidance/ng155/history')
    if data.status_code == 200:

        soup = BeautifulSoup(data.text, 'html.parser')

        get_results = []
        for result in soup.find('div', attrs={'class': 'panel-grid isotope unstyled'}).find_all('div', attrs={'class':'panel panel-resources isotope-item'}):
            results_dict = {}
            
            title = result.find('div', attrs={'class':'panel-heading'}).find('h3').get_text()
            results_dict['title'] = title
            
            
            value_list = []
            for value in result.find('ul', attrs={'class':'media-list'}).find_all('li', attrs={'class': 'media media-resource'}):
                
                    
                    
                value_dict = {}
                try:
                    value_a = '%s%s' % ('https://www.nice.org.uk',value.find('a').get('href'))
                    value_dict['pdf'] = value_a
                    value_text =value.find('i').next_sibling.string
                    value_dict['title'] = value_text.strip().rstrip()
                    value_size = value.find('sup').get_text()
                    value_dict['pdf_size'] = value_size.strip().rstrip()
                    value_time = value.find('time').get_text()
                    value_dict['time'] = value_time.strip().rstrip()
                except AttributeError as e:
                    pass
               
                value_list.append(value_dict)
            results_dict['pdf'] = value_list
            get_results.append(results_dict)
        
        
        return get_results
        
if __name__ == "__main__":
        
    #print(json.dumps(get_results, sort_keys=True, indent=4))
    print(json.dumps(get_data_history(), indent=4))
    
    
    # how to run
    # python 003.py > data.json
