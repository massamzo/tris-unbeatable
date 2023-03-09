tris = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

# 0 is player
# 1 is robot
turn = 0

players = ['o','x']

def showTris(tris):
    print("----------\n")

    for i in range(len(tris)):
        print("[",tris[i][0], tris[i][1],tris[i][2], "]")

    print("----------\n")

def indConverter(inp):

   
    x=0
    y = 0
    if(int(inp)%3 != 0):
        y = int(int(inp)/3)
        x = int(inp)-((y*3)-1)-2
    
    else:
        y = int(int(inp)/3)-1
        x = 2

    return [x,y]

def askUser(tris):
    global turn
    inp = input("choise : ")

    #calculating the indexes
    
    vals = indConverter(inp)
    
    tris[vals[1]][vals[0]] = players[turn]

    #change turn 

    if(turn):
        turn = 0
    else:
        turn = 1



# winner check

def winnerCheck(tris):

  
  for i in range(len(tris)):

    #horrizontal check
    if(tris[i][0] == tris[i][1] and tris[i][1] == tris[i][2]):
      return tris[i][0]

    #vertical check
    if(tris[0][i] == tris[1][i] and tris[1][i] == tris[2][i]):
      return tris[0][i]


  #oblique check

  if((tris[0][0] == tris[1][1] and tris[2][2] == tris[0][0]) or (tris[0][2] == tris[1][1] and tris[2][0] == tris[1][1])):
    return tris[1][1]

  #draw check

  x = 0
  for i in range(len(tris)):
    for j in range(len(tris[i])):
      if(tris[i][j] == 'x' or tris[i][j] == 'o'):
        x +=1

  if(x == 9):
    return 'd'

  #if the game isn't finished
  return 'n'




#implementing the minMax

#this finds the index number from 1 to 9 for the robot
def indexFiner(dati, tris):
    #find the maximum with it's index
    ind = 0;
    max = -1;
    for i in range(len(dati)):
        if(dati[i] > max):
            max = dati[i];
            ind = i;

    #find the position
    x = 0;
    for i in range(len(tris)):
        for j in range(len(tris[i])):
            if(tris[i][j] != 'x' and tris[i][j] != 'o'):
                if(x == ind):
                    return int(tris[i][j])
                x+=1


def minMax(tris, turn, level):

  #strating point 
  trisCopy = list(tris)
    
  
 

  dati = []
  
  for i in range(len(trisCopy)):
    for j in range(len(trisCopy[i])):

      val = trisCopy[i][j]
      #it's free
      if(trisCopy[i][j] != 'x' and trisCopy[i][j] != 'o'):
        
        trisCopy[i][j] = players[turn]

        t2 = 0;
        if(turn == 0):
            t2 = 1
        else:
            t2 = 0


        #check if someone has won or not

        if(winnerCheck(trisCopy) != 'n'):
            #it's either draw or someone won

            if(winnerCheck(trisCopy) != 'd'):
                #it's not a draw, the current player has won

                if(turn == 0):
                    dati.append(-1)
                else:
                    dati.append(1)

            else:
                dati.append(0)

                


        else:

            #no one has wo
            dati.append(minMax(trisCopy, t2, level+1))

      
      #restoring the original value of the cell
      trisCopy[i][j] = val

  
  # once i got out of the loop return the min or max value

  if(level != 0):
        if(turn == 0):
            return min(dati)
        else: 
            return max(dati) 

  else:
        # on the first return the index value of the position

        return indexFiner(dati, trisCopy)
    

def changeTurn(turn):
    
    if(turn == 0):
        turn =1;
    else:
        turn = 0


def robTurn(tris):
    global turn
    inp = minMax(tris,turn,0)
    ins = str(inp)
    
    vals = indConverter(ins)

    tris[vals[1]][vals[0]] = players[turn]

    if(turn == 0):
        turn =1;
    else:
        turn = 0


def startGame():
    while(winnerCheck(tris) == 'n'):
        
        showTris(tris)
        askUser(tris)

        showTris(tris)
        if(winnerCheck(tris) == 'x'):
            print("winner  :  x")
            break;
        elif(winnerCheck(tris) == 'o'):
            print("winner  : o")
            break;
        elif(winnerCheck(tris) == 'd'):
            print("DRAW")
            break;
            
        robTurn(tris)

        showTris(tris)
        if(winnerCheck(tris) == 'x'):
            print("winner  :  x")
            break;
        elif(winnerCheck(tris) == 'o'):
            print("winner  : o")
            break;
        elif(winnerCheck(tris) == 'd'):
            print("DRAW")
            break;


    

