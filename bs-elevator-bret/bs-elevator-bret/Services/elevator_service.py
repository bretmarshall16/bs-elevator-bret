import sys

end_program_string = "END"


def setup_elevator_service():
    print(f"Elevator service started, at any time you can enter {end_program_string} to exit the program")
    
    valid_floors = False

    while not valid_floors:
    
        print("How many floors should this elevator service?")
   
        number_of_floors = input()
        valid_floors = execute_function(validate_number_of_floors, number_of_floors)

    print(f"Elevator create with {number_of_floors} floors")

def run_elevator(elevator):
    print("Running elevator service...")


def validate_number_of_floors(number_of_floors_input_string): 
    try:
        number_of_floors = int(number_of_floors_input_string)
    except:
        print("Invalid input for floors, value must be a positive integer")
        return False
    else:
        if number_of_floors < 1:
            print("Invalid input for floors, value must be a positive integer")
            return False
        else:
            return True

def evluate_if_input_is_end_program_string(input):
    if input == end_program_string:
        return True
    else:
        return False

def execute_function(func, input):
    if evluate_if_input_is_end_program_string(input):
        print("Exiting program")
        print("------------------------------------------------------------")
        sys.exit()
    else: 
        return func(input)