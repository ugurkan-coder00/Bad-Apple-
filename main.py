import os 
import cv2
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resized_image(image ,new_width=75):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	resized_image = image.resize((new_width,new_height)).convert('L')
	return resized_image

def pix2chars(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

def frame_ss(image,new_width=75):
	new_image_data = pix2chars(resized_image(image))
	total_pixels = len(new_image_data)
	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])
	print(ascii_image)
	
video = cv2.VideoCapture("video.mp4")

while True:
	ret,framee = video.read()
	cv2.imshow("frame",framee)
	frame_ss(Image.fromarray(framee))
	cv2.waitKey(1)
