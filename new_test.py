import csv

def get_TestScript():
    Script_Raw = []
    Script_Output = []
    Script_File = open('text.csv', 'r')

    for line in Script_File:
        Script_Raw.append(line.strip('\n'))

    for i in range(1, len(Script_Raw)):
        Script_Output.append(Script_Raw[i].split(''))

    for i in range(0, len(Script_Output)):
        for j in range(0, len(Script_Output[i])):
            Script_Output[i][j] = Script_Output[i][j].strip()

    return Script_Output


Script = get_TestScript()
print(Script[1])

#print(Script)
#for i in range(0, len(Script)) :
#    if i < 30 :
#        for j in range(0, len(Script[i])):
#            print(Script[i][j])
