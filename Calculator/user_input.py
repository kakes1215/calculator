from calculator import Calculator as Calc


class User_Input():

    def get_input(self):
        expression = input("Enter an problem: ")

        result = Calc().handle_expression(expression)

        print("Result: " + str(result))
