def Test():
    f = open('input.txt', 'r')
    line = f.readlines()
    line = [i.strip('\n') for i in line]
    num = int(line[-1])
    ind = line[:-1]

    d={}
    for i in ind:
        i = i.split(':')
        d[i[1]] = int(i[0])
    d = sorted(d.items(), key = lambda x : x[1])

    st = ''
    for i in d:
        if num % i[1] == 0:
            st += i[0]

    if st == '':
        answer = num
    else:
        answer = num

    return answer

print(Test())