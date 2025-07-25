from math import e
import sys
import time
from tkinter import N

end_program_string = "END"
seconds_per_floor = 1

class Elevator:
    def __init__(self):
        self.number_of_floors = 0
        self.current_floor = 1

    #PUBLIC FUNCTIONS
    def setup_elevator_service(self):
        print(f"Elevator service started, at any time you can enter {end_program_string} to exit the program")
    
        valid_floors = False

        while not valid_floors:
    
            print("How many floors should this elevator service?")
   
            self.number_of_floors = input()
            valid_floors = self._execute_function(self._validate_number_of_floors, self.number_of_floors)


    def run_evevator_service(self):
        print(f"Elevator is running with {self.number_of_floors} floors.")
        print(f"Current floor: {self.current_floor}")
        
        while True:
            valid_calling_floor = False
            while not valid_calling_floor:
                print("What floor are you calling from?")
                calling_floor = input()
                valid_calling_floor = self._execute_function(self.move_to_floor, calling_floor)
            
            valid_moving_floor = False
            while not valid_moving_floor:
                print("What floor are you moving to?")
                moving_floor = input();
                valid_moving_floor = self._execute_function(self.move_to_floor, moving_floor)
    
            
    def move_to_floor(self, input_floor_str):
        input_floor = self._execute_function(self._validate_move_to_floor_input, input_floor_str)
        if(input_floor != False):
            step = 1 if self.current_floor < input_floor else -1
            for x in range(self.current_floor+step, input_floor+step, step):
                print(f"Ding! Elevator on floor {x}")
                self.current_floor = x
                time.sleep(seconds_per_floor)

            print(f"The elevator has arrived to your desired floor: {input_floor}")
            return True
        else:
            return False

    #END PUBLIC FUNCTIONS

    #PRIVATE FUNCTIONS

    def _validate_number_of_floors(self, number_of_floors_input_string): 
        invalid_message = "Invalid input for floors, value must be an integer greater than 1"

        try:
            self.number_of_floors = int(number_of_floors_input_string)

        except:
            print(invalid_message)
            return False
        else:
            if self.number_of_floors < 2:
                print(invalid_message)
                return False
            else:
                return True

    def _validate_move_to_floor_input(self, input_floor_str):
        invalid_message = f"Invalid input for floors, value must be a integer between 1 and {self.number_of_floors}"

        try:
            input_floor = int(input_floor_str)
        except:
            print(invalid_message)
            return False
        else:
            if input_floor < 1 or input_floor > self.number_of_floors:
                print(invalid_message)
                return False
            else:
                return input_floor

    def _evaluate_if_input_is_end_program_string(self, input):
        if input == end_program_string:
            return True
        else:
            return False

    def _execute_function(self, func, input):
        if self._evaluate_if_input_is_end_program_string(input):
            print("Exiting program")
            print("------------------------------------------------------------")
            sys.exit()
        else: 
            return func(input)
    #END PRIVATE FUNCTIONS
        
        
    
