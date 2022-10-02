import requests
from datetime import datetime
import threading


theips = ["https://bvmg.amserp.in/", "https://bav.amserp.in/", "https://bvvt.amserp.in/",
          "https://bnvv.amserp.in/", "https://bmv.amserp.in/",  "https://bvvt.amserp.in/","https://bvmer.amserp.in/"]
therange = input("Range(None):- ")
threadnum = int(input("Threads:- ") or 50)
therange = therange.split(" ")
for i in theips:
    theip = str(f"{i}banner/")

    filename = i.split("//")[1].split("/")[0] + ".txt"
    #filename = f"/content/{filename}"
    print(filename)
    open(filename, "w+")

    def getinfo(info):
        r = requests.get("{}{}.jpg".format(theip, info))
        if r.status_code == 200:
            return info
        else:
            return None

    thethreads = []

    def pingserver(start, end, thefile):

        for i in range(int(start), int(end)):

            try:
                info = getinfo(i)
                if info != None:
                    print(info)

                    thefile.write(str(info)+"\n")
                    #thefile.close()
            except Exception as e:
                #print(e)
                pass

    width = int(len(range(int(therange[0]), int(therange[1])))/threadnum)
    thefile = open(filename, "w")
    for i in range(int(therange[0]), int(therange[1]), width):

        zeerange = (i, i + width, thefile)
        thethreads.append(threading.Thread(target=pingserver, args=(zeerange)))
    for i in thethreads:
        i.start()
    for i in thethreads:
        i.join()
