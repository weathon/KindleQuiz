# 新词时负数，每过一次就加一个数，每过一天就-m,每一次训练排序来？
# 还是两个排序，优先掌握程度然后是时间？
from flask import Flask
import random
import queue
app = Flask(__name__)

f=open("export.txt","r")
words=f.read()
f.close()
f=open("points.txt","r")
energypoints=int(f.read())
f.close()

#If passed, add -1 to the end, means random, if not, add it self
myq=queue.Queue()

notagain={}
mydict={}
#If point==2, add to here, but 如果三次抽到一張卡，那麽還是要檢查（模擬過一會檢測）

for i in [-1,-1,-1,-1,-1,-1,-1]:
    myq.put(i)


words_list=words.split("\n\n")
for i in words_list:
    stmp=i.split("******")
    notagain[stmp[0]]=0
    mydict[stmp[0]]=stmp[1]

@app.route('/getword')
def getword():
    stattmp=myq.get()
    print(stattmp)
    if stattmp==-1:
        return words_list[random.randint(0,len(words_list)-1)]
    #elif notagain[stattmp]==1:#got here once
    #    return words_list[random.randint(0,len(words_list)-1)]
    #    notagain[stattmp]=0
    else:
        return stattmp+"******"+mydict[stattmp]

@app.route('/queue')
def returnq():
    return myq.size()

@app.route('/')
def main():
    f=open("index.html","r")
    tmp=f.read()
    f.close()
    return tmp

@app.route('/feedback&<points>&<word>')
def feedback(points,word):
    global energypoints
    energypoints+=int(points)
    print(points)
    if points==0:
        myq.put(word)
    elif points==2:
        myq.put(-1) 
    return ""

@app.route("/getpoints")
def getpoints():
    f=open("points.txt","w")
    f.write(str(energypoints))
    f.close()
    return str(energypoints)



#内存到硬盘的频率？
