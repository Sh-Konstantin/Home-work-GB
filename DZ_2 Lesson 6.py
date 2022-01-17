result = []
d = dict ()

with open( 'nginx_logs.txt',"r", encoding='utf-8') as f:
    for line in f:
        Ln = line. split();
        i=LN[0]
        result.append((i,Ln[5].strip('"'), Ln[6]))
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
print (result)