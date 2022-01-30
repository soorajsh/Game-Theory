import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

class Game:
    def __init__(self):
        self.p_list = []
        self.total_chips = 50
        self.min_moves = 1
        self.max_moves = 6
    # def sum_of_lists(self, l):
    #     self.l = l
    #     self.total = 0
    #     for value in self.l:
    #         self.total += value
    #     return self.total

    def check_input(self, pl1, pl2, inp):
        self.input = inp
        pl1.num = pl1.p_list 
        pl2.num = pl2.p_list
        sum_all = sum(pl1.num + pl2.num) + self.input

        if self.input <self.min_moves or self.input>self.max_moves:
            print('Only ',self.min_moves,'-',self.max_moves,' chips can be used at a time.')
            return False
        elif sum_all > self.total_chips :
            print('The chips u asked is unavailable.')
            return False 
        else:
            return True
    def append_list(self, num):
        self.p_list.append(num)
    
    # def check_total(self, )

player1 =  Game()
player2= Game()
while(1):
    win = False
    while(1):
        print('First Player')
        chips = sum(player1.p_list + player2.p_list)
        print('The total no. of chips used:', chips)
        print('Available chips', player1.total_chips-chips)
        temp = int(input('Please select a number from '+ str(player2.min_moves)+'-'+ str(player2.max_moves)+' :'))
        if player1.check_input(player1, player2, temp) == True:
            player1.append_list(temp)
            chips = sum(player1.p_list + player2.p_list)
            if(chips == player1.total_chips):
                print('Player 1 won')
                win = True
            break
    if win== True:
        break
    while(1):
        print('Second Player')
        chips = sum(player1.p_list + player2.p_list)
        print('The total no. of chips used:', chips)
        print('Available chips', player1.total_chips-chips)
        temp = int(input('Please select a number from '+ str(player2.min_moves)+'-'+ str(player2.max_moves)+' :'))
        if player2.check_input(player1, player2, temp) == True:
            player2.append_list(temp)
            chips = sum(player1.p_list + player2.p_list)
            if(chips == player2.total_chips):
                print('Player 2 won')
                win = True
            break
    if win== True:
        break


