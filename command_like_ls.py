#coding:utf-8

from os import listdir,path,stat
from pathlib import Path
import time

class Ls:   

    def __init__(self,pos='.'):
        self.pos = pos
        for element in listdir(self.pos):
            if element.startswith('.'):
                continue
            else:
                print(element)

    def showall(self):
        for i in listdir(self.pos):
            print(i)

    def long(self,oneopt=True,twoopt='a'):
        if oneopt == 'h' and twoopt == False:
            #Ls.__init__(self)
            #self.showall()
            for x in listdir(self.pos):
                print('{} {} {} {} {} {} {} {} '.format('-' if Path(x).is_file else 'd',oct(stat(x).st_mode)[-3:], '1' if Path(x).is_file else len(listdir(self.pos)),
                Path(x).owner(),Path(x).group(),path.getsize(x), time.strftime('%m %d %H:%M',time.localtime(stat(x).st_mtime)),x))

        elif oneopt == 'h' and twoopt == 'a':
            print('holy fuck')






    #def long(self):

    #def show(self):



a = Ls()
#print(a)
#print(a.showall())
print(a.long(oneopt='h',twoopt=False))