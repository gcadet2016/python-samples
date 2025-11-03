# This code provides functions to parse command line arguments using argparse.
# argparse is part of Python's standard library
# Documentation: https://docs.python.org/3/library/argparse.html

# Key Features
#   Positional Arguments: Required arguments like name in the example.
#   Optional Arguments: Prefixed with -- or -, like --age.
#   Help Messages: Automatically generated with -h or --help.
#   Type Conversion: Automatically converts input to specified types (e.g., int, float).
#   Default Values: You can set default values for optional arguments.
# Advanced Features
#   Subcommands: Useful for creating complex CLIs with multiple commands.
#   Mutually Exclusive Groups: Ensures only one of several arguments is provided.
#   Custom Actions: Define custom behaviors when an argument is encountered.


import argparse
from html import parser

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process some parameters.")
    # Add arguments
    # Required positional argument
    parser.add_argument("name", type=str, help="Your name")
    # Optional argument with default value
    parser.add_argument("--age", type=int, help="Your age (optional)")
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    parser.add_argument('--num_epochs', type=int, default=10, help='Number of epochs for training')
    # optional argument with short syntax
    parser.add_argument('-lr', '--learning_rate', type=float, default=0.01, help='Learning rate for the model')
 
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Learning Rate: {args.learning_rate}")
    print(f"Batch Size: {args.batch_size}")
    print(f"Number of Epochs: {args.num_epochs}")

# Example usage:
#   python .\cmd_line_args.py -h
#
# Run the script from the command line with arguments, for example:
#   python .\cmd_line_args.py Alice --age 30 --learning_rate 0.001 --batch_size 64 --num_epochs 20
#
#   python .\cmd_line_args.py Alice --age 30