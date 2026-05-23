# Programming Exercise 10-1

import pet

def main():
    # Local variables
    pet_name = ""
    pet_type = ""
    pet_age = 0
    
    # Get pet data.
    pet_name = input('Enter the name of the pet: ')
    pet_type = input('Enter the type of animal: ')
    pet_age = int(input('Enter the age of the pet: '))

    # Create an instance of Pet.
    mypet = pet.Pet(pet_name, pet_type, pet_age)

    # Display the data that was entered.
    print ('Here is the data that you entered: ')
    print (f'Pet name: {mypet.get_name()}')
    print (f'Animal type: {mypet.get_animal_type()}')
    print (f'Age of pet: {mypet.get_age()}')

# Call the main function.
if __name__ == '__main__':
    main()