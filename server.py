import socket
import sys
try:
	s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
	s.bind( ( 'localhost' , int( sys.argv[ 1 ] ) ) )
	s.listen( 10000 )
	must_log = bool( sys.argv[ 2 ] )
	while True:
		sock , addr = s.accept()
		msg = sock.recv( 255 )
		print addr[0] , addr[ 1 ] , msg
		sock.close()
		if must_log:
			f = open( 'test.txt' , 'a' )
			i1 = int( addr[ 1 ] ) / 255
			i2 = 
			f.write( "{}:{}->{}\n".format( addr[ 0 ] , addr[ 1 ] , msg ) )
			f.close()
finally:
	s.close()
