import random



class Game():

    def guesing(self):
        difficulty = int(input('First choise game difficulty\n1.Easy\n2.Medium\n3.Hard\nYour choise: '))

        if difficulty == 1:
            counter = 10
            print('Great! You have selected the Medium difficulty level and you have 10 guesses')
            while True:
                guess = int(input('Enter you choise: '))
                generator = random.randrange(100)
                if guess > generator:
                    counter -=1
                    if counter != 0:
                        if counter == 1:
                            print(f'[You number is greater than our number {generator}\nNow you have {counter} more guess]')
                        else:    
                            print(f'[You number is greater than our number {generator}\nNow you have {counter} more guesses]')
                    else:
                        print('**The End***')    
                        break
                      

                elif guess < generator:   
                    counter -=1
                    if counter != 0:
                        print(f'[You number is less than our number {generator}\nNow you have {counter} more guesses]')  
                    else:
                        print('**The End***')    
                        break    

                elif guess == generator:
                    print('Congrats you win!')    





        elif difficulty == 2:
            counter = 5
            generator = random.randrange(100) 
            print('Great! You have selected the Medium difficulty level and you have 5 guesses')
            while True:
                guess = int(input('Enter you choise: '))
                generator = random.randrange(100)
                if guess > generator:
                    if counter != 0:
                        if counter == 1:
                            print(f'[You number is greater than our number {generator}\nNow you have {counter} more guess]')
                        else:    
                            print(f'[You number is greater than our number {generator}\nNow you have {counter} more guesses]')
                    else:
                        print('**The End***')    
                        break
                      

                elif guess < generator:   
                    counter -=1
                    if counter != 0:
                        if counter == 1:
                            print(f'[You number is less than our number {generator}\nNow you have {counter} more guess]')
                        else:    
                            print(f'[You number is less than our number {generator}\nNow you have {counter} more guesses]')
                    else:
                        print('**The End***')    
                        break    

                elif guess == generator:
                    print('Congrats you win!')       



        elif difficulty == 3:      
            counter = 3
            print('Great! You have selected the Medium difficulty level and you have 3 guesses')  
            while True:
                guess = int(input('Enter you choise: '))
                generator = random.randrange(100)
                if guess > generator:
                    counter -=1
                    if counter != 0:
                        if counter == 1:
                            print(f'[You number is greater than our number {generator}\nNow you have {counter} more guess]')
                        else:    
                            print(f'[You number is greater than our number {generator}\nNow you have {counter} more guesses]')
                    else:
                        print('**The End***')    
                        break
                      

                elif guess < generator:   
                    counter -=1
                    if counter != 0:
                        if counter == 1:
                            print(f'[You number is less than our number {generator}\nNow you have {counter} more guess]')
                        else:    
                            print(f'[You number is less than our number {generator}\nNow you have {counter} more guesses]')  
                    else:
                        print('**The End***')    
                        break    

                elif guess == generator:
                    print('Congrats you win!')                 

  
        

    def main(self):
        game = Game()
        print('Welcome to the Number Guessing Game!')
        print('1. Start Game')
        print('2. End Game')
        choise = int(input('Enter you choise: '))
        while True:
            if choise == 1:
                game.guesing()
            elif choise ==2:
                break
            else:
                print('Sorry we dont have that option. Please try again!')
            




if __name__ =='__main__': 
    activate = Game()
    start = activate.main()
    

