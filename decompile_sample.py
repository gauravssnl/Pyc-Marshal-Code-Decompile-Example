# Code for generating pyc file
import os

output_dir = os.path.join(os.getcwd(), "pyc")
if not os.path.exists(output_dir):
	os.mkdir(output_dir)
	print("Output path created to store pyc files.")
with open(output_dir + "/" + __file__ + "c", "wb") as f:
	# first 4 bytes represent magic code , second 4 bytes represent timestamp
	f.write('\x03\xf3\x0d\x0a\0\0\0\0')
	f.write(code)
	print("PYC file generated succesfully")
