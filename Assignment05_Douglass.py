#Assignment 05

class BasicMathOperations:
    
    def GreetUser(first_name,last_name):
        print(f"Hello {first_name} {last_name}, welcome to Assignment 05!")
        
    def AddNumbers(number1,number2):
        num_sum = number1 + number2
        print(f"The sum of {number1} and {number2} is {num_sum}.")
        
    def PerformOperations(num1,num2,operator):
        if num1 < num2:
            num1,num2 = num2,num1
        if operation == 'd':
            quotient = num1/num2
            return quotient
        elif operation == 'm':
            product = num1*num2
            return product
        elif operation == 'a':
            num_sum = num1 + num2
        elif operation == 's':
            difference = num1 - num2
            return difference
        
    def SquareNumber(number):
        answer = (number)**0.5
        return answer
         
    def Factorial(number):
        for i in range(1,n+1):
            number = number*i
        return number
        
    def Counting(start_number,end_number):
        count_list = list(start_number,end_number)
        return count_list
          
    def calculateHypotenuse():
        
        def calculateSquare():
    
    def RectangeArea(width,length):
        
    def PowerNumber(number):
        
    def ArgumentType(argument):
        
def main():
    user = BasicMathOperations()
    answer = input("Hello! Welcome to Python, I have a set of questions and operations to share with you, do you want to hear them? Please enter Y for yes and N for no:")
    
    if answer == 'Y':
        choice = int(input(f"""Great Choice! Here are your options, please enter the number of the prompt you'd like to interact with:
        1.) Greet User  
        2.) Add Numbers
        3.) Perform Operation
        4.) Square Numbers
        5.) Factorial
        6.) Counting
        7.) Computing Hypotenuse
        8.) Area of Rectangle
        9.) Power of a Number
        10.) Type of Argument"""))
        
        if choice == 1:
            firstname = input("Please enter your first name:")
            lastname = input("Please enter your last name:")
            GreetUser(firstname,lastname)
            
        elif choice == 2:
            number1 = float(input("Please enter a number:"))
            number2 = float(input("Please enter another number:"))
            AddNumbers(number1,number2)
            
        elif choice == 3:
            number1 = float(input("Please enter a number."))
            number2 = float(input("Please enter another number."))
            operation = input("Next you need to enter an operation. Your options are addition(a), subtraction(s), multiplication(m), division(d), please enter one:")
            print(f"\nThe answer using your desired operation is {PerformOperations(number1,number2,operation)}")
            
        elif choice == 4:
            number = float(input("Please enter the number you would like squared:"))
            if number > 0:
                print(f"The answer is {SquareNumber(number)}")
            else:
                print("Invalid response, cannot square a negative number or zero!")
            
        elif choice == 5:
            number = int(input("Please enter an integer, this program will find its factorial:"))
            print(f"The factorial is {Factorial(number)}")
            
        elif choice == 6:
            start = int(input("Please enter the starting number:"))
            end = int(input("Please enter the ending number:"))
            print(f"\nStarting from {start} and ending at {end}, your count is {Counting(start,end)}")
            
        elif choice == 7:
            
        elif choice == 8:
            
        elif choice == 9:
            
        elif choice == 10:
            
        else:
            print("INVALID RESPONSE")






    elif answer == 'N':
        print("Rude.")  
    else:
        print("Invalid Answer!!!!")


main()        