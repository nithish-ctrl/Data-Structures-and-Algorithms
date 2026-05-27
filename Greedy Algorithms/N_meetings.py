
def n_meetings(start,end):
    meets = [(end[i], start[i], i+1) for i in range(len(start))]
    meets.sort()
    result = []
    last_index = -1
    for e, s, idx in meets:
        if s > last_index :
            result.append(idx)
            last_index = e
    return result


start = [1,3,0,5,8,5]
end = [2,4,5,7,9,9]
result= n_meetings(start,end)
print(result)


