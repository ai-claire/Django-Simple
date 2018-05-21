import sys
import os

class SysArgs(object):
	def __init__(self,args_list):
		self.args_list = args_list
		self.args_len = len(self.args_list)
		self.path = os.getcwd()

	def check_args(self):
		if self.args_len > 3 or self.args_len == 1:
			print ("Invalid Arguments")
			print ("Use -h for syntax")
			return 0
		if self.args_len == 2:
			print ("Python [Project Name] [App Name]")
			return 0

	def print_all(self):
		print (self.args_list)
		print (self.args_len)

	def markers(self):
		print ("***************")

	def EditFile(self,filename):
		with open(filename) as Edit:
			content = Edit.read()
		return content

	def makefile(self,filename):
		os.system("touch "+filename)


def main():
	sysargs = SysArgs(sys.argv)
	print ("\n\n")
	sysargs.markers()
	if sysargs.check_args() == 0:
		sysargs.markers()
		print ("\n")
		return 0
	else:
		print ("Cool\n")
		os.system("django-admin startproject "+str(sysargs.args_list[1]))
		print ("Project created...\n")
		os.chdir(sysargs.path+"/"+sysargs.args_list[1])
		os.system("python3 manage.py startapp "+str(sysargs.args_list[2]))
		print ("App Created")
		os.chdir(sysargs.path+"/"+sysargs.args_list[1]+"/"+sysargs.args_list[1])
		print ("Adding Home IP to settings.py")
		print ("Editing Project's Urls.")
		os.remove('urls.py')
		sysargs.makefile('urls.py')
		f = open ('urls.py','w')
		f.write(
				"from django.contrib import admin\n\
from django.urls import path,include\n\
urlpatterns = [\n\
    path('admin/', admin.site.urls),"+"path('"+sysargs.args_list[2]+"/',include('"+sysargs.args_list[2]+".urls')),]")
		f.close()
		os.chdir(sysargs.path+"/"+sysargs.args_list[1]+"/"+sysargs.args_list[2])
		sysargs.makefile('urls.py')
		f = open ('urls.py','w')
		f.write(
			"from django.conf.urls import url\n\
from . import views\n\
\
urlpatterns = [url(r'^$', views.index, name='index'),\
]")
		f.close()
		f = open ('views.py','w')
		f.write('from django.http import HttpResponse\n\
def index(request):\n\
	return HttpReponse("Okay!")')
		f.close()
		os.chdir(sysargs.path+"/"+sysargs.args_list[1])
		os.system("python3 manage.py migrate")
		print ("Migration done!")



if __name__ is main():
	main()
#sysargs.print_all()
