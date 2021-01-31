from sys import exit
 
import re
import string
import time
name = re.compile(r'[a-zA-Z]+')
Aname = re.compile(r'[A-Z]+')












                                                        #BAT ROOM#
#--------------------------------------------------------------------------------------------------------------------------------------------------#    


def Bat_Room():
    print "\n"
    print "You open the rather ordinary looking Redwood door"
    print "You give it a push and it bursts OPEN"
    print "\n"
    print "And they came swarming out of  it"
    print "Hundreds and Thousands of them"
    print "\n"
    print "The Swarm of the most Blood Thirsty BATS there are"
    print "And they are coming right at you"
    print "With their sharp Fangs"
    print "You got a split second decision to make"
    print "\n"
    print "You can either :-"
    print "                  (a)Wait For Them To Pass"    
    print "                  (b)Close The Door Shut"   
    print "\n"
    
    Reflex = raw_input("What will you do? >")

    if Reflex == "CLOSE THE DOOR" or Reflex == "CLOSE DOOR" or Reflex == "b" or Reflex =="B" or Reflex == "2" or Reflex == "CLOSE THE DOOR SHUT":
        print "\n"
        print "Good Choice"
        print "You Shut The Door and Escaoe with minor cuts"
        print "It could've been lot worse :| "
        print "\n"
        print "I'd advise you to Start Exploring Other Options " 
        print "\n"
        
        
        print  "(1) East Door "
        print  "(2) North Door"
        print  "(3) West Door "
    
        action= raw_input(">")

        if  action == "EAST DOOR" or action == "a" or action == "1":
            print " You Push the black wooden Oak Door with surprisingly clean front a push it doesnt budge "
            print " You ram your body on the door it bursts open...... inside"
            print "\n"
                              
            return    Elephant_Room()



        elif action == "WEST DOOR" or action == "c" or action == "3":
            print "Well it seems like you want your Ass Kicked"
            print "You Open the Door Again with the intention of getting your Ass Kicked"
            print "But what's waiting at the other end is Far Far worse"
            print "\n"
            print "They come for your face with everything the've got"
            print "You run for your life but its too late"
            print "\n"
            print "They catch up to you EAT YOUR BRAINS OUT"
            print "Wait.....YOU NEVER HAD ANY"
            return dead()

            

        elif action == "NORTH DOOR" or action == "b" or action == "2":
            print "This Door looks extremely Robust and Sturdy with a Thick Iron Plate" 
            print "It looks like it can easily withstand a Cannon Strike"
            print "Lucky for you, it's Unlocked!"
            print "\n \n"
            return Lava_Room()



        else:
            print "You slip on the Floor, Bang your head and never see Light again"
            return dead()  


    elif Reflex == "WAIT FOR THEM TO PASS" or Reflex == "LET THEM PASS" or Reflex == "LET THEM FLY" or Reflex == "a":
        print "\n"
        print "Seriously!! It's a close corridor from which you're trying to Get Out"
        print "Where the Hell are the Damn Bats gonna fly?"
        return dead("THEY EAT YOUR BRAINS OUT")


    else:
        print "\n"
        print "I don't know what that means "
        print "You're back where you were"
        return Bat_Room()        
    

#--------------------------------------------------------------------------------------------------------------------------------------------------#    








                                                  # LAVA ROOM#
#---------------------------------------------------------------------------------------------------------------------------------------------------#

