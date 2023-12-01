#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1  # Exclude the script name

    if num_args == 0:
        print("0 argument.")
        print(".")
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        [print(f"{idx}: {arg}") for idx, arg in enumerate(argv[1:], start=1)]

