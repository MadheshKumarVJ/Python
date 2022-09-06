import os, glob

#list will be retured 
[f for f in glob.glob('*Dec*.py')]
#dict (key:value)
{f:os.stat(f).st_size for f in glob.glob('*Dec*.py')}
#as same as dict with out key:value only value -->set
{f for f in glob.glob('*Dec*.py')}