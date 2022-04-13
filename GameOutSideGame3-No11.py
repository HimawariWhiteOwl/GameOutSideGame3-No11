import requests
from cffi.backend_ctypes import xrange

your_list = 'abdijkmo'
complete_list = []
answerList = []
for current in xrange(6):
    a = [i for i in your_list]
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a
    print(complete_list)
print(complete_list)
# /([^ahote ircbus])\w+/g
for index in range(len(complete_list)):
    indexA = complete_list[index].find('a')
    indexB = complete_list[index].find('b')
    print(indexB)
    if(indexA==1 and indexB == 3 and len(complete_list[index])==6):
        answerList.append(complete_list[index])
        url = 'http://localhost:3000/answers'
        myobj = {'password': complete_list[index]}
        x = requests.post(url, data=myobj)
        print(x)
print("Answer is {0}".format(answerList))


