# 新词时负数，每过一次就加一个数，每过一天就-m,每一次训练排序来？
# 还是两个排序，优先掌握程度然后是时间？
from flask import Flask
import random
app = Flask(__name__)

f=open("export.txt","r")
words=f.read()
f.close()

words_list=words.split("\n\n")


@app.route('/getword')
def getword():
    return words_list[random.randint(0,len(words_list)-1)]

@app.route('/')
def main():
    f=open("index.html","r")
    tmp=f.read()
    f.close()
    return tmp