#!/usr/bin/python

# import argparse
import sys
import math
 
# Function that returns normal vector values 
def normal_finder(p1x, p1y, p1z, p2x, p2y, p2z, p3x, p3y, p3z):
	a1  = p1x-p2x;
	a2  = p1y-p2y;
	a3  = p1z-p2z;
	b1  = p3x-p2x;
	b2  = p3y-p2y;
	b3  = p3z-p2z;
	# Normal (n1,n2,n3) calculated as cross product of v1 and v2
	n1  = ((a2*b3)-(a3*b2));
	n2  = ((a3*b1)-(a1*b3));
	n3  = ((a1*b2)-(a2*b1));

	m   = math.sqrt((n1*n1) + (n2*n2) + (n3*n3));

	if m != 0:
		n1 /= m;
		n2 /= m;
		n3 /= m;
			
	print (n1, n2, n3)

normal_finder(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]))

	
