"""
http://www.codechef.com/JULY14/problems/DISHOWN
"""
 
#from logger import log #mylogger
ownerArr = []
dishScore = []
 
#@log
def compete(dish1,dish2) :
    global ownerArr, dishScore
    owner1 = owner(dish1)
    owner2 = owner(dish2)
    if owner1 == owner2 :
        print "Invalid query!"
        return
    if dishScore[owner1] > dishScore[owner2] :
        ownerArr[owner2] = owner1
    elif dishScore[owner1] < dishScore[owner2] :
        ownerArr[owner1] = owner2
    # return ownerArr
 
#@log
def owner(dishNum) :
    while dishNum != ownerArr[dishNum] :
        oldDishNum = dishNum
        dishNum = ownerArr[dishNum]
        ownerArr[oldDishNum] = ownerArr[dishNum]
    return dishNum

T = int(raw_input())
for _ in xrange(T) :
    N = int(raw_input())
    dishScore = [0]+map(int,raw_input().split())
    Q = int(raw_input())
    ownerArr = range(N+1)	#initialize array
    for _i_ in xrange(Q) :
        QArr = map(int,raw_input().split())
        # x=0;print [(x,eval(x)) for x in ['QArr','ownerArr','dishScore','N'] if x in locals()]
        QType = QArr[0]
        if QType == 0 : # compete
            compete(QArr[1],QArr[2])
        else : # output the dish owner number
            print owner(QArr[1])	
        # x=0;print [(x,eval(x)) for x in ['QArr','ownerArr','dishScore','N'] if x in locals()]

