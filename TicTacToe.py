theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

##print(theBoard)
##for True:
##print(theBoard)
##print(theBoard['top-L'],'|',theBoard['top-M'],'|',theBoard['top-R'])
##print(theBoard['mid-L'],'|',theBoard['mid-M'],'|',theBoard['mid-R'])
##print(theBoard['low-L'],'|',theBoard['low-M'],'|',theBoard['low-R'])
##input('X or O')
##

print(theBoard)
def printBoard(board):
    print('      L M R')
    print('top: ',board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('      -+-+-')
    print('mid: ',board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('      -+-+-')
    print('low: ',board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
n=0
turn='X'
##for n in range(9): #pierwowzór który sam opracowałem
##    if n==0:
##        print('Write name_of_row-name_of_column, for example where you write as first move top-L X will occur in top left corner. X start.')
##    printBoard(theBoard)
##    k=input('Enter coorindates\n')
####    if k=='i':
####        print('Write name_of_row-name_of_column=X/O, for example for input top-L=X will input X in top left corner')
####        n=0
##    if n%2==0:
##        theBoard[k]='X'
##    if n%2!=0:
##        theBoard[k]='O'

for n in range(9): #pierwowzór który sam opracowałem
    if n==0:
        print('Write name_of_row-name_of_column, for example where you write as first move top-L X will occur in top left corner.')
    printBoard(theBoard)
    
    k=input('Turn for: ' + turn + '. Move on which space?\n')
    theBoard[k]=turn        
    if turn=='X':
        turn='O'
        continue
    if turn=='O':
        turn='X'
    if k not in theBoard.keys():
        print('Wrong move')
        n-1
    
        
