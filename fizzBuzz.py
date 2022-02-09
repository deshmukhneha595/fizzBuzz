# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:41:26 2022

@author: Lenovo
"""


def fizzBuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i)+"= FIZZBUZZ")
        else:
                if(i%3==0):
                    print(str(i)+"= FIZZ")
                else:
                        if(i%5==0):
                            print(str(i)+"= BUZZ")
                        else:
                                print(str(i))
                        
                
            

