# Gnarly-Supernumeraries-Pioneer (NPC-Generator)

## Features

- Customizable amount of NPCs
- Customizable NPC features such as:
  - Name
  - Age
  - Ethnicity
  - Gender
  - Wealth
  - IQ
- Text file output
- Choice between and and input generation

## Code Facets

**This Python Program uses many different and versatile methods in the process of NPC Generation.** One of these such methods is the *Class* object, which is what stores the value of the NPCs, which then get transferred to another branch of the program, a *list*. This list contains all the NPC objects stored in the NPC class shown:
```python
class Npc:
    # The __init__ func lets you include paramaters that will perist in different objects of the class, but have different values
    def __init__(self, Name, Age, Gender, Wealth, IQ):
        self.Name = str(Name)
        self.Age = str(Age)
        self.Gender = str(Gender)
        self.Wealth = str(Wealth)
        self.IQ = str(IQ)
```
*This class is accessed throught the code in order to store the different values of the NPCs*

The list that stores the NPC is constantly updated through a *for* loop, this list containing all the NPC objects is shown below:
```python
Npcs.append(CurrentNpc) # Adds the finished NPC object to a list, where its value will be stored independent of the other objects despite having the same variable name
```

The final facet of the code which is majorly important to the overall program is the *open* method which allows for the code to be written on a seperate text file. This *open* method works by deleting the previous output file, creating a new one, and then writing the values of all the NPC objects to the new file. The code for deleting the previous session can be found below:
```python
if os.path.exists("output.txt"): # checks if file exists to prevent errors
        os.remove("output.txt")
```

The code for creating the new file and writing the values to it:
```python
for NpcTar in range(int(NpcNum)):  # Goes through the code for each NPC instance

  # Prints a grid of all NPC objects
    TextAdd = "-----------------------------------------------------------\nNPC #" + str(NpcTar + 1) + " CHARACTERISTICS:\n\nNAME: " + Npcs[NpcTar].Name + "\nAGE: " + Npcs[NpcTar].Age + "\nGENDER: " + Npcs[NpcTar].Gender + "\nWEALTH: " + Npcs[NpcTar].Wealth + "\nIQ: " + Npcs[NpcTar].IQ + "\n-----------------------------------------------------------\n"
    Output = open("output.txt", "a")
    Output.write(TextAdd)
    Output.close()
```
*Here, the for loop loops through all the NPCs, and sets a variable "TextAdd" equal to what is going to be written on the text file. Then a new file is opened and the new test is appended to the file.*
