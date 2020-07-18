from django.shortcuts import render
from datetime import datetime
# Create your views here.


def msgproc(request):
    datalist = []
    if request.method == 'POST':
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        time = datetime.now()
        msg = request.POST.get("msg", None)

        with open("msgdata.txt", 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, msg,
                                                time.strftime("%Y-%m-%d %H:%M:%S")))
            f.close()

    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if None != userC:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt += 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
                        datalist.append(d)
                    if cnt > 9:
                        break
                f.close()

    return render(request, "MagSingleWeb.html", {"data": datalist})

