"""
#
# Part: Python Try Except
#
"""

# the "try" block lets you test a block of code for errors.
# The "except" block lets you handle the error.
# The "else" vlock lets you excute code when there is no error.
# the "finally" block lets you excute code, regardless of the result of the try- and except blocks.
try:
    print(x)
except NameError as e:
    print("Not defined! :", e)
except:
    print("Somthing else went wrong!")
    
try:
    print("Hello World")
except:
    print("Somthing else went wrong!")
else: 
    print("Nothing went wrong!")
    
try:
    print(x)
except:
    print("Somthing else went wrong!")
finally:
    print("Finished!")


#x = -1
#if x < 0:
 #   raise Exception ("Sorry, no number below zero.")
 
x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed.")