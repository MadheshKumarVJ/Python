import re
#balls in string
balls ="red Green blue orange green white green yellow red green red green blue orange green white green yellow red green red green blue orange green white green yellow red green"

#search pattern a for green ball
search_pattern_of_green_ball="green"

#finding all green balls position and storing it in a object
green_balls= re.finditer(search_pattern_of_green_ball,balls,flags=re.I)

#when you iterate it you will show all the positions
for green_ball in green_balls:
    print(green_ball)