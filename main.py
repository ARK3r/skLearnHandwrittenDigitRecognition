# Project: Handwritten Digit Recognition
# Created by: Ahmad Reza Kermani github.com/ARK3r
#							Thanks to: @juggy1233 and @Jigy5000
# Date: Jan 14th, 2018

# this program will read previous data stored in a file "data.csv" to train two sklearn classifiers and
# will decide on the value that both of them decide on, otherwise the prediction with a lower value, and
# will output the prediction.

# the training happens everytime the program is run, using the previous data, therefore it is not expected
# for the program to start working through it's first run or to improve over time using the same build of the 
# program since it is designed to save the data each time it is being closed, using the titlebar close button
# or simply pushing the escape button on the keyboard, the program will be closed and the data will be stored
# for future usage of training.

# since the screen created by pygame is 280x280pix, it is shorten to 28x28 as the conventional MNIST database
# and is flatten. Although it is clear that this approach will ignore the placement of the pixels with respect
# to each other, which can be fixed using convolutional readings, for this program it is only intended to implement
# simple ideas for the sake of using them as steps forward. 


from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import csv
import pygame, sys
import random
import numpy as np

data = []
labels = []

numbers = [0 for i in range(10)]

with open('data.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ' ')
	for row in reader:
		labels.append(int(row[0]))
		numbers[labels[-1]] += 1
		cur_list = []
		for i in range(1, len(row)):
			cur_list.append(int(row[i]))
		data.append(cur_list)

for i in range(10):
	print "number of", str(i) + ":", numbers[i]

pygame.init()

size = width, height = 280, 280

screen = pygame.display.set_mode(size)


pixels = [[False for i in range(280)] for j in range(280)]
drawing_points = []


def count_pixels(surf):
	col_array = []
	for i in range(280):
		tmp = []
		for j in range(280):
			tmp.append(0)
		col_array.append(tmp)

	for x in range(280):
		for y in range(280):
			col = surf.get_at((x,y))
			if col==(0,0,0):
				col_array[x][y] = 1

	oned_array = []
	for x in range(0, 280, 10):
		for y in range(0, 280, 10):
			total = 0
			for i in range(10):
				for j in range(10):
					total += col_array[x+i][y+j]
			oned_array.append(total)
	return oned_array

def save_data():
	with open('data.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ')
		while len(data) != 0:
			i = random.randint(0, len(data) - 1)
			data[i].insert(0, labels[i])
			writer.writerow(data[i])
			del data[i]
			del labels[i]
data_beg_len = len(data)
if data_beg_len != 0:
	clf1 = SVC()
	clf1.fit(data, labels)
	clf2 = GaussianNB()
	clf2.fit(data, labels)



				

number = 20;

new_input = []

def choose_ans(a):
	ans = [0 for i in range(10)]
	for n in a:
		ans[n] += 1
	num = 0
	for i in range(10):
		if ans[i] > num:
			num = i
	return num

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_data()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				save_data()
				sys.exit()
			if event.key >= pygame.K_0 and event.key <= pygame.K_9:
				number = event.key - pygame.K_0

			if event.key == pygame.K_SPACE and number != 20:
				pred = []
				cur_screen = count_pixels(screen.copy())
				pred.append(cur_screen)
				if data_beg_len == 0:
					print "training..."
				else:
					print choose_ans([clf1.predict(pred)[0], clf2.predict(pred)[0]])
					# print clf1.predict(pred)[0]
					# print clf2.predict(pred)[0]
				labels.append(number)
				number = 20
				data.append(count_pixels(screen.copy()))
				pixels = [[False for i in range(280)] for j in range(280)]
				drawing_points = []
				screen.fill((255, 255,255))




	screen.fill((255, 255, 255))
	if pygame.mouse.get_pressed()[0]:
		pos = pygame.mouse.get_pos()
		if not pixels[pos[0]][pos[1]]:
			drawing_points.append(pos)

	for i in range(len(drawing_points) - 1):
		pygame.draw.line(screen, (0,0,0), drawing_points[i], drawing_points[i+1], 5)

	pygame.display.flip()

