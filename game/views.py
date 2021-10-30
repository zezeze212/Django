from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">我的第一个网页!!!</h1>'
    line2 = '<img src="https://c-ssl.duitang.com/uploads/blog/202107/16/20210716193532_21f90.jpeg">'
    line3='<hr>'
    line4='<a href="/play/">进入游戏界面</a>'
    return HttpResponse(line1+line4+line3+line2)

def play(request):
    line1='<h1 style="text-align: center">游戏界面<hr>'
    line2='<img src="https://c-ssl.duitang.com/uploads/blog/202109/25/20210925233644_3d9ac.png">'
    line3='<a href="/">返回主页面</a>'
    return HttpResponse(line1+line3+line2)
