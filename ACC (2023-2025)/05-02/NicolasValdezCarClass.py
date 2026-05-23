# Nicolas Valdez Sat May  3 12:15:21 2025
# NicolasValdezCarClass
# Accelerate and slow down a car object
# Input(s)
# N/A
# Output
# Speed of a car after acceleration and slow down
# Acceleration = Speed + 5
# Brake = Speed - 5

import Car

# Welcoming Statement
print("View the speed of a car after accelerating and braking.")

def main():
    myCar=Car.Car("2020 Toyota","Tundra")
    n=5
    # Accelerate the car
    for i in range(n):
        myCar.accelerate()
        speed=myCar.get_speed()
        print(f"Speed after acceleration: {speed}")
        
    # Brake the car
    for i in range(n):
        myCar.brake()
        speed=myCar.get_speed()
        print(f"Speed after braking: {speed}")
    
# Call the main function.
if __name__ == '__main__':
    main()

# Ending Note
print("Program Ends")