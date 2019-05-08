for num in range(1,21):
    if num == 4 or num == 13:
        print (str(num) + " unlucky")
    elif num % 2 == 0: # even
        print (str(num) + " is even")
    else:
        print (str(num) + " is odd")

