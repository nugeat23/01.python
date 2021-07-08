def calcstep(**args):
    
    print(type(args))
    print(args)
    
    begin = args['begin']
    end = args.get('end',1)
    step = args.get('step',1)

    total = 0
    for num in range(begin, end +1, step):
        total += num

    return total

dic = {
    'begin' : 1,
    'end' : 100,
    'step' : 2

}

# dict의 펼침: **사전명
calcstep(**dic)     # calcstep(begin =1, end=100, step=2)
