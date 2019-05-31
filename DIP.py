## This is the reference 

## The following part defines all the exceptions used in Homework 7.1 and 7.2
## Please DO NOT MODIFY THE EXCEPTIONS!
import math

class PixelSyntaxError(Exception):
	pass

class MatrixSizeError(Exception):
	pass

class PixelBitError(Exception):
	pass

class BitUnmatchedError(Exception):
	pass

class ImageSizeUnmatchedError(Exception):
	pass

class KenelElementError(Exception):
	pass

class PixelNegError(Exception):
	pass

class IndexSyntaxError(Exception):
	pass

## =================== End of Exception Definition ===========================

## Feel free to add self-defined functions and classes here

## TreeNode from Leetcode
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

## =================== End of Self-Defined Functions and Classes ===========================

## The following is a template class Image where all your implementations is.
## Augments of each method may not be well developed, you should complete those augments by yourself

class Image:
	def __init__(self, s, n = 8):

		'''
		Task 1.1
		'''
		pass

	def __str__(self):

		'''
		Task 1.2
		'''
		raise NotImplementedError
	
	def __add__(self, other):

		'''
		Task 2
		'''
		raise NotImplementedError

	def __eq__(self, other):

		'''
		Task 2
		'''
		raise NotImplementedError
	
	def reverse(self):

		'''
		Task 3
		'''
		raise NotImplementedError

	def bitChange(self, n_new = 8):
		
		'''
		Task 4
		'''
		raise NotImplementedError
	
	def __getitem__(self,key):
		
		'''
		Task 5
		'''
		raise NotImplementedError
	
	def __setitem__(self, key, value):

		'''
		Task 5
		'''
		raise NotImplementedError

	def his(self):

		'''
		Task 6.1
		'''
		raise NotImplementedError
	
	def hiseq(self):

		'''
		Task 6.2
		'''
		raise NotImplementedError

	## ======================== End of Homework 7.1 ===============================

	## ======================== Beginning of Homework 7.2 =========================
	
	def __mul__(self, kernel_str):
		
		'''
		Task 7
		'''
		raise NotImplementedError

	def huffman(self):

		'''
		Task 8
		'''
		raise NotImplementedError

	## ======================== End of Homework 7.2 ===============================

