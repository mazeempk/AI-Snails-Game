import arcade
import random
import os
import copy


# from arcade.color import GREEN


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 65
HEIGHT = 65
SPRITE_SCALING = 0.5
ROW_COUNT = 10
COLUMN_COUNT = 10
MARGIN = 2
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 730
SCREEN_TITLE = "Array Backed Grid Example"


class MainView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
    def on_draw(self):
        arcade.start_render()
        textture1=arcade.load_texture("C:/Users/HP/Desktop/Snail game/mainBack.jpg")
        scaled1=1
        arcade.draw_scaled_texture_rectangle(500, 290, textture1, scaled1, 0)
        arcade.draw_text("Snails Game", 380, 550, arcade.color.WHITE, 66, font_name='Elephant')
        arcade.draw_text("Let the game begins", 590, 500, arcade.color.YELLOW_GREEN, 45, font_name='FTP - Virtuozo')
        arcade.draw_text("Press mouse to start the Game!", 450, 180, arcade.color.WHITE_SMOKE, 21)   
        textture5=arcade.load_texture("C:/Users/HP/Desktop/Snail game/icons.png")
        scaled5=1
        arcade.draw_scaled_texture_rectangle(690, 380, textture5, scaled5, 0)  
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if key == arcade.key.S:
            # User hits s. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Instead of a one-to-one mapping, stretch/squash window to match the
            # constants. This does NOT respect aspect ratio. You'd need to
            # do a bit of math for that.
            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)
    


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)
    


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.tmp_counter = (40,40)
        self.tmp_counter2 = (660,660)
        self.grid = []
        self.a1 = 0 
        self.stuck1 = 0
        self.stuck2 = 0
        self.window.score1=0
        self.window.score2=0
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
        
        self.grid[0][0] = 1
        self.grid[9][9] = 2
        self.turn = 0




    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        
        self.window.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()
        textture0=arcade.load_texture("C:/Users/HP/Desktop/Snail game/bck.jpg")
        scaled0=.6
        arcade.draw_scaled_texture_rectangle(700, 350, textture0, scaled0, 0)
        textture4=arcade.load_texture("C:/Users/HP/Desktop/Snail game/PL1.png")
        scaled4=.3
        arcade.draw_scaled_texture_rectangle(310, 700, textture4, scaled4, 0)

        textture6=arcade.load_texture("C:/Users/HP/Desktop/Snail game/AD.png")
        scaled6=.2
        arcade.draw_scaled_texture_rectangle(1100, 600, textture6, scaled6, 0)
        
        a=arcade.load_texture("C:/Users/HP/Desktop/Snail game/score.png")
        b=.3
        arcade.draw_scaled_texture_rectangle(1000, 360, a, b, 0)
        arcade.draw_text(str(self.window.score1),1100, 415, arcade.color.BLACK, 34)
        arcade.draw_text(str(self.window.score2),1100, 276, arcade.color.BLACK, 34)
    



    
 
 
 



        # Draw the board
        for row in range(ROW_COUNT):  #iterate on ecery grid position
            for column in range(COLUMN_COUNT):
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2  #grid
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2


                if self.grid[row][column] == 1:
                    p1 = arcade.load_texture("C:/Users/HP/Desktop/Snail game/SNAIL1.png")
                    size = 0.03
                    arcade.draw_scaled_texture_rectangle(x,y,p1,size,0)
                    

                if self.grid[row][column] == 2:
                    p2 = arcade.load_texture("C:/Users/HP/Desktop/Snail game/SNAIL2.png")
                    size = 0.025
                    arcade.draw_scaled_texture_rectangle(x,y,p2,size,0)
                
                if self.grid[row][column] == 10:
                    sp1 = arcade.load_texture("C:/Users/HP/Desktop/Snail game/sp1.png")
                    size = 0.025
                    arcade.draw_scaled_texture_rectangle(x,y,sp1,size,0)
                
                if self.grid[row][column] == 20:
                    sp2 = arcade.load_texture("C:/Users/HP/Desktop/Snail game/sp2.png")
                    size = 0.03
                    arcade.draw_scaled_texture_rectangle(x,y,sp2,size,0)




                
                arcade.draw_rectangle_outline(x,y,WIDTH,HEIGHT,arcade.color.WHITE,2)
    
    
    def legalmove(self,row,column,pre_row,pre_col):
        if row < ROW_COUNT and column < COLUMN_COUNT :
            if row == pre_row or column == pre_col:
                if (row == pre_row-1 or column == pre_col-1) or (row == pre_row+1 or column == pre_col+1):
            # Flip the location between 1 and 0.

                    return 1
        
    def position(self,grid,positionnumber):  #return the position of 1 or 2 passed to them  
        for i in range(10):
            for j in range(10):
                if grid[i][j] == positionnumber:
                    pos = (i,j)
                    return pos

    def possibilty(self,grid,positionnumber):#checks the all the possibilites of 1 or 2 by checking the adjacent blocks empty.
                                            #more empty blocks adjacent means more availaible chances and possibility
        count = 0
        array = []
        pos = self.position(grid,positionnumber)
        row = pos[0]
        column = pos[1]
        if row-1 >= 0:
            if grid[row-1][column] ==0:
                count += 1
                a = (row-1,column)
                array.append(a)
        if row+1 <10:
            if grid[row+1][column] ==0:
                count += 1
                a = (row+1,column)
                array.append(a)
            
        if column+1 <10:
            if grid[row][column+1] ==0:
                count += 1
                a = (row,column+1)
                array.append(a)
    
    
        if column-1 >=0:
            if grid[row][column-1] ==0:
                count += 1
                a = (row,column-1)

                array.append(a)
        
            
        return count,array,pos

    def evaluateBoard(self,bord):
        human_score = 0
        ai_bot_score =0
        
        for a in range(len(bord)):
            for b in range(len(bord[a])):
                if bord[a][b] == 0:
                    return 0
                elif bord[a][b] ==1 or bord[a][b] ==10:
                    human_score +=1
                elif bord[a][b] ==2 or bord[a][b] ==20:
                    ai_bot_score += 1
        
        if ai_bot_score > human_score:
            return 20
        elif ai_bot_score < human_score:
            return 10
        elif ai_bot_score == human_score:
            return 1020 
        
    def gen_child(self,grid,poss_count,poss_array,pos):
        grid_list = []
        for i in range(poss_count):
            a = copy.deepcopy(grid)#it generates the copy of grid according to the possibilities of 2 
            row = pos[0]
            column = pos[1]
            a[row][column] = 20
            new = poss_array[i]
            new_row = new[0]
            new_col = new[1]
            a[new_row][new_col] = 2
            grid_list.append(a)
        return grid_list#returns all the copies of the grid
    def heuristic(self,grid):#computes the winning chances of 2
        winningChances = 0
    # First Condition 
        count=0
        for i in grid:#checks the index of 2  in grid
            if 2 in i:
                a=i.index(2)
                row=count
                coloumn=a
                # print(row,coloumn)
            count+=1
            for j in i:#checks that how many blocks are covered by ai agent
                if j==20:
                    winningChances+=1
        if row+1<10:#checks how many adjacent blocks are empty and for every  block increases the winning chances
            if grid[row+1][coloumn]== 0:
                winningChances+=1
        if row-1>=0:
            if grid[row-1][coloumn]==0:
                winningChances+=1
        if coloumn+1<10:
            if grid[row][coloumn+1]==0:
                winningChances+=1
        if coloumn-1 >=0:
            if grid[row][coloumn-1]==0:
                winningChances+=1
        # minrange=6
        # maximumrange=12
        ourrange=row+coloumn
        if (1,3)<=(row,coloumn)<=(3,9):#checks that the current position is close to centre and increases the 10
            winningChances+=10
        return winningChances  
    
    
    def minimax(self,grid,depth,isMax):
        
        if depth==5:
            score = self.heuristic(grid)#when depth 5 is reached it means that the base condition has been reached and we can call the heuristic function for score
            return score
        
    # If Maximizer has won the game return his/her
                # evaluated score
    
 
    # this is maximizer's move means the move of ai agent
        if(isMax) :    
            best = -1000
            
            a=self.possibilty(grid,2)#every time it returns the possibility of 2 in available grid
            
            b=a[1]
            count=0
            count1=0
            for i in grid:
                if 2 in i:
                    col=i.index(2)
                    row=count
                    adress=row,col
                
                count=count+1
            if 1 in i:
                col=i.index(1)
                row=count1
                adress1=row,col
            count1=count1+1
            if len(b) !=0:  
                for i in ((b)):
                   
                    


                    row=i[0]
                    column=i[1]
                    previous=row,column  
                    
                            # Make the move
                    grid[previous[0]][previous[1]] = 2
                    grid[adress[0]][adress[1]]=20
                    
                            # Call minimax recursively and choose
                            # the maximum value
                    best = max( best, self.minimax(grid,depth + 1,False) )
        
                            #  Undo the move and return the previous original grid
                    grid[previous[0]][previous[1]] = 0
                    grid[adress[0]][adress[1]]=2

                return best
            else:
                score = self.heuristic(grid)
                return score
                
    #this is minimizer's move means this is the move of the player
        else :
            best=1000
            a=self.possibilty(grid,1)#every time it returns the possibility of 1 in available grid
            b=a[1]
            count=0
            count1=0
            for i in grid:
            
                if 2 in i:
                    col=i.index(2)
                    row=count
                    adress=row,col
                count=count+1
                if 1 in i:
                    col=i.index(1)
                    row=count1
                    adress1=row,col
                
                count1=count1+1
            if len(b)!=0:   
                for i in b:
                    
                    row=i[0]
                    column=i[1]
                    previous1=row,column
                    
                    grid[previous1[0]][previous1[1]] = 1
                    grid[adress1[0]][adress1[1]]=10
                    
                        # Call minimax recursively and choose
                        # the maximum value
                    best = min( best, self.minimax(grid,
                                            depth + 1,
                                            True) )
        
                            # Undo the move and return the previous original grid
                    grid[previous1[0]][previous1[1]] = 0
                    grid[adress1[0]][adress1[1]]=1
                return best
            else:
                score = self.heuristic(grid)
                return score
                
    def findbestmove(self,grid):#every time we call this function it finds the best move using mimmax and return a result
        
        grd = self.possibilty(grid,2)#return all the possibility of 2 in grid as 2 is for ai player
        poss_count = grd[0]
        poss_array = grd[1]
        pos = grd[2]
        

        child = self.gen_child(grid,poss_count,poss_array,pos)#this will return the child of the grid on bases of available 
                                                                  #position
        
        valueslist=[]
        if len(child)!=0: #if there are child available then we will all the miminax function on every child turn by turn
            for i in child:
                values=self.minimax(i,0,False)
                valueslist.append(values)#returns score of each deap copy 
    
            new= child,valueslist#it contains the child and there scores
            index0fmax=new[0][new[1].index(max(new[1]))]# it has the deap copy that has max score 
            
        # 
            count3=0
            for i in index0fmax:#in that deap copy we check the index of the 2
                if 2 in i:
                    coloumn=i.index(2)
                    row=count3
                    appropiaterowcoloumn=row,coloumn
                count3+=1
            return (appropiaterowcoloumn)#it returns the adress of the block where 2 should be placed to enhance the winning chances
        else:#else will run if ai agent has no child and it will then call the splash function
            a=self.position(grid,2)
            rowofstruck=a[0]
            coloumnofstruck=a[1]
            print(rowofstruck,coloumnofstruck)
            array=[]
            count=0
            if rowofstruck-1 >= 0:
                if grid[rowofstruck-1][coloumnofstruck] ==20:
                    count += 1
                    a = (rowofstruck-1,coloumnofstruck)
                    array.append(a)
            if rowofstruck+1 <10:
                if grid[rowofstruck+1][coloumnofstruck] ==20:
                    count += 1
                    a = (rowofstruck+1,coloumnofstruck)
                    array.append(a)
            
            if coloumnofstruck+1 <10:
                if grid[rowofstruck][coloumnofstruck+1] ==20:
                    count += 1
                    a = (rowofstruck,coloumnofstruck+1)
                    array.append(a)
    
    
            if coloumnofstruck-1 >=0:
                if grid[rowofstruck][coloumnofstruck-1] ==20:
                    count += 1
                    a = (rowofstruck,coloumnofstruck-1)

                    array.append(a)
            
            b=random.randint(0,count)
            
            c=array[b]
            return c

    def splashed1(self,row,column,p_row,p_column):
        if row == p_row and column == p_column-1:
            for a in range(0,9):
                if column >=0 :
                    if self.grid[row][column] == 10:
                    
                        column -= 1
            column += 1
        elif row == p_row and column == p_column+1:
            for a in range(0,9):
                if column <=9 :
                    if self.grid[row][column] == 10:
                        column += 1
            column -= 1
        elif column == p_column and row == p_row-1:
            for a in range(0,9):
                if row >=0 :
                    if self.grid[row][column] == 10:
                    
                        row -= 1
            row += 1
        elif column == p_column and row == p_row+1:
            for a in range(0,9):
                if row <=9 :
                    if self.grid[row][column] == 10:
                    
                        row += 1
            row -= 1

        return row,column

    def splashed2(self,row,column,p_row,p_column):
        if row == p_row and column == p_column-1:
            for a in range(0,9):
                if column >=0 :

                    if self.grid[row][column] == 20:
                        column -= 1
            column += 1
        elif row == p_row and column == p_column+1:
            for a in range(0,9):
                if column <=9 :

                    if self.grid[row][column] == 20:
                        column += 1
            column -= 1
        elif column == p_column and row == p_row-1:
            for a in range(0,9):
                if row >=0 :
                    
                    if self.grid[row][column] ==20:
                        row -= 1
            row += 1
        elif column == p_column and row == p_row+1:
            for a in range(0,9):
                if row <=9 :

                    if self.grid[row][column] == 20:
                        row += 1
            row -= 1

        return row,column
  







    def on_mouse_press(self, x, y, button, modifiers):
        result = self.evaluateBoard(self.grid)

        if result == 10 or result == 20 or result == 1020 or self.stuck1 ==7 or self.stuck2 ==7 :
            gameover = GameOverView(result,self.stuck1,self.stuck2)
            self.window.show_view(gameover)
        
        
        
        
        # print(x,y)
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))
        if column <=9 and row<=9:   #control outside clicks
            p_row = int(self.tmp_counter[0] // (WIDTH + MARGIN))
            p_col = int(self.tmp_counter[1] // (HEIGHT + MARGIN))
        else:
            p_row = p_col = 0

        # print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        if self.legalmove(row,column,p_row,p_col) == 1:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
                self.grid[p_row][p_col] = 10
                n_row = (MARGIN + WIDTH) * row + MARGIN + WIDTH // 2
                n_col = (MARGIN + HEIGHT) * column + MARGIN + HEIGHT // 2
                self.tmp_counter = (n_row,n_col)
                self.window.score1=self.window.score1+1
                self.stuck1 = 0

            elif self.grid[row][column] == 10:
                a = self.splashed1(row,column,p_row,p_col)
                row = a[0]
                column = a[1]
                self.grid[row][column] = 1
                self.grid[p_row][p_col] = 10
                n_row = (MARGIN + WIDTH) * row + MARGIN + WIDTH // 2
                n_col = (MARGIN + HEIGHT) * column + MARGIN + HEIGHT // 2
                self.tmp_counter = (n_row,n_col)
                self.stuck1 += 1



        pre_coord = self.position(self.grid,2)
        p_row = pre_coord[0]
        p_col = pre_coord[1]
        # print(self.grid)
        co_ordinates =  self.findbestmove(self.grid)
        row = co_ordinates[0]
        col = co_ordinates[1]
        if self.grid[row][col] == 0:
            self.grid[row][col] = 2
            self.grid[p_row][p_col] = 20
            self.window.score2=self.window.score2+1
            self.stuck2 = 0
            
        elif self.grid[row][col] == 20:
            a=self.splashed2(row,col,p_row,p_col)
            row = a[0]
            column = a[1]
            self.grid[row][column] = 2
            self.grid[p_row][p_col] = 20
            self.stuck2 += 1
                
                      


class GameOverView(arcade.View):
    def __init__(self,result,stuck1,stuck2):
        super().__init__()
        self.result = result
        self.stuck1 = stuck1
        self.stuck2 = stuck2


    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        
        if self.result ==10 or self.stuck2==7:
            arcade.draw_text("Player 1 WINS  ", 300, 500, arcade.color.GREEN, 80)
        elif self.result == 20 or self.stuck1==7:           
            arcade.draw_text("Player 2 WINS  ", 300, 500, arcade.color.GREEN, 80)
        elif self.result == 1020:   
            arcade.draw_text("Match Drawn  ", 300, 500, arcade.color.GREEN, 80)
                    
        
        arcade.draw_text("Game Over", 470, 400, arcade.color.WHITE, 54)
        
        arcade.draw_text("Click to restart", 550, 160, arcade.color.WHITE, 24)
        


        output_total1 = f"PLAYER 1 SCORE =  {self.window.score1}"
        arcade.draw_text(output_total1, 540, 340, arcade.color.RED, 18)
        
        output_total2 = f"PLAYER 2 SCORE =  {self.window.score2}"
        arcade.draw_text(output_total2, 540, 300, arcade.color.BLUE_VIOLET, 18)
        
        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

        
        


        
        











def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Different Views Example",fullscreen=True)
    window.total_score = 0
    window.score1 = 0
    window.score2 = 0
    menu_view = MainView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()