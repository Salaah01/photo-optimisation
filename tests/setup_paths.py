import sys
import os

root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

code_dir = os.path.join(root, 'code')

sys.path.append(root)
sys.path.append(code_dir)