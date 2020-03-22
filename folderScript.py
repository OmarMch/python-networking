#!/usr/bin/python3

import os

# detect the current directory and print it
# _path_dir = os.getcwd()

pathname = 1

# define the name of the directory to be created(replace "path" with own)
path_dir = "/home/och/Git/python-networking/Chapter_" + str(pathname)

# folder access rights 
access_rights = 0o777


while pathname < 14:
    if not os.path.exists(path_dir):
        os.makedirs(path_dir, access_rights)
    pathname += 1
    # replace "path" as well.
    path_dir = "/home/och/Git/python-networking/Chapter_" + str(pathname)
    print("Successfuly created the directory %s" % pathname)



