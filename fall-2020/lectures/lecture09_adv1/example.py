import argparse

parser = argparse.ArgumentParser()
# позиционный аргумент (обязательный т.к. нет дефолта или обязательность не отменена параметром)
parser.add_argument("square", type=int,
                    help="display a square of a given number")
# именованный и необязательный, т.к. action предполагает, что если аргумент не вызван, то он False
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
# "парсим" аргументы (теперь args это такой типа словарь, к элементам которого можно обращаться через точку)
args = parser.parse_args()

answer = args.square ** 2

if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)