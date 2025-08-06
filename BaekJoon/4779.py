import sys
def Cantor(string,a,b) :
    length = b-a
    if length <= 1:
        return
    s = a + length // 3
    e = a + length // 3 * 2
    for i in range(s,e) :
        string[i] = " "
    Cantor(string, a, s)
    Cantor(string, e, b)
    
while 1 :
    try :
        n = int(sys.stdin.readline())
    except:
        break #E0F처리
    string = list('-'* (3**n))
    Cantor(string,0,len(string))
    print(''.join(string))