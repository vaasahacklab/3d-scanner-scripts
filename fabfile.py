from fabric.api import env
from fabric.operations import local, run, get

env.hosts = [
	'10.15.1.1',
	'10.15.1.2',
	'10.15.1.3',
]
env.user = 'root'
env.password = 'raspbian'

def copy():
	local('mkdir -p images')
	#run('mkdir -p /home/frodo/tmp')
	get('/SDCard/Pictures/*', "images/%(host)s_%(basename)s")
	run('rm /SDCard/Pictures/*')

def list():
	run('ls /SDCard/Pictures/')
