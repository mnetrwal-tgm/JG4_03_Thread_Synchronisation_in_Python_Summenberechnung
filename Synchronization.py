import threading

class simucount (threading.Thread):
    counter=0
    summe=0
    lock=threading.Lock()
    def __init__(self, part):
        """
        Initialize object of simucount
        :param part: which number
        :param threads:
        """
        threading.Thread.__init__(self)
        self.part=part

    def run(self):
        """Sum a part of the numbers"""
        for i in range(0, int(simucount.maximum/simucount.anzahlthreads)):

            with simucount.lock:
                simucount.summe+=int(simucount.maximum/simucount.anzahlthreads)*self.part+i+1
                simucount.counter+=1

        i3 = simucount.maximum - int(simucount.maximum / simucount.anzahlthreads) * simucount.anzahlthreads
        with simucount.lock:
            if simucount.maximum/simucount.anzahlthreads % 1 != 0 and simucount.counter+i3==simucount.maximum:
                for i in range(0,i3):
                    simucount.summe += int(simucount.maximum / simucount.anzahlthreads) * simucount.anzahlthreads + i + 1
                    simucount.counter += 1

def toIntChecker(out):
    """
    A simple method to check a User Inputs type as an integer

    :param out: what the user shall see
    :return: the User Input as an Integer
    """
    running2 = True
    while running2:
        try:
            #Takes input and trys to turn it into an integer. If it doesn't work, an error gets printed and the code
            # gets redone
            re = input(out)
            re = int(re)
            running2 = False
        except:
            print("Bitte geben sie eine Zahl ein!")

    return re

import time

t=time.time()
threads = []
simucount.maximum=toIntChecker("Was ist ihr höchster Summand?")
simucount.anzahlthreads=  toIntChecker("Wie viele Threads sollen daran arbeiten? (Maximal der höchste Summand)")
t1=time.time()
for i in range(0, simucount.anzahlthreads):
    thread=simucount(i)
    threads+=[thread]
    thread.start()

# wait for childthreads
for x in threads:
    x.join ()
t2=time.time()
# print sum
print(simucount.summe)
#print runtime
print("%s Seconds over all runtime" %(t2-t))
print("%s Seconds runtime after user inputs" %(t2-t1))
