#coding:utf-8

from shutil import *
from os import path



class Cp:

    def __init__(self,pos1,pos2):
        self.pos1 = pos1
        self.pos2 = pos2



    def common(self,*args):

        if path.exists(self.pos1) is True:

            if len(args) == 0:
                if path.isfile(self.pos1) is True:
                    copyfile(self.pos1, self.pos2)
                else:
                    try:
                        copyfile(self.pos1, self.pos2)
                    except:
                        print('{} must be a file'.format(self.pos1))


            elif 'r' in args and len(args) == 1:
                if path.isfile(self.pos1):
                    copyfile(self.pos1, self.pos2)
                elif path.isdir(self.pos1):
                    copytree(self.pos1, self.pos2, ignore_patterns(copystat), copy_function=copyfile)

            elif 'p' in args and len(args) == 1:
                if path.isfile(self.pos1):
                    copy2(self.pos1, self.pos2)
                else:
                    try:
                        copy2(self.pos1, self.pos2)
                    except:
                        print('{} must be a file, is a directory (not copied)'.format(self.pos1))

            elif 'p' in args and 'r' in args:
                if path.isfile(self.pos1):
                    print('right there')
                    copy2(self.pos1, self.pos2)
                if path.isdir(self.pos1):
                    copytree(self.pos1, self.pos2,copy_function=copy2)






c = Cp('/tmp/lab','/tmp/lab7')
print(c.common('p','r'))




