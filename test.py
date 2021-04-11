# import the necessary packages
# import argparse
import cv2
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
point_list = []
cropping = False
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global point_list, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		point_list = [(x, y)]
		cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		point_list.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		# cv2.rectangle(image, point_list[0], point_list[1], (0, 255, 0), 2)
		# cv2.imshow("image", image)

		
			
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
# load the image, clone it, and setup the mouse callback function

def main():
	image_path = "C:\\Users\\howar\\Desktop\\23.PNG"
	image = cv2.imread(image_path)
	clone = image.copy()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", click_and_crop)
	# keep looping until the 'q' key is pressed
	while True:
		# display the image and wait for a keypress
		cv2.imshow("image", image)
		key = cv2.waitKey(1) & 0xFF
		# if the 'r' key is pressed, reset the cropping region
		if key == ord("r"):
			image = clone.copy()
		# if the 'c' key is pressed, break from the loop
		elif key == ord("c"):
			break

		if len(point_list) >= 2:
			left, right = (point_list[0][1],  point_list[1][1]) if point_list[0][1] < point_list[1][1] else (point_list[1][1],  point_list[0][1])
			top, down = (point_list[0][0],  point_list[1][0]) if point_list[0][0] < point_list[1][0] else (point_list[1][0],  point_list[0][0])

			roi = clone[left:right, top:down]
			cv2.imshow("ROI", roi)
			# cv2.waitKey(0)
	# if there are two reference points, then crop the region of interest
	# from teh image and display it
	# if len(point_list) >= 2:
	# 	roi = clone[point_list[0][1]:point_list[1][1], point_list[0][0]:point_list[1][0]]
	# 	cv2.imshow("ROI", roi)
	# 	cv2.waitKey(0)
	# close all open windows
	cv2.destroyAllWindows()	


if __name__ == '__main__':	
	main()  

