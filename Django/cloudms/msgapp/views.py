import os

from django.http import HttpResponse, JsonResponse, FileResponse, StreamingHttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
from django.template import Template, Context


def msgproc(request):
    datalist = []
    if request.method == 'POST':
        # 发送方
        userA = request.POST.get("userA", None)
        # 接收方
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open('msg.txt', 'a+') as fp:
            fp.write("{}--{}--{}--{}\n".format(userB, userA, msg, time.strftime('%Y-%m-%d %H:%M:%S')))
            fp.close()

    if request.method == 'GET':
        userC = request.GET.get('userC')
        if userC is not None:
            with open('msg.txt', 'r') as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt += 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
                    datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "MsgSingleWeb.html", {"data": datalist})


def homeproc(request):
    # return HttpResponse("<h1>知识首页,具体功能访问<a href='./msggate'>这里</a> </h1>")
    response = HttpResponse()
    response.write("<h1>知识首页,具体功能访问<a href='./msggate'>这里</a> </h1>")
    response.write("<h1>第二行</h1>")
    return response


def homeproc1(request):
    response = JsonResponse({'name': '张三'})
    return response


def homeproc2(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/bg.jpg", 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="bg.jpg"'
    return response


def aa(request):
    return render(request, 'upload_file.html')


def file_download(request):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    fname = 'E:\\20180\\Pictures\\Saved Pictures\\1.png'
    response = StreamingHttpResponse(file_iterator(fname))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="1.jpg"'
    return response


def upload_file(request):
    """
    方法一：
    　　我们可以在settings.py中注释掉一行即可。这一行大概在46行左右。
        'django.middleware.csrf.CsrfViewMiddleware'
    方法二：
    　　在html页面的form标签下加上
        {% csrf_token %}
    方法三：
    　　views.py上导入
        from django.views.decorators.csrf import csrf_exempt
    　　然后在自己写的函数上面加上
        @csrf_exempt
    """
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\20180\\Pictures\\Saved Pictures", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")


def pgproc(request):
    template = Template("<h1>这个程序的名字: {{name}} </h1>")
    context = Context({"name": "实验平台"})
    return HttpResponse(template.render(context))
