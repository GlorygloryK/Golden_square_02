def fizzbuzz(num):
    if num %3 == 0 and num %5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num 
    
# print (fizzbuzz(1))
# print (fizzbuzz(2))
# print (fizzbuzz(3)) # Should return Fizz 
# print (fizzbuzz(4))
# print (fizzbuzz(5)) # Should return Buzz 
# print (fizzbuzz(15))# Should return Fizzbuzz 