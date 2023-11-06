from iter_game import iter_game
import pygame
import random
# Initialize the game
# Set up the game window
window_width = 800
window_height = 600
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Define game variables
snake_size = 20
snake_speed = 10
clock = pygame.time.Clock()
# Define the Snake class
class Snake:
	def __init__(self):
		self.x = window_width // 2
		self.y = window_height // 2
		self.direction = "RIGHT"
		self.length = 1
		self.body = []
	def move(self):
		if self.direction == "UP":
			self.y -= snake_size
		elif self.direction == "DOWN":
			self.y += snake_size
		elif self.direction == "LEFT":
			self.x -= snake_size
		elif self.direction == "RIGHT":
			self.x += snake_size
	def draw(self,pygame,screen):
		for part in self.body:
			pygame.draw.rect(screen, GREEN, (part[0], part[1], snake_size, snake_size))
	def check_collision(self):
		if self.x < 0 or self.x >= window_width or self.y < 0 or self.y >= window_height:
			return True
		for part in self.body[1:]:
			if self.x == part[0] and self.y == part[1]:
				return True
		return False
# Define the Food class
class Food:
	def __init__(self):
		self.x = random.randint(0, (window_width - snake_size) // snake_size) * snake_size
		self.y = random.randint(0, (window_height - snake_size) // snake_size) * snake_size
	def draw(self,pygame,screen):
		pygame.draw.rect(screen, RED, (self.x, self.y, snake_size, snake_size))
# Initialize the snake and food
snake = Snake()
food = Food()

class snake_game(iter_game):
	def __init__(self,window_width=50,window_height=50):
		self.i = 2
		self.window_height = window_height
		self.window_width = window_width
		self.fin = False
	def next(self,pygame,events,screen,dt,data):
		global snake
		global food
		if self.fin:
			data.game_num = 0
			return
		for event in events:
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and snake.direction != "DOWN":
					snake.direction = "UP"
				elif event.key == pygame.K_DOWN and snake.direction != "UP":
					snake.direction = "DOWN"
				elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
					snake.direction = "LEFT"
				elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
					snake.direction = "RIGHT"
		# Move the snake
		snake.move()
		# Check collision with food
		if snake.x == food.x and snake.y == food.y:
			snake.length += 1
			food = Food()
		# Update the snake's body
		snake.body.insert(0, (snake.x, snake.y))
		if len(snake.body) > snake.length:
			snake.body.pop()
		# Check collision with snake's body or boundaries
		if snake.check_collision():
			data.game_num = 0
			self.fin = True
		# Clear the window
		screen.fill(BLACK)
		# Draw the snake and food
		snake.draw(pygame,screen)
		food.draw(pygame,screen)
		# Update the display
		pygame.display.update()
		# Set the game speed
		clock.tick(snake_speed)
