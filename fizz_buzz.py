def fizz_buzz(check_array):
    for i in range(len(check_array)):
        if(check_array[i] % 3 == 0 and check_array[i] % 5 == 0):
            print("Fizz Buzz")
        elif(check_array[i] % 3 == 0):
            print("Fizz")
        elif(check_array[i] % 5 == 0):
            print("Buzz")
        else:
            print(check_array[i])

fizz_buzz([1,2,3,4,5,6,7,8,9,10])