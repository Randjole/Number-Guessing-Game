import random



class Game():

    print('Welcome to the Number Guessing Game!')
    def guesing(self):
        difficulty = int(input('First choise game difficulty\n1.Easy\n2.Medium\n3.Hard\nYour chouse: '))

        if difficulty == 1:
            counter = 5

            guess = int(input('Great now is time to guess number\nEnter you choise: '))
            generator = random.randrange(100)
            if guess > generator:
                counter -=1
                print(f'You number is greater than our number {generator}\nNow you have {counter} more guess')

            elif guess < generator:   
                counter -=1
                print(f'You number is less than our number {generator}\nNow you have {counter} more guess')  

            elif guess == generator:
                print('Congrats you guess the number!')    





        elif difficulty == 2:
            generator = random.randrange(100)    



        elif difficulty == 3:
            generator = random.randrange(100)    

  
        



























if __name__ =='__main__': 
    activate = Game()
    main = activate.guesing()
    

