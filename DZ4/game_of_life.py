# coding: utf-8

import pygame as pg
import numpy as np


class GameOfLife():

	def __init__(self, width=640, height=480, cell_size=20, FPS=30):
		self.width = width
		self.height = height
		self.cell_size = cell_size

		self.screen = pg.display.set_mode((width, height))

		self.Ncol = self.width // self.cell_size
		self.Nrow = self.height // self.cell_size

		self.FPS = FPS

		self.grid = np.zeros((self.Nrow, self.Ncol), dtype="int")
		self.next_grid = np.zeros((self.Nrow, self.Ncol), dtype="int")


	def draw_lines(self):
		for x in range(self.cell_size, self.width, self.cell_size):
			pg.draw.line(self.screen, pg.Color("black"), (x, self.cell_size), (x, self.height-self.cell_size))

		pg.draw.line(self.screen, pg.Color("black"), (0, 0), (self.width, 0))
		for y in range(self.cell_size, self.height, self.cell_size):
			pg.draw.line(self.screen, pg.Color("black"), (self.cell_size, y), (self.width-self.cell_size, y))


	def draw_cell(self, nrow, ncol, status):

		color = "white"
		if status == 1: color = "orange"
		
		x = self.cell_size * ncol 
		y = self.cell_size * nrow
		pg.draw.rect(self.screen, pg.Color(color), (x, y, self.cell_size, self.cell_size))
	

	def next_status(self):
		for i in range(1, self.Nrow-1):
			for j in range(1, self.Ncol-1):

				if self.grid[i][j] == 0:
					if np.sum(self.grid[i-1:i+2, j-1:j+2]) == 3:
						self.next_grid[i][j] = 1
						self.draw_cell(i, j, 1)

				else:
					if np.sum(self.grid[i-1:i+2, j-1:j+2])-1 == 2 or np.sum(self.grid[i-1:i+2, j-1:j+2])-1 == 3:
						self.next_grid[i][j] = 1
					else:
						self.draw_cell(i, j, 0)


	def run(self):
		pg.init()
		pg.display.set_caption('Game of Life')
		self.screen.fill(pg.Color('white'))
		fnt = pg.font.Font(None, int(1.5*self.cell_size))

		clock = pg.time.Clock()

		run = False
		running = True
		while running:
			clock.tick(self.FPS)

			for event in pg.event.get():
				if event.type == pg.QUIT: running = False

				if event.type == pg.MOUSEBUTTONDOWN and \
				event.pos[0]>self.cell_size and event.pos[0]<self.width-self.cell_size and \
				event.pos[1]>self.cell_size and event.pos[1]<self.height-self.cell_size:

					ncol = event.pos[0] // self.cell_size
					nrow = event.pos[1] // self.cell_size
						
					if event.button == 1:
						self.grid[nrow][ncol] = 1
						self.draw_cell(nrow, ncol, 1)
					if event.button == 3:
						self.grid[nrow][ncol] = 0
						self.draw_cell(nrow, ncol, 0)

				if event.type == pg.KEYUP and (event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN): run = (run == False)
				
			if run:
				text = fnt.render("Stopped", False, pg.Color("white"))
				self.screen.blit(text, (0, 0))
				text = fnt.render("Running...", False, pg.Color("black"))
				self.screen.blit(text, (0, 0))

				# print(self.grid)
				self.next_status()
				# print(self.next_grid)
				self.grid = self.next_grid.copy()
				self.next_grid = np.zeros((self.Nrow, self.Ncol), dtype="int")
			else:
				text = fnt.render("Running...", False, pg.Color("white"))
				self.screen.blit(text, (0, 0))
				text = fnt.render("Stopped", False, pg.Color("black"))
				self.screen.blit(text, (0, 0))


			self.draw_lines()

			pg.display.flip()


		pg.quit()



		

# game = GameOfLife(500, 500, 100, 2)
game = GameOfLife()

game.run()