## Testing Part
if __name__ == "__main__":
	### Test for empty matrix

	img1 = Image('[]',2)
	if str(img1) == '[]':
		print('Pass Test 1')
	else:
		print('Fail Test 1')

	### Test for PixelSyntaxError
	try:
		img2 = Image('[12,3333333333333333+j,2,3]',8)
	except PixelSyntaxError:
		print('Pass Test 2')
	else:
		print('Fail Test 2')

	### Test for MatrixSizeError

	try:
		img3 = Image('[1;1;2,3]')
	except MatrixSizeError:
		print('Pass Test 3')
	else:
		print('Fail Test 3')

	### Test for PixelBitError

	try:
		img4 = Image('[1,1,1,1]', -1)
	except PixelBitError:
		print('Pass Test 4')
	else:
		print('Fail Test 4')

	## Test for priting out image

	img5 = Image('[1,2,3; 4,5,6; 7,8,9]')
	if str(img5) == '[1,2,3;4,5,6;7,8,9]':
		print('Pass Test 5')
	else:
		print('Fail Test 5')

	## Test for Image Addtion

	img6 = Image('[1,2,3; 4,5,6; 7,8,9]')
	img7 = Image('[1,2,3; 4,5,6; 7,8,9]')

	if str(img6+img7) == '[2,4,6;8,10,12;14,16,18]':
		print('Pass Test 6')
	else:
		print('Fail Test 6')

	## Test for PixelExceedingError

	img8 = Image('[1,2,3; 4,5,6; 7,8,9]',4)
	img9 = Image('[1,2,3; 4,5,6; 7,8,9]',4)

	try:
		img10 = img8 + img9
	except PixelSyntaxError:
		print('Pass Test 7')
	else:
		print('Fail Test 7')

	## Test for BitUnmatchedError

	img11 = Image('[1,2,3; 4,5,6; 7,8,9]',11)
	img12 = Image('[1,2,3; 4,5,6; 7,8,9]',10)

	try:
		img13 = img11 + img12
	except BitUnmatchedError:
		print('Pass Test 8')
	else:
		print('Fail Test 8')

	## Test for ImageSizeUnmatchedError

	img14 = Image('[1,2,3; 4,5,6]')
	img15 = Image('[1,2,3; 4,5,6; 7,8,9]')

	try:
		img16 = img14 + img15
	except ImageSizeUnmatchedError:
		print('Pass Test 9')
	else:
		print('Fail Test 9')

	## Test for Gray Scale Reversion

	img16 = Image('[1,2,3,4;5,6,7,8]')
	img17 = img16.reverse()

	if img17 == Image('[254,253,252,251;250,249,248,247]'):
		print('Pass Test 10')
	else:
		print('Fail Test 10')

	## Test for Bit Extension and Compression

	img18 = Image('[4,8,12,16;20,24,28,32]', 16)
	img18_1 = img18.bitChange()
	img19 = Image('[1,2,3,4;5,6,7,8]', 4)
	img19_1 = img19.bitChange(8)

	if img18_1 == img19_1:
		print('Pass Test 11.1')
	else:
		print('Fail Test 11.1')

	img19_2 = img19.bitChange(7)

	if img18_1 != img19_2:
		print('Pass Test 11.2')
	else:
		print('Fail Test 11.2')

	## Test for Image Indexing
	img20 = Image("[1,2,3; 4,5,6; 7,8,9]")
	img21 = Image("[0,1,2; 3,4,5; 6,7,8]")
	z = img20[2]

	if z == '[7,8,9]':
		print('Pass Test 12.1')
	else:
		print('Fail Test 12.1')

	if img20[2,1] == 8:
		print('Pass Test 12.2')
	else:
		print('Fail Test 12.2')

	if img20[1:3:1,0:3:2] == '[4,6;7,9]':
		print('Pass Test 12.3')
	else:
		print('Fail Test 12.3')

	img20[2] = Image("[17,18,19]")
	if str(img20) == '[1,2,3;4,5,6;17,18,19]':
		print('Pass Test 12.4')
	else:
		print('Fail Test 12.4')

	img20[1,2] = 0
	if str(img20) == '[1,2,3;4,5,0;17,18,19]':
		print('Pass Test 12.5')
	else:
		print('Fail Test 12.5')

	img20[1:3:1,0:3:2] = Image("[14,16;7,9]")
	if str(img20) == '[1,2,3;14,5,16;7,18,9]':
		print('Pass Test 12.6')
	else:
		print('Fail Test 12.6')

	## Test for Histogram
	img21 = Image("[1,2,3; 4,5,6; 7,8,9]", 4)
	h = img21.his()
	if h == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]:
		print('Pass Test 13')
	else:
		print('Fail Test 13')

	## Test for Histogram Equalization
	img21 = Image("[1,1,3; 4,4,5; 7,7,7]", 4)
	img21_his = img21.hiseq()
	if img21_his == Image('[3,3,4;8,8,9;14,14,14]',4):
		print('Pass Test 14')
	else:
		# print(img21_his)
		print('Fail Test 14')

	## Test for Convolution
	img22 = Image("[1,1,3; 4,4,5; 7,7,7]", 100)
	kernel = '[1,1,1;1,1,1;1,1,1]'

	img23 = img22 * kernel
	if img23 == Image('[10,18,13;24,39,27;22,34,23]',100):
		print('Pass Test 15')
	else:
		print('Fail Test 15')

	try:
		img24 = img22 * '[1,1,1;1,1,1;1,1]'
	except MatrixSizeError:
		print('Pass Test 16.1')
	else:
		print('Fail Test 16.1')

	try:
		img25 = img22 * '[1,1,1;1,1,1;1,1,1.1]'
	except KenelElementError:
		print('Pass Test 16.2')
	else:
		print('Fail Test 16.2')

	try:
		img26 = img22 * '[-1,-1,-1;-1,-1,-1;-1,-1,-1]'
	except PixelNegError:
		print('Pass Test 16.3')
	else:
		print('Fail Test 16.3')

	## Test for Huffman Coding

	img27 = Image('[1,2,2,3,3,3;4,4,4,4,5,5;5,5,5,5,7,7;7,7,7,7,7,7;7,7,7,7,3,3]')
	if img27.huffman() == '100010011001110110110101101101101111111111111111111000000000000110110':
		print('Pass Test 17.1')
	else:
		print('Fail Test 17.1')

	img28 = Image('[1,2,2,3,5,3;3,3,4,4,5,3;4,4,5,5,5,3]')
	if img28.huffman() == '000001001111011111101011011010110101011':
		print('Pass Test 17.2')
	else:
		print('Fail Test 17.2')
