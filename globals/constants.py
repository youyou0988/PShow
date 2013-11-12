from os.path import dirname, join

ROOT = dirname(dirname(__file__))

# The [index] or [permutation] exceed the length should be 
OVERFLOW = -11

#
ERROR = -12

#
WARNING = -13

# length for name
NAMELENGTH = 50

# length for dir
DIRLENGTH = 30

# length for id
IDLENGTH = 20

# length for permutation
PLENGTH = 20

# length for index
ILENGTH = 20

# length for password
PWDLENGTH = 30

DICTIONARY = 0

INCREASE = 1

DECREASE = 2

SWITCH = 3

# default permutation length
DEPLENGTH = 4