def Lava_Room():
    print " You open the North Door with a good powerful push"
    print " It opens up in a Room that without any doubt is BAD NEWS"
    print ##
    print "It opens up in Room Full Of LAVA"
    print "The lava is rising like a Shaken Champagne "
    print "What will you do?"
    print "Flee or Confront"
    print "\n \n"

    Choice = raw_input(">")

    if Choice == "FLEE" or Choice == "Flee" or Choice == "GO BACK" or Choice == "GET OUT":
        print "\n"
        print " You act fast and get out of that room and close the large Door Behind You"
        print " Now you finally know what it was  for :)"
        print " Good Choice!"
        print "\n \n"



        print  "(1) East Door "
        print  "(2) North Door"
        print  "(3) West Door "
        print "\n"
    
        action= raw_input(">")

        if action == "EAST DOOR" or action == "a" or action == "1":
            print " You Push the black wooden Oak Door with surprisingly clean front a push it doesnt budge "
            print " You ram your body on the door it bursts open...... inside"
            print "\n"
                              
            return    Elephant_Room()



        elif action == "WEST DOOR" or action == "c" or action == "3":

            return Bat_Room()

        elif action == "NORTH DOOR" or action == "b" or action == "2":
            print " Looks like you got a death wish"
            print " You open the large chamber door once again  and enter"
            print " The Moment you step in you regret your decision"
            print " But now its too late...The lava rises beyond mercy and takes you with it"
            return dead("I've got no idea why you went inside again!") 


        else:
            print "I Think Lava got into your head"
            return dead()



        
            

    elif Choice == "CONFRONT" or Choice == "FIGHT THE FIRE" or Choice == "FIGHT FIRE":
        print "Seriously....I dont even wanna talk about it"
        return dead("Really!! Who do you think you are AQUAMAN!!")

    else:
        print "I've got no idea what that means"
        print "You're Back where you started"
        print "\n"
        return Lava_Room()
    




#---------------------------------------------------------------------------------------------------------------------------------------------------#
































                                                           #DOORS#
#---------------------------------------------------------------------------------------------------------------------------------------------------#
def Doors():
    print  "(1) East Door "
    print  "(2) North Door"
    print  "(3) West Door "
    print  "\n"
    action = raw_input(">")

    if action == "EAST DOOR" or action == "a" or action == "1":
        print "\n"
        print " You give the Black Wooden Oak Door with surprisingly clean face a Push, it  doesnt budge "
        print " You ram your body on the door it bursts open...... inside"
        print "\n"
                              
        return    Elephant_Room()



    elif action == "WEST DOOR" or action == "c" or action == "3":

        return Bat_Room()

    elif action == "NORTH DOOR" or action == "b" or action == "2":
        print "This Door looks extremely Robust and Sturdy with a Thick Iron Plate" 
        print "It looks like it can easily withstand a Cannon Strike"
        print "Lucky for you, it's Unlocked!"
        print "\n \n"
        return Lava_Room()



    else:
        print "You slip on the Floor, Bang your head and never see Light again"
        return dead()  

#---------------------------------------------------------------------------------------------------------------------------------------------------#








                                                
                                                        #DEAD#
#--------------------------------------------------------------------------------------------------------------------------------------------------#    

def dead(why):
    print "Your Dead!!", why , "Great Job NutHead!"

#---------------------------------------------------------------------------------------------------------------------------------------------------#
















                                                     #FREEDOM#
#---------------------------------------------------------------------------------------------------------------------------------------------------#


def Freedom():
     print " You crawl out in a beautiful plain, with Lush Green Trees and Blue Clear Sky....And NO sign of any Mysterious Castle is Visible"
     print " You see a swarm of people coming your way but just as you're about to embrace them"
     print " You hear a voice ....A STRANGE ....A FAMILIAR VOICE ....IT'S SHOUTING SOMETHING ....SOMETHING FAMILIAR"
     print " IT'S SHOUTING "
     print "\n"
   

     Guess = raw_input("Can you guess what it's saying?")

     if name.match(Guess):  
     
        while True:
            print "  IT SAYS WAKE UP  "
            time.sleep(2)

     else:
        print "\n"
        print "Learn to type words"
        return dead()
        
        
#--------------------------------------------------------------------------------------------------------------------------------------------------#    















                                                         #MIRROR ROOM#       
#--------------------------------------------------------------------------------------------------------------------------------------------------#    

