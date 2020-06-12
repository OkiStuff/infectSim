
import time
import random

try:

    amount = int(input("Enter Amount of People infected per sick person: "))
    whole = int(input("Enter Amount of People in the World: ") )
    
except Exception:

    print("String Inputted instead of number")
    exit()
    


def infect(p, w):


    infected = 1
    timeSpent = 0
    daysSpent = 0

    print("\n PRESS CTRL+C TO QUIT")
    

    while True:
    
        addText = True
    
        time.sleep(.5)
        timeSpent += .5 
        
        addText = False
        
        try:
            daysSpent += 1
            print( "Day " + str(daysSpent) +", infected: " + str(infected) )
            if random.randint(0,3) != 0:
                infected = infected * p
                
            else:
            
                pass
                
            
            
            
            
            if infected >= w:
            
       
                print("Took " + str(timeSpent) + " seconds to get everyone sick")
                print("The World Survived for " + str(daysSpent) + " days")
                
                break
            
        except Exception:
        
            print("shutting down..")
            time.sleep(1)
            
    exit()
        
    
infect(amount, whole)