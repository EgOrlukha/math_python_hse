import argparse
parser = argparse.ArgumentParser()

# позиционные и обязательные аргументы
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

# необязательный именованный аргумент, который нужно вызывать как -v -vv -vvvvvv и тогда он равен числу "вызовов"
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()

answer = args.x**args.y
if args.verbosity >= 2:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbosity >= 1:
    print("{}^{} == {}".format(args.x, args.y, answer))
else:
    print(answer)