import numpy as np		#we use numpy for a lot of things

def main():
	i=0		#integer i and initialize i to 0
	n=10	#integer n, with value 10
	x=119.0	#float x with value 119
	
	#can use numpy to declare arrays quickly
	
	y=np.zeros(n,dtype=float)	#declares 10 zeros
	
	#we can iterate trough the elements of y
	#by passing an index
	
	for i in range(n):	#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.0		#set y = 2i+1 as float
		
	#we can also simply iterate through an array
	for y_element in y:
		print(y_element)
		
#execute the main function
if __name__ == "__main__":
	main()