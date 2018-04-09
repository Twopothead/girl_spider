# coding:utf-8 
import requests
from lxml import html
from lxml import etree
import os
from threading import Thread
import re
base_url = "http://www.cangls.com/tag/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/61.0.3163.100 Safari/537.36"}
nr_girl_nude_photo = 1
def getxpath(html):
    return etree.HTML(html)

def get_nr_page_url(girlname,nr):
    if nr == 0:
        url = base_url + girlname + ".html"
    # http://www.cangls.com/tag/长泽梓.html
    else: 
        url = base_url + girlname + "_"+str(nr)+".html"
    # http://www.cangls.com/tag/长泽梓_1.html
    return url
    # response = requests.get(url).content
    # selector = html.fromstring(response)
def get_girl_names():
    girl_names = []
    with open("./pornstar_names.txt",'r') as porn_names_file:
        for  line in porn_names_file.readlines():
            name = line.strip()
            if name.find("_") == -1:
                girl_names.append(name)
    return girl_names

def download_img(img_title,img_detail_websites):
    # num = 1 
    global nr_girl_nude_photo
    try :  
        for url,title in zip(img_detail_websites,img_title):
                filename = title
                print(filename+":   "+url)
                with open(str(nr_girl_nude_photo)+"__"+filename,'wb') as f:
                    f.write(requests.get(url,headers=headers,timeout=5).content)
                    nr_girl_nude_photo += 1
                    # num += 1
    except Exception as e:
        print(repr(e))
        return download_img

def get_str_nr(nr):
# 937 japanese girls    
    if(nr<10):
        return "00"+str(nr)
    elif(nr<100):
        return "0"+str(nr)
    return str(nr)
            

def get_girl_page(name,page_img_url):
    try:
        response = requests.get(page_img_url,headers=headers,timeout=7).content
        selector = html.fromstring(response)
        img_detail_websites = selector.xpath("//img/@src")
        # print(img_detail_websites)
        # we should delete the logo picture:/picture/logo-3-1.png
        img_detail_websites.remove('/picture/logo-3-1.png')
        fanhao = selector.xpath("//h2/a/text()")
        # print(fanhao)
        print("Begin to download...")
        download_img(fanhao,img_detail_websites)
    except Exception as e:
        print(repr(e))
        return get_girl_names    


# # url = "http://www.cangls.com/tag/长泽梓.html"
# url = "http://www.cangls.com/tag/波多野结衣.html"

# response = requests.get(url).content
# selector = html.fromstring(response)
# img_detail_websites = selector.xpath("//img/@src")
# # print(img_detail_websites)
# # we should delete the logo picture:/picture/logo-3-1.png
# img_detail_websites.remove('/picture/logo-3-1.png')
# fanhao = selector.xpath("//h2/a/text()")
# # print(fanhao)
# print("Begin to download...")
# # download_img(fanhao,img_detail_websites)

if not os.path.exists("girl_images"):
    os.makedirs("girl_images")



girl_names = get_girl_names()
print(girl_names)
print("total: "+str(len(girl_names))+" beautiful girls")
os.system("pwd")
print("changing directory: girl_images/")
os.chdir("girl_images"),os.system("pwd")
nr_girl = 1
for name in girl_names:
    if not os.path.exists(get_str_nr(nr_girl)+"__"+name):
        os.makedirs(get_str_nr(nr_girl)+"__"+name)
        print("pornstar"+get_str_nr(nr_girl)+": "+name)
        os.chdir(get_str_nr(nr_girl)+"__"+name),os.system("pwd")
        nr_girl_nude_photo = 1
        for i in range(0,35):    
            print("    "+get_nr_page_url(name,i))
            get_girl_page(name,get_nr_page_url(name,i))
        os.chdir("..")
    nr_girl += 1

print(" OK, nude photos of beatiful girls have been successfully saved!!! : )")
print(" FBI WARNING: Copyright (C) 2018 Frank Curie (邱日)")





# reference: - https://zhuanlan.zhihu.com/p/26395979    
#            - https://zhuanlan.zhihu.com/p/25572729
#            - https://zhuanlan.zhihu.com/p/25784651
# learn Xpath
# Python爬虫跳过异常