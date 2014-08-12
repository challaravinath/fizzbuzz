__author__ = 'cravindr'
#Ver-1: of FizzBuzz where it takes numbers from 1 to 100 in Hardcoded way
for num in range(1,101):
    """ verifying below condition as first
     reason being  when we place this condition at end this check is never getting executed"""
    if num % 3 == 0 and num %5 ==0:
        print "FizzBuzz"
    if num %3 == 0:
        print "Fizz"
    if num %5 ==0:
        print "buzz"
    else:
        print num
