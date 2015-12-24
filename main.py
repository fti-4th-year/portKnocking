import inotify.adapters
from subprocess import call
i = inotify.adapters.Inotify()
path = '/home/anton/dev/python/PortKnocking'
i.add_watch( path )
def callback():
	
	call( [ "python" , "server.py" , "8666" , "False" ] )
try:
	for event in i.event_gen():
		if event is not None and:
			( header , type_names , watch_path , filename ) = event
			#print type_names[ 0 ] , filename
			if type_names[ 0 ] == 'IN_CLOSE_WRITE' and filename == 'test.txt':
				callback()
finally:
	i.remove_watch( path )
