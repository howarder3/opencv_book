# import the necessary packages
# import argparse
import cv2
import numpy as np
# import matplotlib.pyplot as plt
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
point_list = []
cropping = False

keyboard_array = [
["q","w","e","r","t","y","u","i","o","p"],
["a","s","d","f","g","h","j","k","l",";"],
["z","x","c","v","b","n","m",",",".","/"]
]



class CV_KEYBORAD:
	def __init__(self, keyboard_array):
		# init keyboard background
		self.__keyboard_array = keyboard_array
		self.__keyboard_size = 90
		shape = (len(self.__keyboard_array)*self.__keyboard_size, len(self.__keyboard_array[0])*self.__keyboard_size, 3) # y, x, RGB
		self.__clean_img = np.full(shape, 255).astype(np.uint8)
		self.key_setting()
		self.__clean_keyboard = self.__keyboard_img.copy()
		self.__word_list = ""
		shape = (100, 1000, 3) # y, x, RGB
		self.__clean_screen = np.zeros(shape).astype(np.uint8)
		self.__current_screen = self.__clean_screen.copy()
		self.update_screen()
		self.show_screen()


	def update_screen(self):
		word = self.__word_list
		word_size = 1
		word_position = (50, 50)
		word_color = (0, 255, 255)
		word_thickness = 1
		word_lineType =  cv2.LINE_AA
		cv2.putText(self.__current_screen, word, word_position, cv2.FONT_HERSHEY_DUPLEX, word_size, word_color, word_thickness, word_lineType)


	def get_words_from_keyboard(self, x, y):
		return self.__keyboard_array[x][y]

	def click_and_crop(self, event, x, y, flags, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			point = (x, y)
			cv2.circle(self.__keyboard_img, point, self.__keyboard_size//10, (0, 0, 255), -1)
			self.__word_list += self.get_words_from_keyboard(x=y//self.__keyboard_size, y=x//self.__keyboard_size) # iamge position (x,y) -> list position (y,x)
			self.update_screen()
			 

	def show_screen(self):
		cv2.namedWindow("keyboard")
		cv2.namedWindow("show_screen")
		cv2.setMouseCallback("keyboard", self.click_and_crop)
		

		while True:
			# display the image and wait for a keypress
			cv2.imshow("keyboard", self.__keyboard_img)
			cv2.imshow("show_screen", self.__current_screen)
			key = cv2.waitKey(1) & 0xFF
			# if the 'r' key is pressed, reset the cropping region
			if key == ord("r"):
				self.__keyboard_img = self.__clean_keyboard.copy()
				self.__word_list = ""
				self.__current_screen = self.__clean_screen.copy()
			# if the 'c' key is pressed, break from the loop
			elif key == ord("c"):
				break

		cv2.destroyAllWindows()	


	def key_setting(self):
		self.__keyboard_img = self.__clean_img.copy()
		for y_idx in range(len(self.__keyboard_array)):
			for x_idx in range(len(self.__keyboard_array[0])):
				color = (200, 200, 200) if (x_idx+y_idx)%2==0 else (100, 100, 100)
				self.add_key(x=x_idx*self.__keyboard_size, y=y_idx*self.__keyboard_size, color = color) # gray
				self.write_word(x=x_idx*self.__keyboard_size, y=y_idx*self.__keyboard_size, word_color = (0, 255, 255), word=self.__keyboard_array[y_idx][x_idx]) # gray

				# self.add_key(x=2*self.__keyboard_size, y=0, color = (0, 0, 0), word="w") 
				# self.add_key(x=4*self.__keyboard_size, y=0, color = (127, 127, 127), word="e") # gray
				# self.add_key(x=6*self.__keyboard_size, y=0, color = (0, 0, 0), word="r") 
				# self.add_key(x=8*self.__keyboard_size, y=0, color = (127, 127, 127), word="t") # gray

	def write_word(self, x=0, y=0, word_color=(0, 255, 255), word=""):
		word_size = 1
		word_position = (x+self.__keyboard_size//2, y+self.__keyboard_size//2)
		word_color = (0, 255, 255)
		word_thickness = 1
		word_lineType =  cv2.LINE_AA
		cv2.putText(self.__keyboard_img, word, word_position, cv2.FONT_HERSHEY_DUPLEX, word_size, word_color, word_thickness, word_lineType)

	def add_key(self, x=0, y=0, color=(0, 0, 0)):    
		left_up = (x, y)  
		right_down =  (x+self.__keyboard_size, y+self.__keyboard_size)
		thickness = -1 # 寬度 (-1 表示填滿)
		cv2.rectangle(self.__keyboard_img, left_up, right_down, color, thickness) 

		


if __name__ == '__main__':	
	my_keyboard = CV_KEYBORAD(keyboard_array)
	
