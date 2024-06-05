import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from foo import foo

def main():
    result = foo(42)
    print(result)

if __name__ == "__main__":
    main()

