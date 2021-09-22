# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:22:25 2021

@author: chris
"""



def format_amount(amount):
    result = 0
    while True:
        try:
            result = "${:,.2f}".format(float(input(amount)))
            
        except ValueError:
            if result != float():
                result = "${:,.2f}".format(float(input(amount)))
            print("Please enter a valid number.")
      
        else:
             return result


            
amount_spent = format_amount("Enter spending amount")
print(amount_spent)



