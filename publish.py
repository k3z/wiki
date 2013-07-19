#!/usr/bin/python
import os

here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

os.system("make html")
os.system("rsync -r --delete %s root@k3z.fr:/home/k3zfr/wiki/" % here('build/html/'))
