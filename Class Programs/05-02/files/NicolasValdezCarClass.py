# Programming Exercise 10-1

import Car

def main():
    myCar=Car.Car("2020 Toyota","Tundra")
    n=5
    # Accelerate the car
    for i in range(n):
        myCar.accelerate()
        speed=myCar.get_speed()
        print(f"Speed: {speed}")
        
    # Brake the car
    for i in range(n):
        myCar.brake()
        speed=myCar.get_speed()
        print(f"Speed: {speed}")

# Call the main function.
if __name__ == '__main__':
    main()