def Mirror_Room():

    print " Well you can officialy call yourself a Beast Slayer now....But It isn't over yet, you still have to get out of this HELLHOLE"
    print " \n \n \n"
    print " This room not unlike the other DARK Rooms, ... except you can see a ray of light entering through a crack along with the occasional"
    print " breeze of wind telling you that you are not far from your way out"
    print "\n"
    print " You focus your mind in finding a clue that will help you find your way out"
    print " This Room unlike others has no doors other than that one you came from"
    print " You try to find your way around but there are nothing but walls to the naked eye"
    print " \n"
    print " You can either LOOK AROUND FOR CLUES or LOOK AROUND FOR CLUES :)"

   
    
    Your_Choice = raw_input(">")

    if Your_Choice == "LOOK AROUND" or Your_Choice == "LOOK AROUND FOR CLUES": 
       print " Good choice it must've been difficult" 
   

    else:
       print " That's not an option"
       return dead("Learn to listen Mr.Smarty Pants")        
    print "\n \n"
    print " You Look Around and find a Metal Stand"
    print " On that Metal stand is peculiar round thing covered with Dust and Cobwebs"
    print "\n "
    print " You clean the dirt and the Round thing turns out to be a Reflective Mirror "
    print " What will you do with it?"
    print "\n \n"

    Your_Action = raw_input(">")

    if Your_Action == "ALIGN WITH THE LIGHT" or Your_Action == "REFLECT RAY" or Your_Action == "ALIGN WITH THE RAY":    
        print " Well done Mr.Brainiac you got some Brains"
        print " You align the Mirror with the ray of light"
        print " The Mirror reflects it and scatters the ray onto 4 other similar mirrors fixed on the four corners of the ceiling to light the entire room"
        print " The Ray from those mirror converges on a single point .....A TRAPDOOR"
        print " You Open the door and crawl your way out of that Shit...Back in the world where you are not only Gold Rich "
        print " But are now THE GREATEST ADVENTURER"
        print ###
        print "\n"
        print "\n"
        return Freedom() 

    elif Your_Action == "TEND TO YOUR HAIR" or Your_Action == "SEE FACE":
        print "Yep you're a looker but that won't help you now"
        print "Cause The mirror is no ordinary mirror ....Its The Mirror of Erised"
        print "You Waste your life staring at it"
        return dead("Use your Brains next time")


    elif Your_Action == "LIGHT RAY" or Your_Action == "RAY OF LIGHT" or Your_Action == "RAY":
        print "So close yet so Far"
        return dead("Right Track just stick to it")  

    else:
        print "\n"
        print "Happiness Can Be Found In The Darkest Of Times"
        print "If One Only Remembers To Turn On The LIGHT"
        return dead("Figure that out") 
        
#--------------------------------------------------------------------------------------------------------------------------------------------------#    
























                                                          #TREASURE ROOM#      

#--------------------------------------------------------------------------------------------------------------------------------------------------#    

def Treasure_Room():
    print " You having found a way to counter the Gigantic Beast in the other room now enter a whole new world"
    print " Unlike you're expectations of dim and obstitue room this one is the last thing you would've hoped"
    print "\n"
    print " This room has no beasts no darkness but Glory, Pure and Absolute scene to the eye you are witness to something that you had "
    print " never ever seen in your life...And probably never will"
    print " \n "
    print " You are in a GOLD ROOM! "
    print " Not just a gold room ...THE GOLD ROOM..were not only the one of the most priced and valuable possesions of the entire Globe are kept"
    print " But also the entire room has been blooming with the light of golden reflection coming from one single ray of light making its way through"
    print " a tiny crack in the ceiling"
    print "\n"
    print " The Mere sight brings a grin to your face"
    print " And if you care you see a door about a 1000 feet away from where you are...Which leads to some other DARK ROOM"
    print " \n \n \n "
    print " You can  just leave the room and continue on the quest or just smuggle some gold with you on your way out"

    action = raw_input(">")

    if action == "TAKE GOLD" or action == "TAKE SOME" or action == "SMUGGLE":
        print " So youre not so selfless afterall ...how much do you wanna take?"

        amount = raw_input(">")

        if "0" in amount or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in amount:  
            how_much = int(amount)   # THis function is not clear yet
        else: 
            dead("Man, learn to type a number.")

        if how_much < 50:
            print " Nice, you're not greedy...You take the gold and minding the giant dozed off elephant behind,"
            print " Slowly make your way to the other Room" 
            return Mirror_Room()



        else:
         dead(" YOu greedy bastard, The Elephant wakes from the sound of the metal you try to run but t'was too late!") 
         exit()
              
          
    elif action == "LEAVE":

        print " Well Well you really are self restrained ..YOu sure you dont wanna take anything from this Golden Xanadu?"

        answer = raw_input(">")

        if "YES" in answer:
            print " Well if you're sure then head right out there's an open black wood door and another DARK ROOM waiting for you"
            return Mirror_Room()

        elif "NO" in answer:
            print " So changed your mind? How much do you want?"
            how_many = raw_input("Number of Gold ")
            estimate = int(how_many)

            if estimate < 50:
                print " Nice, you're not greedy. .You take the gold and minding the giant dozed off elephant behind slowly make your way to the other room!"
                return Mirror_Room
             
            
            

        else:
            print "Too Late, your presence in the room extended beyond the limit waking up the giant beast beside you, He crushes you like an ant"
            return dead()

    else:
        print " I've got no idea what that means "
        print " You're back where you started"
        return Treasure_Room()            

             
            
       
    
