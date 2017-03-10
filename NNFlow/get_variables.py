#Script to get variables from a ROOT file
#Only variables which appear in the wish list will be saved in the variable list. For example generator level variables can be sorted out this way.
#Usage: python get_variables.py /path/to/root/file /path/to/wish/list /path/to/outputfile/for/variable/list /path/to/outputfile/for/vector/like/variables name_of_ROOT_TTree


import sys
import ROOT


path_infile_root                   = sys.argv[1]
path_infile_wishlist               = sys.argv[2]
path_outfile_variablelist          = sys.argv[3]
path_outfile_vector_like_variables = sys.argv[4]
treename                           = sys.argv[5]


infile_root = ROOT.TFile(path_infile_root)
tree = infile_root.Get(treename)
branchlist = tree.GetListOfBranches()


with open(path_infile_wishlist, 'r') as infile_wishlist:
  wishlist = [line.rstrip() for line in infile_wishlist.readlines()]


with open(path_outfile_variablelist, 'w') as outfile_variablelist:
  with open(path_outfile_vector_like_variables, 'w') as outfile_vector_like_variables:
    for branch in branchlist:
      if branch.GetName() in wishlist:
        outfile_variablelist.write(branch.GetName() + '\n')
        if ('[' in branch.GetTitle() and ']' in branch.GetTitle()):
          outfile_vector_like_variables.write(branch.GetName() + '\n')
