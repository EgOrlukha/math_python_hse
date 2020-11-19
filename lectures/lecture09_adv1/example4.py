import argparse
import solve

parser = argparse.ArgumentParser()
parser.add_argument('char', type=str, default='x', 
                    help='the character of equation')
# именованный обязательный аргумент
# список из ровно 4х элементов (nargs еще может быть равен '+', тогда это любое число аргументов, но как минимум один)
# вводится как -c 1 2 3 4 или --coef 1 2 3 4
parser.add_argument('-c','--coef', nargs=4, type=int, required=True, 
                    help='REQUIRED the coefficients a b c d of the equation ax^2 + bx + c = d')
parser.add_argument('-v', '--verbosity', action='count', default=0)
args = parser.parse_args()

answer = solve.solve(*args.coef)

if args.verbosity >= 2:
    print('The equation: ({args.coef[0]}){args.char}^2 + ({args.coef[1]}){args.char} + ({args.coef[2]}) = {args.coef[3]}'.format(args=args))
elif args.verbosity >= 1:
    print('{} = {}'.format(args.char, answer))
else:
    print(answer)