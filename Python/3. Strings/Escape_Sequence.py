from codecs import backslashreplace_errors
from multiprocessing.context import SpawnContext
from cv2 import line


a="My Name is Ahmad ali"
print(a)
    # ESCAPE SEQUENCE 
    # ==>  \n \t \f \b \\ \' \"
''' \n => for new line
    \t => for tab Space
    \f => for formfeed
    \b => for backspace
    \\ => for \
    \' => for '
    \" => for "
'''
b= '''I\n need\t \" food'''
print(b)