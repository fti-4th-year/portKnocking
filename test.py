import socket
import sys
s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
s.connect( ( "127.0.0.1" , int( sys.argv[ 1 ] ) ) )
s.send( 'hello' )
buf = s.recv( 64 )
print buf
