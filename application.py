#coding: utf-8
"""APP. search engine"""
import re
import os
import sys
import time
import urllib


#cont = 0

class _point(object):
    """the first part of the program"""
    def limp(self):
        """this function serves to clean the window"""
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("reset")

    def __init__(self):
        """here only declare the global variables"""
        self.cont1 = 0
        self.cont2 = 0
        self.slec = 0

    def buscar(self):
        """this function will search the word in both URL"""
        web = ""
        web2 = ""
        word = ""
        ser1 = ""
        ser2 = ""
        res1 = ""
        res2 = ""
        self.limp()
        ans = "yes"
        while ans != "no":
            try:
                web = raw_input("insert first URL: ")
                web2 = raw_input("insert second URL: ")
                word = raw_input("insert the word that you want search: ")
                ser1 = urllib.urlopen(web)
                res1 = ser1.read()
                self.cont1 = len(re.findall(word, res1))
                ser2 = urllib.urlopen(web2)
                res2 = ser2.read()
                self.cont2 = len(re.findall(word, res2))
                if word == "":
                    print "you have to insert some word"
                elif word == "":
                    print word.isspace()
                elif self.cont1 > self.cont2:
                    print "\nthe word that you inserted is: " + word
                    print "it shows : " + str(self.cont1) + " times in the fisrs URL"
                    print "it shows : " + str(self.cont2) + " times in the second URL"
                    print "this is the page where the word shows most times: " + web + "\n"
                    break
                elif self.cont2 > self.cont1:
                    print "\nthe word that you inserted is: " + word
                    print "it shows : " + str(self.cont1) + " times in the first URL"
                    print "it shows : " + str(self.cont2) + " times in the second URL"
                    print "this is the page where the word shows most times: " + web2 + "\n"
                    break
                elif (self.cont1 > 0) and (self.cont2 > 0) and self.cont1 == self.cont2:
                    print "\nthe word that you inserted is: " + word
                    print "it shows : " + str(self.cont1) + " times in the first URL"
                    print "it shows : " + str(self.cont2) + " times in the second URL"
                    self.limp()
                    break
                elif (self.cont1 == 0) and (self.cont2 == 0):
                    break
            except IOError:
                print "this is an invalid URL"
            raw_input("press enter to continue...")
            self.again()
            self.limp()

    def again(self):
        """this function only will ask the user if he wants to insert again other word"""
        while True:
            ans = raw_input("do you want to insert another word? y/n :")
            ans.isalpha()
            ans = ans.lower()
            self.limp()
            #print type(ans)
            checktype = type(ans)
            if checktype != int:
                ans = str(ans)
                if ans == "y" or ans == "yes":
                    self.buscar()
                elif ans == "n" or ans == "no":
                    self.limp()
                    self.menu()

            else:
                print"insert a valid option"
                self.limp()
                #os.system("cls")
                #os.system("clear")

    def menu(self):
        """this is the menu of the search engine"""
        self.limp()
        selec = 0
        while True:
            while (selec != 1) or (selec != 2):
                print "    Search Engine"
                print "1) Find word"
                print "2) Exit"

                selec = raw_input("insert an option: ")
                try:
                    selec = int(selec)
                    if selec > 0 and selec <= 2:
                        break
                    else:
                        print u"insert a valid option\n"
                        time.sleep(1)
                        self.limp()

                except(RuntimeError, TypeError, NameError, ValueError):
                    print u"insert a valid option\n"
                    time.sleep(1)
                    self.limp()

            if selec == 1:
                sta = _point()#inicio
                sta.buscar()

            if selec == 2:
                print "coming out ..."
                time.sleep(2)
                self.limp()
                print "Thanks for visit us"
                time.sleep(1)
                sys.exit()
        selec = 0
        return

START = _point()
START.menu()




































