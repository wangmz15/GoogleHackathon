from Splendor import Splendor
import sys

def main(status):
    # my code here
    splendor = Splendor(status)

if __name__ == "__main__":
    status = ''.join(sys.stdin.readlines())
    main(status)