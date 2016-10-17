#!/usr/bin/env
import os

import getopt 
import sys

#Transmission Delay  in millisecond
# t Mbps
# M Mbits
def transDelay(t,M):
	return (M/t)*10**3

#Propagation Delay   in millisecond
#d KM
#S 10^8 m/s
def propDelay(d,S):
	return d/(S*100)

def main():

	t1,t2,d1,d2,N,M,S,p = 1,1,1,1,1,1,1,1 #Default 
	try:

		opts, args = getopt.getopt(sys.argv[1:],'N:M:S:p:',['t1=','t2=','d1=','d2=','help'])
		if len(opts) == 0 :

			print """Please use the correct arguments, for usage type --help  """
			sys.exit(2)

	except getopt.GetoptError,err: 
		print str(err)
		print """Please use the correct arguments, for usage type --help """
		sys.exit(2) 
	for opt,arg in opts:

		if opt == '--t1':

			t1 = float(arg) 
		elif opt == '--t2':

			t2 = float(arg) 
		elif opt == '--d1':

			d1 = float(arg) 

		elif opt == '--d2':

			d2 =float(arg) 

		elif opt == '-N':

			N = float(arg) 

		elif opt == '-M':

			M = float(arg) 

		elif opt == '-S':

			S = float(arg) 

		elif opt == '-p':

			p = float(arg) 

		elif opt == '--help':

			printHelp()
		else:
			assert False, "unhandled option"

	print '\n%10s%5s%9s%20s%9s%20s%9s' % (""," ","+-------+"," "," ------- "," ","+-------+")
	print '%10s%5s%9s%20s%9s%20s%9s' % ("Packet "," ","| A |","-" * 20,"( R )","-" * 20,"| B	|")

	print '%10s%5s%9s%20s%9s%20s%9s' % ("-" * 10," ","+-------+"," "," ------- "," ","+-------+") 
	n,A,B,queueDelay= 1,0,0,0

	while n<=N:
		R = A + transDelay(t1,M) + propDelay(d1,S)

		B = R + queueDelay + p + transDelay(t2,M) + propDelay(d2,S) 

		if R < transDelay(t2,M):

			queueDelay = queueDelay + transDelay(t2,M) - transDelay(t1,M) 

		print'%10s%2s%9.3f ms%17s%9.3f ms%17s%9.3f ms' % ('P' + `n` + ' ','',A,'',R,'',B)
		n,A = n + 1,A + transDelay(t1,M)

	print "\nEnd to End transmission delay = %9.3f ms\n" %(B) 

def printHelp():

	print """We have multiple options:\n\t--t1: Transmission Delay at Link1 <value in Mbps>\n\ --t2: Transmission Delay at Link2 <value in Mbps>\n\t--d1: Distance of Link1<value in KM>\n\ --d2: Distance of Link2 <value in KM>\n\t -N: Number of Packets <value>\n\t -M: Packet Size
<value in Mbits>\n\ -S: Propagation Speed <speed in 10^8m/s>\n\t -p: Router Processing Time <processing time in milliseconds>"""

	sys.exit()

if __name__ =='__main__':
	main()


# OUTPUT:
# root@kbw-Lenovo-G50-80:~/BE/Execution A  group# python b9.py --t1 10 --t2 12 --d1 2 --d2 1 -N 5 -M 19 -S 2 -p 1

#                +-------+                     -------                     +-------+
#    Packet          | A |--------------------    ( R )--------------------    | B|
# ----------     +-------+                     -------                     +-------+
#        P1       0.000 ms                  1900.010 ms                  3484.348 ms
#        P2    1900.000 ms                  3800.010 ms                  5384.348 ms
#        P3    3800.000 ms                  5700.010 ms                  7284.348 ms
#        P4    5700.000 ms                  7600.010 ms                  9184.348 ms
#        P5    7600.000 ms                  9500.010 ms                 11084.348 ms

# End to End transmission delay = 11084.348 ms

# root@kbw-Lenovo-G50-80:~/BE/Execution A  group# 

