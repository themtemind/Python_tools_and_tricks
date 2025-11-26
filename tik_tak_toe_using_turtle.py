from turtle import *
from pygame import mixer
from tkinter import messagebox
cellCenter = {
    '1':(-200,200),'2':(0,200),'3':(200,200),
    '4':(-200,0),'5':(0,0),'6':(200,0),
    '7':(-200,-200),'8':(0,-200),'9':(200,-200)
}
validMoves = list(cellCenter.keys())
occupiedMoves = {'black':[],'yellow':[]}
turn = 'black'
rounds = 0
def board():
    global cellcenter
    Screen()
    setup(600,600,10,70) # the whole window is 600x600 pixels
    title("Tic Tac Toe")
    bgcolor("light yellow")
    pensize(5)
    color("black")
    hideturtle()
    tracer(False)
    for i in (-100,100):
        up()
        goto(i,300)
        down()
        goto(i,-300)
        up()
        goto(-300,i)
        down()
        goto(300,i)
        up()
    for cell, center in cellCenter.items():
        up()
        goto(center)
        write(cell,align='center',font=('Arial',20,'normal'))

def winner():
    global occupiedMoves, turn
    win = False
    winningCombos  = [
        ['1','2','3'],['4','5','6'],['7','8','9'], # rows
        ['1','4','7'],['2','5','8'],['3','6','9'], # columns
        ['1','5','9'],['3','5','7']                # diagonals  
    ]
    for combo in winningCombos:
        if all(cell in occupiedMoves[turn] for cell in combo):
            win = True
            break
    return win
        
def position(x,y):
    global turn, rounds, occupiedMoves, validMoves
    if -300<x<300 and -300<y<300:
        col = int((x + 300)//200) + 1 # 1,2,3 and to  make range of x 0 to 600
        row = int((y + 300)//200) + 1 # 1,2,3 and to  make range of y 0 to 600
        cell = str((3 - row)*3 + col)
        print(f"Clicked on cell {cell}")
        mixer.init()
        mixer.music.load("E:\mouse.mp3")
        mixer.music.play()
    else:
        print("Clicked outside the board")
    
    if cell in validMoves:
        rounds += 1
        validMoves.remove(cell)
        occupiedMoves[turn].append(cell)
        goto(cellCenter[cell])
        if turn == 'black':
            dot(100,turn)
            if winner():
                validMoves = []
                messagebox.showinfo("Game Over",f"{turn} wins!")
            else:
                turn = 'yellow'
        elif rounds == 9 and len(validMoves) == 0 and not winner():
            messagebox.showinfo("Game Over","It's a tie!")
        else:
            turn = 'yellow'
            dot(100,turn)
            if winner():
                validMoves = []
                messagebox.showinfo("Game Over",f"{turn} wins!")
            else:
                turn = 'black'
    else:
        messagebox.showerror("Invalid Move","Cell already occupied or invalid move")   
        import sys
        sys.exit()        

def main():
    onscreenclick(position)
    board()
    update()
    done()
    try:
        bye()
    except:
        pass
    
if _name_ == "_main_":
    main()
