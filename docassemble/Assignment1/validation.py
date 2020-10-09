# check NRIC format
import re
from docassemble.base.util import * 

def check_nric(string):
  if not re.match(r'[STGF][0-9]{7}[A-Z]',string):
    validation_error('Wrong NRIC format')
#you changed the string positions all by +1
  if string[0] == 'G' or string[0] == 'T':
    d0 = 4
  else:
    d0 = 0

  d1 = int(string[1])
  d2 = int(string[2])
  d3 = int(string[3])
  d4 = int(string[4])
  d5 = int(string[5])
  d6 = int(string[6])
  d7 = int(string[7])
  sumproduct = (d1*2)+(d2*7)+(d3*6)+(d4*5)+(d5*4)+(d6*3)+(d7*2)
  d = (d0 + sumproduct)%11

  if string[0] == 'S' or string[0] == 'T':
    if d == 10 and string[8] == 'A':
      return True
    elif d == 9 and string[8] == 'B':
      return True
    elif d == 8 and string[8] == 'C':
      return True
    elif d == 7 and string[8] == 'D':
      return True
    elif d == 6 and string[8] == 'E':
      return True
    elif d == 5 and string[8] == 'F':
      return True
    elif d == 4 and string[8] == 'G':
      return True
    elif d == 3 and string[8] == 'H':
      return True
    elif d == 2 and string[8] == 'I':
      return True
    elif d == 1 and string[8] == 'Z':
      return True
    elif d == 0 and string[8] == 'J':
      return True
    else:
      validation_error('Invalid NRIC Number')
  elif string[0] == 'F' or string[0] == 'G':
    if d == 10 and string[8] == 'K':
      return True
    elif d == 9 and string[8] == 'L':
      return True
    elif d == 8 and string[8] == 'M':
      return True
    elif d == 7 and string[8] == 'N':
      return True
    elif d == 6 and string[8] == 'P':
      return True
    elif d == 5 and string[8] == 'Q':
      return True
    elif d == 4 and string[8] == 'R':
      return True
    elif d == 3 and string[8] == 'T':
      return True
    elif d == 2 and string[8] == 'U':
      return True
    elif d == 1 and string[8] == 'W':
      return True
    elif d == 0 and string[8] == 'X':
      return True
    else:
      validation_error('Invalid NRIC Number')