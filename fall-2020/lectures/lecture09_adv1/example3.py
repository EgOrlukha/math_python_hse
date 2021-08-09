import argparse
import solve

parser = argparse.ArgumentParser()

# позиционный, необязательный
parser.add_argument('char', type=str, default='x', help='the character of equation')
# именованные, необязательные
parser.add_argument('-a', type=float, default=0, help='the highest coefficient x^2')
parser.add_argument('-b', type=float, default=0, help='the linear coefficient x')
parser.add_argument('-c', type=float, default=0, help='the constant coefficient')
parser.add_argument('-d', type=float, default=0, help="the right hans side constant coefficient")
parser.add_argument('-v', '--verbosity', action='count', default=0)
args = parser.parse_args()
        
answer = solve.solve(args.a, args.b, args.c, args.d)

if args.verbosity >= 2:
    print('The equation: ({args.a}){args.char}^2 + ({args.b}){args.char} + ({args.c}) = {args.d}'.format(args=args))
elif args.verbosity >= 1:
    print('{} = {}'.format(args.char, answer))
else:
    print(answer)