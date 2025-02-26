# modules and pip in python 

# python -m venv .venv
# source .venv/bin/activate
# pip install <package_name>
import pandas 
import hashlib
print(hashlib.md5(b"hello").hexdigest())
print(pandas.__version__)