##Exception try, except block

#1
"""try:
    a=b 
except:
    print("the variabvle has not been assigned")"""

#2 Name error in exception
"""try:
    a=b 
except NameError as ex:
    print(ex)"""

#3 zero division error
"""try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Enter The Denominator Gretaer Than zero [0]")"""
#4 all exception caught here
"""try:
    result=1/2
    a=b 
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter denominator gretae rthean xero (0) ")
except Exception as ex1:
    print(ex1)
    print('Main Exception got caught here ')"""

#5 main exception
"""try:
    num=int(input("Enter A Number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominato greatir than 0")
except Exception as ex:
    print(ex) """

#6 try,except,else block
"""try:
    num = int(input(""))
    result=10/num
except ValueError:
    print("not a valid number ")
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else: 
    print(f"the result is{result} ")  """

#7 try, except, else and finally
"""try:
    num = int(input("Enter a number "))
    result=10/num
except ValueError:
    print("not a valid number ")
except ZeroDivisionError :
    print("You can't divide by zero")
except Exception as ex:
    print(ex)
else: 
    print(f"the result is{result} ")
finally:
    print("execution complete")"""

#8 File handling and exception handling

try:
    file=open('example.txt','r')
    content=file.read()
    print(content)
except FileNotFoundError:
    print("The File The doesn't exist")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("file close")