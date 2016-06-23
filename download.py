#coding=utf-8
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 获取页面html  http://www.lizhi.fm/box#play
def get_page_html(url):
    response = urllib.urlopen(url)
    return response.read()

# 通过正则获取mp3地址
def getImg(html):
    reg = r'title="(.+?)" class=".*?data-url="(.+?\.mp3)" data-id'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0 
    list = []
    names = []
    for imgurl in imglist:
        if names.count(imgurl[1].decode('utf-8'))>0:
            continue
        dict = {"Name": imgurl[0].decode('utf-8'), "Url": imgurl[1].decode('utf-8')}; 
        list.append(dict)
        names.append(imgurl[1].decode('utf-8'))
        x+=1
    print x
    return list

#html = get_page_html("http://www.lizhi.fm/17248/")

# 写文件
def write_file(html,url):
    # 打开文件
    fo = open(url, "w")
    fo.write(html)
    # 关闭文件
    fo.close()
    
# 读文件
def read_file(url):
    fo = open(url, "r")
    line = fo.read()
    # 关闭文件
    fo.close()
    return line

def deal_file_name(name):
    name = name.replace("<",'')
    name = name.replace(">",'')
    name = name.replace("/",'')
    name = name.replace("\\",'')
    name = name.replace("|",'')
    name = name.replace(":",'')
    name = name.replace("：",'')
    name = name.replace("\"",'')
    name = name.replace("*",'')
    name = name.replace("?",'')
    return name
    #<>,/,\,|,:,'',*,? 

def run():
    wurl = raw_input("\n\nPlease enter your url.")
    #print wurl
    #write_file(get_page_html("http://www.lizhi.fm/17248/").decode('utf-8'),"test.txt")
    #write_file(get_page_html("http://www.lizhi.fm/17248/p/2.html").decode('utf-8'),"test.txt")
    #ll = getImg(read_file("test.txt"))
    html = get_page_html(wurl).decode('utf-8')
    ll = getImg(html) 
    for mp3 in ll:
        url = mp3["Url"]
        name = mp3["Name"]
        '''
        strs = name.split(" ") 
        size = len(strs)
        #print strs[0:size-1]
        fname = strs[size-1]+"."+deal_file_name(name)+".mp3"
        '''
        fname = deal_file_name(name)+".mp3"
        
        print "Downloading --> "+ fname
        urllib.urlretrieve(url,fname) 
        print "-----------------------------------------------------"
    print "It's all over! Press any key to exit."
 
run()

