import argparse
# 16.4.1 基本用法--------------------------
# parser = argparse.ArgumentParser()
# parser.add_argument("square",type = int, help="display a square of a given number")
# parser.add_argument("-v","--verbose",help="increase output verbosity",action="count",default=0)
#
# args = parser.parse_args()
#
# answer = args.square**2
#
# if args.verbose >= 2:
#     print("the square of {} is {}".format(args.square,args.square**2))
# elif args.verbose >= 1:
#     print("{}^2={}".format(args.square,answer))
# else:
#     print(args.square**2)

# 16.4.2 多个定位参数-------------------------
# parser = argparse.ArgumentParser()
# parser.add_argument("x",type = int, help="the base")
# parser.add_argument("y",type = int,help="the exponential")
# parser.add_argument("-v","--verbose",help="increase output verbosity",action="count",default=0)
#
# args = parser.parse_args()
#
# answer = args.x**args.y
#
# if args.verbose >= 2:
#     print("running '{}'".format(__file__))
# elif args.verbose >= 1:
#     print("{}^2={}".format(args.x,answer))
# else:
#     print(answer)

# 16.4.3 参数冲突-----------------------------
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
parser.add_argument("x",type = int, help="the base")
parser.add_argument("y",type = int,help="the exponential")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",help="increase output verbosity",action="store_true")
group.add_argument("-q","--quiet",help = "quiet the output", action ="store_true")

args = parser.parse_args()

answer = args.x**args.y

print(type(group))
if args.quiet:
    print(answer)
elif args.verbose:
    print("the {} power of {} is {}".format(args.y, args.x,answer))
else:
    print("{}^{}={}".format(args.x,args.y,answer))

