#this is incase you have an if, elif,and else
#example1
var = 100
if var < 200:
   print('Expression value is less than 200')
   if var == 150:
      print('Which is 150')
   elif var == 100:
      print('Which is 100')
   elif var == 50:
      print('Which is 50')
   elif var < 50:
      print('Expression value is less than 50')
else:
   print('Could not find true expression')

print('Good bye!')

#example2
marks = 500
if marks < 1000:
	print('it is very less than it')
	if marks == 500:
		print('They are equal')
	elif marks != 600:
		print('it is not equal')
	elif marks >= 400:
		print('it is greater')
else:
	print('I love being 500!')

