import random





counter = 5
while True:
    x = input('y,u,i: ')
    if x == 'y':
        counter -=1
        if counter == 0:
            break
        print(counter)
        
