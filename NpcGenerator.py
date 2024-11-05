# Imports the operating system to create the func "clear()" that will be defined later & delete the output file on start
from os import system, name
import os
import sys
import random

# Predefinding variables & arrays
Npcs = []

FNames = ["Amelia", "Ava", "Emma", "Isabella", "Olivia", "Sophia", "Mia", "Evelyn", "Luna", "Susan"]
MNames = ["Ben", "Caiden", "David", "Hans", "Hubert", "Joe", "Liam", "Nathan", "Oliver", "Zack"]

# Last name lists because I felt like it and also for the Ethnicity Factor
Slavic = [" Aleshkovsky", " Melnyk", " Smirnov", " Vutechich", " Nowak"]
Germanic = [ " Fischer", " Hoffmann", " Müller", " Schmidt", " Schulz"]
Latin  = [" Dubois", " Hernandez", " Martinez", " Romano", " Silva"]
Anglic = [" Adams", " Baker", " Brown", " Smith", " Walker"]
Celtic = [" Brady", " Campbell", " Murphy", " O\'Connor", " Williams"]
# Afro-American last names are the same as Anglic last names
WestAfrican = [" Abara", " Djibo", " Kone", " Moukoko", " Yacouba"]
MediAfrican = [" Aït", "Fifi", " Jomana", " Ouyahia", " Zammit"]
EastAfrican = [" Dawit", "Elmi", " Otieno", " Tesfaye", " Raphael"]
SouthAfrican = [" Fourie", " Maluleke", "Nkosi", " Xulu", " Zuma"]
CentralAfrican = [" Ikia", " Ogedegbe", " Osman", " Tchicaya", " Rasaki"]
Sino = [" Chen", " Nguyễn", " Sakanoue", " Yang", " Zhang"]
SoutheasternAsian = [" Chan", " Phan", " Thongdee", " Vongphakdy", ""]
NativeAmerican = [" Curnutt", " Goseyun", " Huancahuari", " Pech", " Xiu"]
SouthIndian = [" Aiyengar", " Iyer", " Pillai", " Rao", " Vishwakarma"]
NorthIndian = [" Jha", " Kumar", "Patel", " Sharma", " Singh"]
Turkic = [" Özdemir", " Öztürk", " Şahin", " Yıldız", " Yılmaz"]
Tatar = [" Abaydullin", " Bashirov", " Turgenev", " Safin", " Yuldashev"]
Arabic = [" Abu", " Al", " Bin", " Bint", " Ibn"]
Polynesian = [" Akana", " Aukai", " Kaʻanāʻanā", " Kahale", " Kahananui"]

WealthRange = ["Poor", "Struggling", "Decent", "Middling", "Upper Middle Class", "Well Off", "Rich", "Elite"]

Done = False

# Deleting previous session
Output = open("output.txt", "w")
Output.close()

if os.path.exists("output.txt"): # checks if file exists to prevent errors
        os.remove("output.txt")

# Predefining Classes
class Npc:
    # The __init__ func lets you include paramaters that will perist in different objects of the class, but have different values
    def __init__(self, Name, Age, Gender, Wealth, IQ):
        self.Name = str(Name)
        self.Age = str(Age)
        self.Gender = str(Gender)
        self.Wealth = str(Wealth)
        self.IQ = str(IQ)

# Predefining Functions
def clear():
  # For windows
  if os.name == "nt":
        os.system("cls")
  # For mac and linux(here, os.name is 'posix')
  else:
        os.system("clear")

