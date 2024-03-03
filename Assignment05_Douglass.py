#Assignment 05

def main():
    
    user = BasicMathOperations()  #intial object, allows for the methods in the class to be implemented
    response = 0 #initialize response for while statement
    
    answer = input("Hello! Welcome to Python, I have a set of questions and operations to share with you, do you want to hear them? Please enter Y for yes and N for no:")
    
    while response != 'N':
        
        if answer == 'Y': #Allow user to choose a task from the ones listed, each corresponds to one of the required problems
            choice = int(input("""\nGreat Choice! Here are your options, please enter the number of the prompt you'd like to interact with:\n
    1.) Greet User  
    2.) Add Numbers
    3.) Perform Operation
    4.) Square Numbers
    5.) Factorial
    6.) Counting
    7.) Computing Hypotenuse
    8.) Area of Rectangle
    9.) Power of a Number
    10.) Type of Argument\n"""))
            
            if choice == 1: #Greet User
                firstname = input("Please enter your first name:")
                lastname = input("Please enter your last name:")
                user.GreetUser(firstname,lastname) #implement method
                
            elif choice == 2: #Add Numbers
                number1 = float(input("Please enter a number:"))
                number2 = float(input("Please enter another number:"))
                user.AddNumbers(number1,number2) #implement method
                
            elif choice == 3: #Operations
                number1 = float(input("Please enter a number.")) #floats used to allow for a wider scope of numbers and calculations
                number2 = float(input("Please enter another number."))
                operation = input("Next you need to enter an operation. Your options are addition(a), subtraction(s), multiplication(m), division(d), please enter one:")
                print(f"\nThe answer using your desired operation is {user.PerformOperations(number1,number2,operation):.2f}") #implement method using fstring print
                
            elif choice == 4: #Squaring Numbers
                number = float(input("Please enter the number you would like squared:"))
                
                if number > 0: #if number is not negative or zero(as root would be imaginary or just 0), implement the method
                    print(f"The answer is {user.SquareNumber(number):.2f}")
                else:
                    print("Invalid response, cannot square a negative number or zero!")
                
            elif choice == 5: #Factorial
                number = int(input("Please enter an integer, this program will find its factorial:"))
                print(f"The factorial is {user.Factorial(number)}") #implement method
                
            elif choice == 6: #Counting
                start = int(input("Please enter the starting number:"))
                end = int(input("Please enter the ending number:"))
                print(f"\nStarting from {start} and ending at {end}, your count is {user.Counting(start,end)}") #implement method
                
            elif choice == 7: #Computing Hypotenuse
                base = float(input("Please enter the value of the base of the right-angle triangle:"))
                perpendicular = float(input("Please enter the value of the perpendicular of the right-angle triangle:"))
                print(f" The value of the Hypotenuse is {user.calculateHypothesis(base,perpendicular):.2f}") #implement method
                
            elif choice == 8: #AreaRectangle
                width = float(input("Please enter the width of the rectangle:"))
                length = float(input("Please enter the length of the rectangle:"))
                print(f"The area of the rectangle is {user.RectangleArea(width,length):.2f}") #implement method
                
            elif choice == 9: #Power
                base = float(input("Please enter the base number:"))
                exponent = float(input("Please enter the exponent number:"))
                print(f"The power based on a base of {base} and an exponent of {exponent} is {user.PowerNumber(base,exponent):.2f}") #implement method
                
            elif choice == 10: #ArgumentType
                argument = input("Please enter any variable, the type will be returned:")
                print(f"The type is {user.ArgumentType(argument)}") #implement method
                
            else: #if none of the numbers are selected
                print("INVALID RESPONSE") 

        elif answer == 'N': #if N is chosen rather than Y
            print("Rude.")  
            
        else: #if neither N nor Y is chosen
            print("Invalid Answer!!!!")
        
        #attached to the while statement, if the user indicated N, the program stops
        response = input("Would you like to try another task? Yes(Y) or No(N)?")   
        

class BasicMathOperations:
    
    @staticmethod #allows the methods to pull from the class without modifying an object or instance
    def GreetUser(first_name, last_name):
        print(f"Hello {first_name} {last_name}, welcome to Assignment 05!")

    @staticmethod
    def AddNumbers(number1, number2):
        num_sum = number1 + number2
        print(f"The sum of {number1} and {number2} is {num_sum}.")

    @staticmethod
    def PerformOperations(num1, num2, operator): #if the user inputs associated letter, operation runs
        if num1 < num2:
            num1, num2 = num2, num1
        if operator == 'd' and num2 != 0: #only calcultes the quotient if the denominator is not zero
            quotient = num1 / num2
            return quotient
        elif operator == 'm':
            product = num1 * num2
            return product
        elif operator == 'a':
            num_sum = num1 + num2
            return num_sum
        elif operator == 's':
            difference = num1 - num2
            return difference
        else: #if none of the letters are entered, error message is printed
            return "Invalid response." 
            
    @staticmethod
    def SquareNumber(number):
        answer = number**2
        return answer 

    @staticmethod
    def Factorial(number):
        for i in range(1, number): #for loop to find factorial for an input number
            number = number * i
        return number

    @staticmethod
    def Counting(start_number, end_number):
        count_list = list(range(start_number, end_number + 1)) #end number + 1 to include the end number in the range
        return count_list

    @staticmethod
    def calculateHypotenuse(base, perpendicular):
        def calculateSquare(number): #method inside the hypotenuse method so it can be used within
            return number ** 2

        square_base = calculateSquare(base)
        square_perp = calculateSquare(perpendicular)
        square_hypo = square_base + square_perp
        hypo = (square_hypo)**0.5
        return hypo

    @staticmethod
    def RectangleArea(width, length):
        area = width * length
        return area

    @staticmethod
    def PowerNumber(base, exponent): #taking a base and exponent and finding the value (power) 
        power = base ** exponent
        return power

    @staticmethod
    def ArgumentType(argument):
        arg = type(argument) #using the built-in type function to find the type of an argument
        return arg
    
    
main()  #invoke main