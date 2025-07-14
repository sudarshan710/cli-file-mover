####  How to use argParser?

import argparse

# parser initialization
parser = argparse.ArgumentParser(description='sample parser')

# adding arguments to parser
parser.add_argument("name", help="Your Name")
parser.add_argument("lastname", help="Your Last Name")
parser.add_argument("--age", type=int, help="Your Age", default=18)

# setting parser
args = parser.parse_args()

# output format and order for arguments
print(f"\n Helloy, my name is {args.name} {args.lastname}. I'm {args.age} years old!\n")

# USE ->    python arg_parser_tutorial.py Alice Snow --age 45

#  use 'python arg_parser.py --help' for helper.
#  'name' and 'lastname' are positional arguments while '--age' / '--a' is optional argument with '18' as default value.
#  use of '--' indicates optional arguments since a default value is provided for it.