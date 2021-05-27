# Python program to compare dates
# importing datetime module
import datetime

today = datetime.date.today()

# input date in yyyy/mm/dd format
print('Wat is het jaar?')
jaar = int(input())
print ('Wat is het maandnummer?')
maand = int(input())
print('Wat is de dag?')
dag = int(input())

d1 = datetime.date(jaar, maand, dag)
print(d1)

# Comparing the dates
d2 = today - d1
print(d2)
