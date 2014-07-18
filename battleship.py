import random

class Battleships:	
	
	def __init__(self):
		""" Creates game board and places Battleship """
		print
		print 'You have 10 turns to sink my Battleship.'
		print
		
		self.inprogress = True
		self.size = 5
		self.turn = 10
		self.board = []
		for i in range(self.size): 
			self.board.append(['O'] * self.size)
		self.hidden_ship = [random.randrange(self.size), random.randrange(self.size)]
#		print self.hidden_ship, ' = hidden ship'
		self.atkhist = []
		self.display()
		self.player_move()
		
	def display(self):
		""" Draws the game board on terminal """
		for i in self.board:
		    line = ' '.join(i)
		    print line
		    		    
	def player_move(self):
		""" Game logic """
		
		while self.inprogress:
			
			atkpos = []
			row = raw_input('Enter row to attack ')
			col = raw_input('Enter column to attack ')
			try:
				row = int(row) - 1
				col = int(col) - 1
			except:
				print 'Please enter integers only.'
				self.player_move()
				
			atkpos = [row, col]
			
			missed = False
			for numb in atkpos:
				if numb >= 0 and numb < self.size:
					pass
				else:
					missed = True
								
			if not missed:
				if atkpos in self.atkhist:
					print 'You\'ve already attacked here, try again.'
					self.player_move()
				
				self.atkhist.append(atkpos)	
				
				if atkpos == self.hidden_ship:
					self.board[row][col] = 'S'
					self.display()
					self.hidden_ship[0] += 1
					self.hidden_ship[1] += 1
					print 'You shunk my Battleship at ' + str(self.hidden_ship) + ', you win!'
					self.inprogress = False
					break
				else:
					pass
				
				self.board[row][col] = 'X'
				self.display()
					
			else:
				print 'You missed, adjust your aim next turn!'
			
			self.turn -= 1
			print 'Turns remaining: ' + str(self.turn)
			if self.turn == 0:
				self.inprogress = False
				print 'Game Over'
				print
				break
				
		self.new_game()

	def new_game(self):
		retry = raw_input('Play again? y/n ')
		if retry.isalpha(): 
			retry.lower()
		else:
			pass
				
		if retry == 'y':
			self.__init__()
		else:
			print 'Thanks for playing.'
		print
	
				
game = Battleships()
game
