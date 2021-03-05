# coding: utf-8
import os
import urllib.request
import webbrowser
import time
from html_support import openpath, dirlist, fwinfo, frinfo, info_title, info_keywords, info_description, info_link, info_article, info_footer, creat_html, upunit, execute



if __name__ == '__main__':
    cmddir = 'D:\\Workspace'
    pydir = 'D:\\Workspace\\Html\\zhengxie.info\\common\\py'
    print('......判断运行目录......')
    if os.getcwd()==cmddir or os.getcwd()==pydir:
        print('......运行目录正确！......')
        os.chdir(pydir)
        execute()
    else:
        print('......运行目录错误！......')
        print('......cmd命令目录：')
        print(cmddir)
        print('......py存放目录：')       
        print(pydir)
        print('......当前运行目录：')
        print(os.getcwd())

    # pydir = input("\n......程序执行完毕！......\n......按Enter关闭窗口......")
    """
    # 网址拼接

    # from urllib.parse import urljoin
    # a = urljoin("https://zhengxie.info/folder/currentpage.html", "../")  

    # b = urljoin("https://zhengxie.info/folder/currentpage.html", "folder2/anotherpage.html")  

    # c = urljoin("https://zhengxie.info/folder/currentpage.html", "/folder3/anotherpage.html")  

    # d = urljoin("https://zhengxie.info/folder/currentpage.html", "../finalpage.html")  

    # print (a)
    # print (b)
    # print (c)
    # print (d)
    """