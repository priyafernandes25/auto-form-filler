import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

current_dir=os.path.dirname(__file__)

#url='http://httpbin.org/forms/post'
url='http://www2.cs.uregina.ca/~ku205/assign/form-signup.html'
def contains(name_,list_):
    found=0
    for items in list_:
        if items==name_:
            found=1
            break
    return found

def autosignup(url):
    
    source_code=requests.get(url)
    driver=webdriver.Firefox()
    driver.get(url)
    plain_code=source_code.text
    name_list=[]
    type_list=[]
    value_list=[]
    
    soup=BeautifulSoup(plain_code,"html.parser")
    for var in soup.findAll('input'):
        name_=var.get('name')
        
        
        type_=var.get('type')
        
        if type_=="email":
            value_="linareddy30@yahoo.com"
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
        elif type_=="date":
            value_="1996-11-12"
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
        elif type_=="number":
            value_=22
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
        elif type_=="password":
            value_='lina245@uu'
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
        elif type_=="file":
            value_=None
            continue
        elif type_=="tel":
            value_=8876545674
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
        elif type_=="checkbox":
            if (contains(name_,name_list)==0):
                for check_boxes in driver.find_elements_by_name(name_):
                    check_boxes.click()
            else:
                continue
        elif type_=="radio":
            if (contains(name_,name_list)==0):
                value_=var.get('value')
                radio1=driver.find_element_by_name(name_)
                radio1.click()
            else:
                continue
        elif type_=="time":
            value_="19:00"
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
        elif type_=="submit":
            value_="submit"
            elem=driver.find_element_by_name(name_)
            elem.click()   
        else:
            value_="lina245@uu"
            elem=driver.find_element_by_name(name_)
            elem.send_keys(value_)
            
        name_list.append(name_)
        value_list.append(value_)
        type_list.append(type_)
            
        #for the select tag
    for var in soup.findAll('select'):
        name_=var.get('name')
        obj=Select(driver.find_element_by_name(name_))
        obj.select_by_index(2)
        
         #if button present then we run this logic
    if (len(driver.find_elements_by_tag_name('button'))>0):
        elem=driver.find_element_by_tag_name('button')
        elem.click()
        print('button')
    
        
    next_url=driver.current_url
    return next_url
    

 
    
def main(url):
    check_type=[]
    button=[]
    source_code=requests.get(url)
    driver=webdriver.Firefox()
    driver.get(url)
    plain_code=source_code.text
    soup=BeautifulSoup(plain_code,"html.parser")    
    for var in soup.findAll('input'):
        type_=var.get('name')
        check_type.append(type_)
    for var1 in soup.findAll('button'):
        buttons=var.string
        button.append(buttons)
    if len(check_type)==2 and len(button)>1:
        next_url=autologin(url)
    elif len(check_type)==3 and len(button)==0:
        next_url=autologin(url)
    elif len(check_type)>0:
        next_url=autosignup(url)
    else:
        exit()
        
    fx=open('Next url',"w")                         
    fx.write("Next url: "+next_url+"\n") 
    fx.write("Successfully done!!")                      
    fx.close()

    print("Next url: "+next_url)
    print("Successfully done!!")

        
main(url)