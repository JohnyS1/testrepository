import pyinputplus as pyip

##pyinputplus.inputStr(limit=3, default='hello')
AdditionList=['mayo', 'mustard', 'lettuce', 'tomato', 'all']
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Select type of bread:\n', numbered=True)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Select type of protein:\n', numbered=True)
x = pyip.inputYesNo(prompt='Do you want some cheese?\n')
if x=='yes':
    cheese= pyip.inputMenu(['cheddar', 'Swiss', 'mozarella'], prompt='Select type of cheese:\n', numbered=True)
else:
    cheese = 'no'
##z = pyip.inputYesNo(prompt='Do you want some additives?\n')
##while z=='yes' and len(AdditionList)!=0:
##    try:
##        inputAdditionsList = pyip.inputMenu(AdditionList, prompt='Select type of addition:\n', numbered=True)
##        AdditionList.remove(inputAdditionsList)
##        if inputAdditionsList=='all':
##            break
##        z = pyip.inputYesNo(prompt='Do you want some additives?\n')
##    except:
##        print(f'No more choices')
##        break
##if len(AdditionList)!=5 or len(AdditionList)!=0:
##    inputAdditionsList=='no'
amount=pyip.inputInt(prompt='How many sandwiches do you want?\n')

print('You want %s sandwich on bread %s with %s, %s cheese' %(amount, bread, protein, cheese))
input()
