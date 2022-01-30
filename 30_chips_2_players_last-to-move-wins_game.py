# import os

# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')

# # now, to clear the screen
# cls()

class Game:
    def __init__(self):
        self.p_list = []
    def sum_of_lists(self, l):
        self.l = l
        self.total = 0
        for value in self.l:
            self.total += value
        return self.total

    def check_input(self, pl1, pl2, inp):
        self.input = inp
        pl1.num = pl1.p_list 
        pl2.num = pl2.p_list
        sum_all = sum(pl1.num + pl2.num) + self.input

        if self.input <1 or self.input>6:
            print('Only 1-6 chips can be used at a time.')
            return False
        elif sum_all >30 :
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
        print('Available chips', 30-chips)
        temp = int(input('Please select a number from 1 to 6:'))
        if player1.check_input(player1, player2, temp) == True:
            player1.append_list(temp)
            chips = sum(player1.p_list + player2.p_list)
            if(chips == 30):
                print('Player 1 won')
                win = True
            break
    if win== True:
        break
    while(1):
        print('Second Player')
        chips = sum(player1.p_list + player2.p_list)
        print('The total no. of chips used:', chips)
        print('Available chips', 30-chips)
        temp = int(input('Please select a number from 1 to 6:'))
        if player2.check_input(player1, player2, temp) == True:
            player2.append_list(temp)
            chips = sum(player1.p_list + player2.p_list)
            if(chips == 30):
                print('Player 2 won')
                win = True
            break
    if win== True:
        break


