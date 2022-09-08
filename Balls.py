import re
#balls in string
balls ="red Green blue orange green white green yellow red green red green blue orange green white green yellow red green red green blue orange green white green yellow red green"

#search pattern a for green ball and yellow ball
search_pattern_of_green_ball=r"(\bgreen+\b).+(\byellow+)"
#finding all green balls position and storing it in a object
green_balls= re.search(search_pattern_of_green_ball,balls,flags=re.I)

#shows the result if they exist
print(green_balls.groups())
#first group
print(green_balls.group(1))
#second group
print(green_balls.group(2))