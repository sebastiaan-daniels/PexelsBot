"""
A setup file that will create and fill the env file with necessary information
"""
import sys


class main():
    def __init__(self, sys_args):
        args = sys_args
        if args[1] == "-env":
            self.env()

    def env(self):

        token = input("Enter your bot token: ")
        pexels_key = input("Enter your pexels api key: ")

        with open("src/.env", "w") as f:
            f.write(f"TOKEN={token}\nPEXELS_KEY={pexels_key}")


if __name__ == "__main__":
    main(sys.argv)
