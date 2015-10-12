#coding: utf-8
"""APP. search engine"""
import re
import os
import sys
import time
import urllib

#cont = 0
class point(object):#_motor
    def __init__(self):
        self.web = "" #pagina1
        self.web2 = "" #pagina2
        self.word = "" #palabra
        self.ser1 = "" #bus1
        self.ser2 = "" #bus2
        self.res1 = ""
        self.res2 = ""
        self.cont1 = 0
        self.cont2 = 0
        self.op = 0 #oportunidad

    def buscar(self):#busqueda
        os.system("cls")
        os.system("clear")
        ans = "yes" #respuesta
        while ans != "no":

            print "Welcome\n "
            print "Search Engine \n"

            self.web = raw_input("insert first URL: ")
            self.web2 = raw_input("insert second URL: ")
            self.word = raw_input("insert the word that you want search: ")

            self.ser1 = urllib.urlopen(self.web)
            self.res1 = self.ser1.read()
            self.cont1 = len(re.findall(self.word, self.res1))

            self.ser2 = urllib.urlopen(self.web2)
            self.res2 = self.ser2.read()
            self.cont2 = len(re.findall(self.word, self.res2))

            if self.cont1 > self.cont2:
                print "\nthe word that you inserted is: " + self.word
                print "it shows : " + str(self.cont1) + " times in the fisrs URL"
                print "it shows : " + str(self.cont2) + " times in the second URL"
                print "this is the page where the word shows most times: " + self.web + "\n"
                break

            elif self.cont2 > self.cont1:
                print "\nthe word that you inserted is: " + self.word
                print "it shows : " + str(self.cont1) + " times in the first URL"
                print "it shows : " + str(self.cont2) + " times in the second URL"
                print "this is the page where the word shows most times: " + self.web2 + "\n"
                break

            elif (self.cont1 > 0) and (self.cont2 > 0) and self.cont1 == self.cont2:
                print "\nthe word that you inserted is: " + self.word
                print "it shows : " + str(self.cont1) + " times in the first URL"
                print "it shows : " + str(self.cont2) + " times in the second URL"
                print "all pages shows the same quantity"
                break

            elif (self.cont1 == 0) and (self.cont2 == 0): 
                print "\ncan't find the word"
                print "all pages shows the same quantity\n"
                break

      	self.again()    
    
    def again(self):
			ans = raw_input("do you want to insert another word? y/n :")
			if type(ans) != int:
				ans = str(ans)
				if ans == "y" or ans == "yes":
					self.buscar()
				elif ans == "n" or ans == "no":
					self.menu()
			else:
				print"ingresa bien las cosas"
				os.system("cls")
				os.system("clear")


    def menu(self):
        self.op = 0
        while True:
            while (self.op != 1) or (self.op != 2):
            	print "    Search Engine"
                print "1) Find word"
                print "2) Exit"

                self.op = raw_input("insert an option: ")
                try:
                    self.op = int(self.op)
                    if self.op > 0 and self.op <= 2:
                        break
                    else:
                        print u"insert a valid option\n"
                        time.sleep(1)
                        os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    print u"insert a valid option\n"
                    time.sleep(1)
                    os.system("clear")

            if self.op == 1:
                sta = point()#inicio
                sta.buscar()

            if self.op == 2:
                print "coming out ..."
                time.sleep(2)
                os.system("clear")
                print "Thanks for visit us"
                time.sleep(1)
                sys.exit()
        self.op = 0
        return

START = point()
START.menu()




