#--------------------------------------------------------------------------------------------------------------------------------------------------#    























                                                    #ELEPHANT ROOM#                                
#--------------------------------------------------------------------------------------------------------------------------------------------------#    


def Elephant_Room():
    print "You open the East Door by raming through the door,"
    print "Inside the Dark and Isolated Room the visibility is all but," 
    print "None still a Small Iron Door is visible on the other end of this apparently Long Hall," 
    print "\n" 
    print "you start pacing forward when you notice a slight wrinkle in the long thread of silence,"
    print "You turn to check the source of the noise when you see it...."
    print "\n"
    print "A Great White Elephant coming your way with the sole intention of Thrashing you on the wall,"
    print "The  intensity of the elephant's march is so Demoraliizing that it even questions this ones vegetarian Diet :)"
    print "\n"
    print "With having already lost  precious time to react to the ramming Mammal heading your way"
    print "you must react quickly for you are nothing more than a TOOTHPICK for this MAMMOTH to break"             
  
    print "\n \n"

    action = raw_input(">")

    if action == "DODGE ELEPHANT" or action == "a" or action == "DODGE MAMMOTH":
        print "\n \n "
        print " The Elephant comes to close to you but you jump out of its way..."
        print " It keeps on running and crashes into the iron door bursitng it open"
        print " The ELephant passes out but you get the chance to get the hell away from that creature"
        print "\n \n"
        return  Treasure_Room()
    
    elif "FIGHT" in action or " FIGHT ELEPHANT" in action:
         print " Really, I've got a Mouse who's better at this than you,"
         print " You know why ...BECAUSE IT'S STILL DAMN WALKING "
         return  dead('The Elephant hits you like a Coal Engine you die an Agonising death')

    else:
        print " Seirously there's a 2000 pound cannonball of flesh coming your way and you think of this :( "

        return dead()            
    

#--------------------------------------------------------------------------------------------------------------------------------------------------#    










                                                      #CORRIDOR#

#--------------------------------------------------------------------------------------------------------------------------------------------------#    


def Corridor():
    print "\n"
    print  " You're in a Dark and Abandoned Corridor"
    print  " Your Objective is to get the Hell out of this Godforsaken place" 
    print  " \n"
    print  " There is a sealed window right ahead through which you get a slight" 
    print  " Glimpse of the Rising Sun "
    print  " But Make no mistake the Building is so conceiled "
    print  " That not even a sliver of light is entering"
    print  "\n"
    print  " The East is in your lLeft as you conclude from your apparent observation"
    print  " You turn back and start pacing straight to find a exit "
    print  " You have three doors in your sight"
    print  " \n"
    print  " [TYPE UPPER CASE AT ALL TIMES...MY HEARING'S A BIT WEAK :)]"
    print  "\n"
    

    Hear = raw_input("TYPE ANY UPPERCASE LETTER TO BEGIN !")
    
    if Aname.match(Hear):
        print "\n"
        print "Good"
        return Doors()

    else:
       
       return dead("Learn to Listen Dumass")
#--------------------------------------------------------------------------------------------------------------------------------------------------#    


  



















        
Corridor()



