#!/usr/bin/python3
import argparse
import sys
import binascii
from PIL import Image, ImageMath

# COLOR CODES
CRESET = '\33[0m'
CGREEN = '\33[32m'
CRED   = '\33[31m'


# Purpose:	attempt to get the image with the PIL module 
# Returns:	a copy of the image so the original image doesn't change at all
def get_image(img):
	try:
		# open the image in read only mode so we don't modify the original image
		image = Image.open(img, 'r')
	except IOError:
		print("[-] Error opening image {}".format(img))
		sys.exit()
	return image.copy()


# Purpose:	see if the message passed to appa can actually fit in the image 
# Returns:	status of this check
def text_fits(message, image):
	image_size = get_pixel_count(image)
	if len(message)*3 > image_size:
		print(CRED + "[!] Image not large enough for the message!" + CRESET)
		print("Image size: {}".format(image_size))
		print("Pixels needed for message: {}".format(len(message*3)))
		return False
	else:			
		print("==> Image data")
		print("\tImage size: {}".format(image_size))
		print("\tPixels needed for message: {}\n".format(len(message*3)))
		return True


# Purpose:	get the number of pixels in the image to ensure the message we are trying to 
#			inject will fit 
# Returns:	the number of pixels in the image
def get_pixel_count(image):
	width, height = image.size
	return width * height


# Purpose:	convert the message provided to appa to binary 
# Returns:	the binary version of the message with a space separating each letter 
def get_binary_string(msg):
	bin_list = [bin(ord(x))[2:].zfill(8) for x in msg]
	print("==> Binary string data")
	print("\tLetters from message [{}] in binary:".format(msg))
	for bin_string in bin_list:
		print("\t{}".format(bin_string))
	binary_msg = ''.join(bin_list)
	print()
	return binary_msg


# Purpose:	get the specific pixels from the image that we are going to modify
# Notes:	we need 3 * the length of the message pixels because letters are 8 bit 
def get_pixels(pixel_count, image):
	pixels = list(image.getdata())[0:pixel_count]
	if debug: print_status("PIXELS TO BE MODIFIED:\n", pixels)
	print("==> Pixel data")
	return pixels


# Purpose:	get the bitmaps for every letter in the message we are encoding 
# Yields:	a list of every set of pixels that needs to be changed  
def get_bitmaps(pixels):
	start = 0
	end = 3
	ascii_len = int(len(pixels) / 3)
	
	for x in range(0, ascii_len):
		bitmap = pixels[start:end]
		if debug: print_status("", bitmap)
		
		yield list(bitmap[0])
		yield list(bitmap[1])
		yield list(bitmap[2])
		
		start+=3
		end+=3

	return


def mod_bitmap(bitmap, bstring):
	print("==> Bitmap modification")

	bitmap = list(bitmap)

	# for parsing through the binary string that is 8 bit 0's and 1's
	bstring_start = 0
	bstring_end   = 8

	# for parsing through the current substring that maps to the pixel list
	substring_start = 0
	substring_end   = 3

	# keep track of when we are at the end of the pixel list for a single letter
	end_pixel_list = 0
	
	for x in range(0, len(bitmap)):
		p = 0

		if x%3 == 0: 
			substring = bstring[bstring_start:bstring_end]
			bstring_start+=8
			bstring_end+=8
			substring_start = 0
			substring_end   = 3
			print("\t(", end="")

		for y in substring[substring_start:substring_end]:
			if y == "0":
				if is_even(bitmap[x][p]):
					print("{}".format(bitmap[x][p]), end=", ")
				else:
					if bitmap[x][p] == 0:
						bitmap[x][p]+=1
					else:
						bitmap[x][p] -= 1
					print(CGREEN + "{}".format(bitmap[x][p]) + CRESET, end=", ")
				if debug:
					print("Needs to be even ", end=", ")
					print(bitmap[x][p])
			else:
				if is_even(bitmap[x][p]):
					if bitmap[x][p] == 0:
						bitmap[x][p] += 1
					else:
						bitmap[x][p] -= 1
					print(CGREEN + "{}".format(bitmap[x][p]) + CRESET, end=", ")
				else:
					print("{}".format(bitmap[x][p]), end=", ")
				if debug:
					print("Needs to be odd ", end="")
					print(bitmap[x][p])
			p+=1
			
		if end_pixel_list == 2:
			# set the last bit of the pixel list
			# odd: end of changes
			# even: more changes to be made

			# we are on the last bit value - make it odd
			if x == len(bitmap)-1:
				# change to odd to terminate changes
				if is_even(bitmap[x][2]):
					if bitmap[x][2] == 0:
						bitmap[x][2]+=1
					else:
						bitmap[x][2]-=1
					print(CGREEN + "{}".format(bitmap[x][2]) + CRESET + ")")
				else:
					print("{})".format(bitmap[x][2]))
			elif is_even(bitmap[x][2]):
				print("{})".format(bitmap[x][2]))
			else:
				if bitmap[x][2] == 0:
					bitmap[x][2]+=1
				else:
					bitmap[x][2]-=1
				print(CGREEN + "{}".format(bitmap[x][2]) + CRESET + ")")
			end_pixel_list = 0
		else:
			end_pixel_list+=1
		
		substring_end+=3
		substring_start+=3

		if debug: 
			print(bitmap[x][0])
			print(bitmap[x][1])
			print(bitmap[x][2])

	print()
	return bitmap


