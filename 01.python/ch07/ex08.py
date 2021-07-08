def calcstep(**args):
    
    print(type(args))
    print(args)
    
    begin = args['begin']
    end = args['end']
    step = args['step']

    # begin = args['begin']
    # end = args.get('end',1)
    # step = args.get('step',1)

    total = 0
    for num in range(begin, end +1, step):
        total += num

    return total


print(f'3 ~ 5 = {calcstep(begin=3,end=5,step=1)}')
print(f'3 ~ 5 = {calcstep(begin=1,end=2,step=3)}')

