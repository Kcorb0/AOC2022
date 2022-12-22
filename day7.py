inp_path = open("day7_input.txt", "r").read().split("\n")

# Task
# Find largest directories


# Outer most directory is /
# $        = User executed commands
# cd       = change dir
# cd ..    = go back
# cd /     = root dir
# ls       = list dir contents
# 123 abc  = size and name of file
# dir xyz  = dir contains 'xyz'

l_directories = {'afsfa': 12415, 'gsbadd': 15531}  # {Key=Dir: Val=[filesize, filesize]}
all_directories = {}
curr_dir = '/'
prev_dir = ''

def change_dir(target):
	
	if target == '..':
		curr_dir = prev_dir
	elif target == '/':
		prev_dir = ''
		curr_dir = '/'
	else:
		prev_dir = curr_dir
		curr_dir = target
	print(curr_dir)
	


for comm in inp_path:

	if '$ cd' in comm:
		cd = comm[4:]
		print(cd)
		change_dir(cd)




print(sum(l_directories.values()))