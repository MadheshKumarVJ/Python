import re
#balls in string
balls ="Red Green blue orange green white green yellow red green red green blue orange green white green yellow red green red green blue orange green white green yellow red green"

#pattern need to be replaced
search_pattern_of_green_ball=r"red"
#repalcing red with orange
bucket= re.sub(search_pattern_of_green_ball,"orange",balls,count=1,flags=re.I)

#shows the result 
print(bucket)
