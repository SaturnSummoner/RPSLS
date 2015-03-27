#Rock-paper-scissors-lizard-Spock

# helper functions
def name_to_number(name):
    if (name) =="rock":
            number=0
    elif (name)=="Spock":
            number=1
    elif (name)=="paper":
            number=2
    elif (name)=="lizard":
            number=3
    elif (name)=="scissors":
            number=4
    else:
         print "Please enter a valid option"   
    return number
    pass


def number_to_name(number):
    if number==0:
        name="rock"
    elif number==1:
        name="Spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        print "please enter a valid option"
    return name
    
    pass


def rpsls(player_choice): 
    print ""
    print "player chooses", (player_choice)
    import random 
    comp_choice=random.randrange(0,4)
    number_to_name(comp_choice)
    name_to_number(player_choice)
    cc=str (number_to_name(comp_choice))
    print "computer chooses", cc
    r=comp_choice-name_to_number(player_choice)
    result=r
    if r>0:
        result=r
    elif r==0:
        result=r
    elif r<0:
        result=r%5   
    else :
        return result
    pass
  
    if result==1:
        print "Computer wins!"
    elif result==2:
        print "Computer wins!"
    elif result==3:
        print "Player wins!"
    elif result==4:
        print "player wins!"
    elif result==0:
        print "player and computer tie!"
        
    else:
            return result
        
user=raw_input("choose your weapon")
weapon=str(user)
rpsls(weapon)
