#Assignment 05
def main():
    user = BasicMathOperations()
    response = 0
    answer = input("Hello! Welcome to Python, I have a set of questions and operations to share with you, do you want to hear them? Please enter Y for yes and N for no:")
    
    while response != 'N': 
        if answer == 'Y':
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
            
            if choice == 1:
                firstname = input("Please enter your first name:")
                lastname = input("Please enter your last name:")
                user.GreetUser(firstname,lastname)
                
            elif choice == 2:
                number1 = float(input("Please enter a number:"))
                number2 = float(input("Please enter another number:"))
                user.AddNumbers(number1,number2)
                
            elif choice == 3:
                number1 = float(input("Please enter a number."))
                number2 = float(input("Please enter another number."))
                operation = input("Next you need to enter an operation. Your options are addition(a), subtraction(s), multiplication(m), division(d), please enter one:")
                print(f"\nThe answer using your desired operation is {user.PerformOperations(number1,number2,operation):.2f}")
                
            elif choice == 4:
                number = float(input("Please enter the number you would like squared:"))
                if number > 0:
                    print(f"The answer is {user.SquareNumber(number):.2f}")
                else:
                    print("Invalid response, cannot square a negative number or zero!")
                
            elif choice == 5:
                number = int(input("Please enter an integer, this program will find its factorial:"))
                print(f"The factorial is {user.Factorial(number)}")
                
            elif choice == 6:
                start = int(input("Please enter the starting number:"))
                end = int(input("Please enter the ending number:"))
                print(f"\nStarting from {start} and ending at {end}, your count is {user.Counting(start,end)}")
                
            elif choice == 7:
                base = float(input("Please enter the value of the base of the right-angle triangle:"))
                perpendicular = float(input("Please enter the value of the perpendicular of the right-angle triangle:"))
                print(f" The value of the Hypotenuse is {user.calculateHypothesis(base,perpendicular):.2f}")
                
            elif choice == 8:
                width = float(input("Please enter the width of the rectangle:"))
                length = float(input("Please enter the length of the rectangle:"))
                print(f"The area of the rectangle is {user.RectangleArea(width,length):.2f}")
                
            elif choice == 9:
                base = float(input("Please enter the base number:"))
                exponent = float(input("Please enter the exponent number:"))
                print(f"The power based on a base of {base} and an exponent of {exponent} is {user.PowerNumber(base,exponent):.2f}")
                
            elif choice == 10:
                argument = input("Please enter any variable, the type will be returned:")
                print(f"The type is {user.ArgumentType(argument)}")
                
            else:
                print("INVALID RESPONSE")

        elif answer == 'N':
            print("Rude.")  
        else:
            print("Invalid Answer!!!!")
            
        response = input("Would you like to try another task? Yes(Y) or No(N)?")   
        

class BasicMathOperations:
    
    @staticmethod
    def GreetUser(first_name, last_name):
        print(f"Hello {first_name} {last_name}, welcome to Assignment 05!")

    @staticmethod
    def AddNumbers(number1, number2):
        num_sum = number1 + number2
        print(f"The sum of {number1} and {number2} is {num_sum}.")

    @staticmethod
    def PerformOperations(num1, num2, operator):
        if num1 < num2:
            num1, num2 = num2, num1
        if operator == 'd' and num2 != 0:
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

    @staticmethod
    def SquareNumber(number):
        answer = number**0.5
        return answer

    @staticmethod
    def Factorial(number):
        for i in range(1, number + 1):
            number = number * i
        return number

    @staticmethod
    def Counting(start_number, end_number):
        count_list = list(range(start_number, end_number + 1))
        return count_list

    @staticmethod
    def calculateHypotenuse(base, perpendicular):
        def calculateSquare(number):
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
    def PowerNumber(base, exponent):
        power = base ** exponent
        return power

    @staticmethod
    def ArgumentType(argument):
        arg = type(argument)
        return arg
    
    
main()        