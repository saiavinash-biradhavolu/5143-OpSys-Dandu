"""
@Program Name: Yo-Shell V1 Starter Code
@Team: Sharath Kumar Dayal, Shashank Namala, Muni Bhupathi Reddy Dandu
@Description:
    This code is a barebones snippet to get your shell up and running. It provides the following classes 
	  interpreter - manages history of commandds , handles parsing of commands into command , arguments, flags and 
	      		gets commands parsed and then runs appropriate functions for command.
"""

import cmd
import os
import time
from stat import *
import sys

"""
@Name: interpreter
@Description:

@Methods:
    history - add command to history
    cat - opens the file   
    copy - copies the content of one file to other file
    remove - removes the file
    move - rename the file
    cd - change the directory
    chmod - add permissions to a file
    wc - Gives the word count, line count and character count of a file
    ls - lists the directory contents
    listing - lists the files in sorting order
    size_convert - converts the size of the files
    display - dispalys the commands in history
    strip - parse the input
"""

class interpreter(cmd.Cmd):

	list_history=[]
	"""
	@Name: history
	@Description:
		Maintains a history of shell commands to be used within a shell environment.
	@Params: 
        	_input (string) - command the user enters
	@Returns: 
		Appends the command to list_history
	"""		
	def history(self,_input):
	
		self.list_history.append(_input)
		
		if _input=="quit":
			print "******************"
			print "Quitting the shell"
			raise SystemExit
			
		elif _input=="history":
			print "history of shell"
			print "****************"
			object.display()
			
		elif "cat" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==3:
			_filename=object.strip(_input)
			if len(_filename)==2 and os.path.exists(_filename[1]):
				object.cat(_filename[1])
			else:
				print "Enter an existing filename"
				
		elif "cp" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==2:
			_filename=object.strip(_input)
			if len(_filename)==3 and os.path.exists(_filename[1]):
				object.copy(_filename[1],_filename[2])
				print "Copy Successful"
			else:
				print "Enter an existing file as argument"
				
		elif "rm" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==2:
			_filename=object.strip(_input)
			if len(_filename)==2 and os.path.exists(_filename[1]):
				object.remove(_filename[1])
				print "Removed the file"
			else:
				print "Enter an existing filename"
				
		elif "mv" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==2:
			_filename=object.strip(_input)
			if len(_filename)==3 and os.path.exists(_filename[1]):
				object.move(_filename[1],_filename[2])
			else:
				print "Enter an existing filename"
				
		elif "cd" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==2:
			_filename=object.strip(_input)
			if len(_filename)==2:
				object.cd(_filename[1])
			else:
				print "Enter correct flag for cd"
				
		elif "chmod" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==5:
			_flag=object.strip(_input)
			if len(_flag)==3:
				object.chmod(_flag[1],_flag[2])
			else:
				print "Syntax Error"
				
		elif "wc" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==2:
			_flag=object.strip(_input)
			if len(_flag)==3 and _flag[1]=="-l":
				object.wc(_flag[2],len(_flag))
			elif len(_flag)==2 and os.path.exists(_flag[1]):
				object.wc(_flag[1],len(_flag))
			else:
				print "Write correct syntax for line count"
		
		elif "ls" in _input.split(' ')[0] and len(str(_input.split(' ')[0]))==2:
			_flag=object.strip(_input)
			length=len(_flag)
			object.ls(_flag,length)
		else:
			print "Check the command"



	"""
	@Name: cat
	@Description:
		Dumps a file 
	@Params: 
        	_filename (string) - The file to be dumped
	@Returns: 
		None
	"""

	def cat(self,_filename):
		f = open(_filename, "r")
		text = f.read()
		print text
		f.close()

	"""
	@Name: copy
	@Description:
		Copies the content of source file to destination file 
	@Params: 
        	_filename1 (string), _filename2 (string) - Source filename and destination filename
	@Returns: 
		None
	"""
		
	def copy(self,_filename1,_filename2):
		path=os.getcwd()
		conc=path+'\%s'%_filename1
		if os.path.exists(_filename1):
			fread=open(_filename1,'r')
			content=fread.read()
			fread1=open(_filename2,'w')
			fread1.write(content)
			fread.close()
			fread1.close()

	"""
	@Name: remove
	@Description:
		Used to remove an existing file.
	@Params: 
        	_filename (string) - file to be removed
	@Returns: 
		None
	"""
			
	def remove(self,_filename):
		if os.path.exists(_filename):
			os.remove(_filename)
			
	"""
	@Name: move
	@Description:
		Used to rename a file
	@Params: 
        	_filename1 (string), _filename2 (string)- old filename and new filename
	@Returns: 
		None
	"""			
			
	def move(self,_filename1,_filename2):
		self.copy(_filename1,_filename2)
		self.remove(_filename1)
		print "Moved the file"

	"""
	@Name: cd
	@Description:
		Used to change the directory. 
	@Params: 
        	flag (string) - the required directory
	@Returns: 
		None
	"""
		
	def cd(self,flag):
	
		if flag=="..":
			x=os.path.dirname(os.getcwd())
			os.chdir(x)
			
		elif flag=="~":
			root=os.path.abspath(os.sep)
			os.chdir(root)	
		
		elif os.path.isdir(os.path.join(os.getcwd(),flag)):
			os.chdir(os.path.join(os.getcwd(),flag))
			
	"""
	@Name: chmod
	@Description:
		Used to assign the required permissions to a file.
	@Params: 
        	_flag1 (string) - required permission which will be converted to integer.
		_flag2 (string) - file on which permissions needs to be changed
	@Returns: 
		None
	"""
	
	def chmod(self,_flag1,_flag2):
		sum=[0,0,0]
		for i in range(len(_flag1)):
			if int(_flag1[i])<=7 and int(_flag1[i])>=0:
				sum[i]=3
			else:
				print "Syntax Error"
				return None
		if os.path.exists(_flag2) and (sum[i]<=3 for w in sum):
			os.chmod(_flag2,int(_flag1,8))
			print "Permissions changed successfully"
		else:
			print "Check the syntax or Filename"

			
	"""
	@Name: wc
	@Description:
		Gives the word count, line count and character count of a file
	@Params: 
        	_flag (string) - filename 
		_size (string) - size of the command
	@Returns: 
		None
	"""
			
	def wc(self,_flag,size):
		path=os.getcwd()+"/%s"%_flag
		length=len(open(os.getcwd()+"/%s"%_flag).readlines())
		if os.path.exists(_flag) and size==3:
			print str(length)+" "+_flag
		else:
			lines=0
			words=0
			chars=0
			for line in open(path).readlines(  ):
				lines=lines+1
				for word in line.split(  ):
					words=words+1
			
			chars=len(open(_flag,'r+').read())
			print("%d %d %d %s" %(lines,words,chars,_flag))

	"""
	@Name: ls
	@Description:
		lists the directory contents.
	@Params: 
        	_flag (string) - the required flag 
		_size (string) - size of the command
	@Returns: 
		None
	"""			
	def ls(self,_flag,size):
		if size==1:
			list=os.listdir(os.getcwd())
			print "File Listing"
			print "------------"
			print '\t\t'.join(list)
			print "------------"
		elif size==2 and (_flag[1]=='-a' or _flag[1]=='-m' or _flag[1]=='-c' or _flag[1]=='-l' or _flag[1]=='-s'):
			object.listing(_flag[1])	
		else:
			print "Enter the correct flag"
	"""
	@Name: listing
	@Description:
		lists the files in sorting order accordding to given flag
	@Params: 
        	flag (string) - required flag
	@Returns: 
		None
	"""
	def listing(self,flag):
		a=['File Name','Size','Permissions','Accessed','Modified','Changed']
		list1=[]
		list2=[]
		list=os.listdir(os.getcwd())
		print('  {0:16s}   {1:9s}   {2:12s}   {3:24s}   {4:24s}   {5:24s} '.format(a[0],a[1],a[2],a[3],a[4],a[5]))
		print('{0:16s}   {1:9s}   {2:12s}   {3:24s}   {4:24s}   {5:24s}'.format("-----------","---------","-------------","----------------","-------------------","-------------------","-------------------"))
		for i in list:
			f=os.stat(os.getcwd()+"/%s"%i)
			if flag=='-a':
				list1.append(f.st_atime)
			elif flag=='-m':
				list1.append(f.st_mtime)
			elif flag=='-c':
				list1.append(f.st_ctime)
			elif flag=='-l':
				list1.append(f)	
			elif flag=='-s':
				list1.append(object.size_convert(f.st_size))
			list2.append(f)
		list1.sort()
		for i in range(0,len(list1)):
			for k in list:
				f=os.stat(os.getcwd()+"/%s"%k)
				st1=os.stat(k)
				if flag=='-a':
					temp1=f.st_atime
				elif flag=='-m':
					temp1=f.st_mtime
				elif flag=='-c':
					temp1=f.st_ctime
				elif flag=='-l':
					temp1=list2[0]
				elif flag=='-s':
					temp1=object.size_convert(f.st_size)
				if list1[i]==temp1:
					Size=object.size_convert(f.st_size)
					Perm=int(oct(os.stat(k)[ST_MODE])[-3:])
					Atime=time.asctime(time.localtime(st1[ST_ATIME]))
					Mtime=time.asctime(time.localtime(st1[ST_MTIME]))
					Ctime=time.asctime(time.localtime(st1[ST_CTIME]))
					print('  {0:16s}   {1:8s}   {2:12d}   {3:24s}   {4:24s}   {5:24s} '.format(k,Size,Perm,Atime,Mtime,Ctime))

	"""
	@Name: size_convert
	@Description:
		converts the size of the files
	@Params: 
		size (string) - size of the file
	@Returns: 
		returns size of the file
	"""							
	def size_convert(self,size):
		suffixes=['B','KB','MB','GB','TB']
		precision=3
		suffixIndex = 0
		while size > 1024 and suffixIndex < 4:
			suffixIndex += 1 #increment the index of the suffix
			size = size/1024.0 #apply the division
		return "%.*f%s"%(precision,size,suffixes[suffixIndex])

	"""
	@Name: display
	@Description:
		displays the history of commands 
	@Params: 
        	None
	@Returns: 
		None
	"""
	
	
	def display(self):
		for i in self.list_history:
			print i

	"""
	@Name: strip
	@Description:
		Parses command into a list. 
	@Params: 
        	_input (string) - The command to be parsed
	@Returns: 
		returns the list 
	"""	
			
	def strip(self,_input):
		_list=_input.split(' ')
		return _list
		
		

if __name__ == "__main__":
	print "\nUser Command Prompt in Python Starts\n"
	print "----------------------------------------"
	while True:
		_input=raw_input(os.getcwd()+"$")
		object=interpreter()
		object.history(_input)

