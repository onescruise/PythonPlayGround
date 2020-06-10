
'''
学习目标:
1. 理解什么是sys.argv
* sys.argv[0]就是本程序的名字
* sys.argv[1]什么的就是加入的名字
2. 打开网页
'''

# webbrower里面的open()函数是一个可以启动一个新浏览器，打开指定的url
import webbrowser,sys
webbrowser.open('https://www.zhihu.com/question/23711222')
