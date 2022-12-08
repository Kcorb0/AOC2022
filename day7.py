inp_path = open("day7_input.txt", "r").read().split("\n")

# Outer most directory is /
# $        = User executed commands
# cd       = change dir
# cd ..    = go back
# cd /     = root dir
# ls       = list dir contents
# 123 abc  = size and name of file
# dir xyz  = dir contains 'xyz'

directories = {}  # {Key=Dir: Val=[filesize, filesize]}
