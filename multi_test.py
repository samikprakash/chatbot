import multiprocessing

x = 0

def some_while(l):
    global x
    while l[0]==0:
        pass
    print("x = ",x)

def takeinput(l):
    
    global x
    for i in range(10):
        s = int(input("enter"))
        l[0] = s

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        test = manager.list([0])
        p1 = multiprocessing.Process(target = takeinput,args = (test,))
        p2 = multiprocessing.Process(target = some_while,args = (test,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

        