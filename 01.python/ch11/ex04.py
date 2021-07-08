def flunk(s):
    return s < 60

def myfilter(fn, datas):
    # print(fn)
    # print(fn(10))   # flunk(10)
    result = []
    for d in datas:
        # print(fn(d))
        if fn(d):
            result.append(d)
            
    return result


score = [45,89,72,53,94]

myfilter(flunk, score)      # fn = flunk, datas = score

# for s in myfilter(flunk,score):
# print(s)

