from tkinter import *
import os
import cv2
import numpy as np


screen1 = Tk()
screen1.title("Ursu' Food")
screen1.geometry("500x500")
screen1.resizable(0, 0)

screen2 = Tk()
screen2.title("Ursu' Food")
screen2.geometry("500x500")
screen2.resizable(0, 0)

canvas = Canvas(screen2, width = 500, height = 500)
canvas.pack()

img = cv2.imread('Food+Bg.jpg', 1)
cv2.imshow("Welcome to Ursu' Food", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

class ShowFood:
	def __init__(self):

		#Widgets
		self.Pizza_tuna = Label(screen1, text = "Pizza Tuna")
		self.Pizza_carnivora = Label(screen1, text = "Pizza Carnivora")
		self.Pizza_Shark = Label(screen1, text = "Pizza Shark")
		self.Pizza_Porumb = Label(screen1, text = "Pizza Porumb")

		self.Supa_de_galuste = Label(screen1, text = "Supa de galuste")
		self.SUpa_de_peste = Label(screen)

		#Prime Labels
		self.Pizza = Label(screen1, text = "Pizza")
		self.Supa = Label(screen1, text = "Supa")

		#Grid Prime Labels
		self.Pizza.grid(row = 0, column = 0)
		self.Supa.grid(row = 0,  column = 1)

		#Grid Widgets
		self.Pizza_tuna.grid(row = 1, column = 0)
		self.Pizza_carnivora.grid(row = 2, column = 0)
		self.Pizza_Shark.grid(row = 3, column = 0)



def main():

	FoodButton = Button(screen1, text = "Food", command = ShowFood)
	FoodButton.grid(row = 0, column = 2)

	screen2.mainloop()
	screen1.mainloop()


if __name__ == '__main__':
	main()
