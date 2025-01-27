number1 = int(input("please enter first number" ))
number2 = int(input("please enter second number "))
process = input("1 for addition  \n 2 for subtraction \n 3 for multiplication \n 4 for division \n ")



if number1 > number2 :
    num1 = number1
    num2 = number2
else:
    num1 = number2
    num2 = number1    

if process == '1':
    result = num1 + num2
    
elif process == '2':
    result = num1 - num2
    
elif process == '3':
    result = num1 * num2    
    
elif process == '4':
    result = num1 / num2

else:
   print('Something went wrong')    
        
   
print(result)    
