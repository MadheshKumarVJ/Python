import re
#balls in string
balls ="red Green blue orange green white green yellow red green red green blue orange green white green yellow red green red green blue orange green white green yellow red green"
#search pattern a for green ball
search_pattern_of_green_ball="green"
#finding all green balls and storing it in a list
green_balls= re.findall(search_pattern_of_green_ball,balls,flags=re.I)
#itha na kandu pidichathi
print(green_balls)