def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False


def inject_bitmap(bitmap, img):
	width = img.size[0]
	(x, y) = (0, 0)
	for pixel in bitmap:
		img.putpixel((x, y), tuple(pixel))
		if x == width-1:
			x=0
			y+=1
		else:
			x+=1
	pixels = get_pixels(len(bitmap), img)
	print("\tPixels after bitmap injection:")
	print("{}".format(pixels))
	print()
	return img


def decode(img):
	pixels = get_pixels(get_pixel_count(img), img)
	print("\tFirst 3 pixels/possible text: {}".format(pixels[0:3]))
	if is_even(pixels[2][2]):
		i=2
		while is_even(pixels[i][2]):
			print("\tPossible text found at pixels[{}]".format(pixels[i]))
			i+=3
		print()
		bstring = translate_pixels(pixels[0:i+1])
		string = translate_from_binary(bstring)
	else:
		i=2
		while not is_even(pixels[i][2]):
			i+=3
		print("possible data found at pixels[{}][2]".format(i))
		while is_even(pixels[i][2]):
			#print("\tPossible text found at pixels[{}]".format(i))
			i+=3
		print()
		bstring = translate_pixels(pixels[0:i+1])
		string = translate_from_binary(bstring)
	return string


def translate_pixels(bitmap):
	bstring = ""
	i = 0
	print("==> Translating each pixel for possible text")
	print("\t{}".format(bitmap))
	for byte in bitmap:
		for b in byte:
			if int(b)%2 == 0:
				bstring+="0"
			else:
				bstring+="1"
			i+=1
	
	return bstring


def translate_from_binary(bstring):
	string=""
	for b in range(0, len(bstring),9):
		print("\t{}".format(bstring[b:b+8]), end=" = ")
		st = chr(int(bstring[b:b+8],2))
		print(st)
		string+=st
	print()
	return string


def save_string(string, image_name):
	fname = image_name.split('.')
	output_file = fname[0] + ".results"
	f = open(output_file, "w+")
	f.write(string)
	f.close()
	return output_file


# Purpose:	print the status to the screen when in debug mode 
#			with fancy formatting that now doesn't have to be copied & pasted a ton
def print_status(message, value):
	print(CGREEN + "\n[!] " + CRESET, end="")
	print("{} {}\n".format(message, value))
	return


if __name__ == "__main__":
	global debug
	global report
	debug = False
	report = False

	parser = argparse.ArgumentParser(description="Interactive steganography")

	parser.add_argument("image",
			help="Image to inject a message into or decode")
	parser.add_argument("-e", "--encode", 
			help="Encode image with text [encode]")
	parser.add_argument("-d", "--decode", action="store_true",
			help="Decode image")
	parser.add_argument("-db", "--debug", action="store_true",
			help="Debug mode")

	args = parser.parse_args()

	if not args.encode and not args.decode:
		print("Choose to either encode or decode image")
		sys.exit()

	if args.debug:
		debug = True

	if args.encode:
		print("==> Encoding image: {}\n".format(args.image))
		image = get_image(args.image)

		if not text_fits(args.encode, image):
			print("Message too large for image. Please find a bigger image")
			sys.exit()

		pixel_count = len(args.encode)*3

		pixels = get_pixels(pixel_count, image)
		print("\tPixels to be modified:\n{}\n".format(pixels))

		bstring = get_binary_string(args.encode)
		bitmap = get_bitmaps(pixels)
		new_bitmap = mod_bitmap(bitmap, bstring)
		new_img = inject_bitmap(new_bitmap, image)
		fname = args.image.split('.')
		print("==> Saving new image")
		new_image_name = fname[0] + "_new" + ".png"
		print("\tModified image: {}".format(new_image_name))
		new_img.save(new_image_name)

	if args.decode:
		print("==> Decoding image: {}\n".format(args.decode))
		image = get_image(args.image)
		string = decode(image)
		if len(string) > 10:
			output_file = save_string(string, args.image)
			print("Appa found an extremely large string in the image. To save your console, results are saved to file: {}".format(output_file))
			print("String length: {}".format(len(string)))
		else:
			print("{}".format(string))