def NpcLibrary():

    MaleName = False
    FemaleName = False
    RanNpc = Npc(None, None, None, None, None) # If any input results in an error, RanNpc will return as a NoneType
    
    print("-----------------------------------------------------------\nIn order to randomly generate an NPC, you need to first answer 4 questions\n-----------------------------------------------------------")
    GenderFactor = input("What gender is the NPC (Answer \"Male\", \"Female\", or \"Croissant\"): ")
    AgeRangeMin = input("Enter an minimum age: ")
    AgeRangeMax = input("Enter a maximum age: ")
    EthnicityFactor = input("1- Slavic\n2- Germanic\n3- Latin\n4- Anglic\n5- Celtic\n6- Afro-American\n7- West African\n8- Mediterranean African\n9- East African\n10- Southern African\n11- Central African\n12- Sinosphere Asian\n13- Southeastern Asian\n14- American Indian (Native American)\n15- South Indian\n16- North Indian\n17- Turkic\n18- Tatar\n19- Arabic\n20- Polynesian\nEnter one of the numbers above to choose an ethnicity for the NPC: ")
    clear()

    # Gender code
    if GenderFactor.lower() == "male":
        RanNpc.Gender = "Male"
        RanNpc.Name = MNames[random.randint(0, 9)]
    elif GenderFactor.lower() == "female":
        RanNpc.Gender = "Female"
        RanNpc.Name = FNames[random.randint(0, 9)]
    elif GenderFactor.lower() == "croissant":
        return Npc("Monsieur Croissant", "999", "Croissant", "#1", "999")
    else:
        print("Input Error")
        return None

    # Long ethnicity code because I put too many ethnicities for inclusivite's sake
    if EthnicityFactor.isdigit() == False or int(EthnicityFactor) > 20 or int(EthnicityFactor) < 0:
        print("Input Error")
        return None
    else:
        EthnicityFactor = int(EthnicityFactor)
        if EthnicityFactor == 1:
            RanNpc.Name += Slavic[random.randint(0, 4)]
        elif EthnicityFactor == 2:
            RanNpc.Name += Germanic[random.randint(0, 4)]
        elif EthnicityFactor == 3:
            RanNpc.Name += Latin[random.randint(0, 4)]
        elif EthnicityFactor == 4:
            RanNpc.Name += Anglic[random.randint(0, 4)]
        elif EthnicityFactor == 5:
            RanNpc.Name += Celtic[random.randint(0, 4)]
        elif EthnicityFactor == 6:
            RanNpc.Name += Anglic[random.randint(0, 4)]
        elif EthnicityFactor == 7:
            RanNpc.Name += WestAfrican[random.randint(0, 4)]
        elif EthnicityFactor == 8:
            RanNpc.Name += MediAfrican[random.randint(0, 4)]
        elif EthnicityFactor == 9:
            RanNpc.Name += EastAfrican[random.randint(0, 4)]
        elif EthnicityFactor == 10:
            RanNpc.Name += SouthAfrican[random.randint(0, 4)]
        elif EthnicityFactor == 11:
            RanNpc.Name += CentralAfrican[random.randint(0, 4)]
        elif EthnicityFactor == 12:
            RanNpc.Name += Sino[random.randint(0, 4)]
        elif EthnicityFactor == 13:
            RanNpc.Name += SoutheasternAsian[random.randint(0, 4)]
        elif EthnicityFactor == 14:
            RanNpc.Name += NativeAmerican[random.randint(0, 4)]
        elif EthnicityFactor == 15:
            RanNpc.Name += SouthIndian[random.randint(0, 4)]
        elif EthnicityFactor == 16:
            RanNpc.Name += NorthIndian[random.randint(0, 4)]
        elif EthnicityFactor == 17:
            RanNpc.Name += Turkic[random.randint(0, 4)]
        elif EthnicityFactor == 18:
            RanNpc.Name += Tatar[random.randint(0, 4)]
        elif EthnicityFactor == 19:
            RanNpc.Name += Arabic[random.randint(0, 4)]
        elif EthnicityFactor == 20:
            RanNpc.Name += Polynesian[random.randint(0, 4)]
            
    # Age code
    if AgeRangeMin.isdigit() == True and AgeRangeMax.isdigit() == True:
        AgeRangeMin = int(AgeRangeMin)
        AgeRangeMax = int(AgeRangeMax)
        if AgeRangeMin < AgeRangeMax:
            RanNpc.Age = str(random.randint(AgeRangeMin, AgeRangeMax))
        elif AgeRangeMin > AgeRangeMax:
            RanNpc.Age = str(random.randint(AgeRangeMax, AgeRangeMin))
        else:
            RanNpc.Age = AgeRangeMin
    else:
        print("Input Error")
        return None

    # Finishes off the other paramters for the Npc class
    RanNpc.Wealth = WealthRange[random.randint(0,7)]
    RanNpc.IQ = str(random.randint(1, 200))

    # Returns the finished Npc
    return RanNpc
        

input("Welcome to the NPC Generator")
clear()
input("Here we are very pythonic and so are the NPCs generated")
clear()
NpcNum = input("How many NPCs do you want to generate? ")  # Number of NPCs
clear()


if NpcNum.isdigit() == False or int(NpcNum) <= 0:  # Checks is the inputted value is a eligible number of npcs
        print("Type a valid number next time butthead >:(")
        sys.exit()

for NpcAsgn in range(int(NpcNum)):

    Done = False  # Makes sure each instance gets to go through the while loop at least once

    while Done == False:

        NpcMethod = input("Would you like your Npc randomly generated? (Type \"yes\" for random generation and \"no\" for manual generation):")
        
        if NpcMethod.lower() == "yes":

            CurrentNpc = NpcLibrary()
            
        elif NpcMethod.lower() == "no":
            
            # Assigns the value of the class parameters based on inputs by the user
            CurrentNpc = Npc(input("What is the name of the NPC: "), input("What is the age of the NPC: "), input("What is the gender of the NPC: "), input("What is the wealth of the NPC: "), input("What is the IQ of the NPC: "))
            clear()

        else:
            continue

        if CurrentNpc == None:
            continue

            # Print statement uses the values stored inside an object in order to project them
        print("---------------------------------------------------------\nCURRENT NPC CHARACTERISTICS:\n\nNAME: " + CurrentNpc.Name + "\nAGE: " + CurrentNpc.Age + "\nGENDER: " + CurrentNpc.Gender + "\nWEALTH: " + CurrentNpc.Wealth + "\nIQ: " + CurrentNpc.IQ + "\n---------------------------------------------------------")
        Answer = input("Is this good? (Say \"yes\" to continue; or anything else to redo the editing of this NPC): ")
        clear()

        # Lets user exit out of the while loop when the current NPC is finished
        if Answer.lower() == "yes":
            Done = True

    Npcs.append(CurrentNpc) # Adds the finished NPC object to a list, where its value will be stored independent of the other objects despite having the same variable name

for NpcTar in range(int(NpcNum)):  # Goes through the code for each NPC instance

  # Prints a grid of all NPC objects
    TextAdd = "-----------------------------------------------------------\nNPC #" + str(NpcTar + 1) + " CHARACTERISTICS:\n\nNAME: " + Npcs[NpcTar].Name + "\nAGE: " + Npcs[NpcTar].Age + "\nGENDER: " + Npcs[NpcTar].Gender + "\nWEALTH: " + Npcs[NpcTar].Wealth + "\nIQ: " + Npcs[NpcTar].IQ + "\n-----------------------------------------------------------\n"
    Output = open("output.txt", "a")
    Output.write(TextAdd)
    Output.close()

print("All NPCs have been generated, check the output file for the results")

sys.exit()
