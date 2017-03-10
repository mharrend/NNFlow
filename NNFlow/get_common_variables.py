#Script to get common variables from two lists of variables
#Usage: python get_common_variables.py /path/to/first/inputfile /path/to/second/inputfile /path/to/outputfile

import sys

with open(sys.argv[1], 'r') as v1_file:
  with open(sys.argv[2], 'r') as v2_file:
    with open(sys.argv[3], 'w') as outfile:
      v1_list = [a.split()[0] for a in v1_file.readlines()]
      v2_list = [a.split()[0] for a in v2_file.readlines()]

      for a in v1_list:
        if a in v2_list:
          outfile.write(a + '\n')
