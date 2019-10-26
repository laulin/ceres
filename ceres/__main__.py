import sys

from .builder import Builder

pwd = sys.argv[1]

if __name__ == "__main__":
    builder = Builder(pwd)
    builder.run()