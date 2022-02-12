percent = 'процент'
step = 1
while step <= 100:
    if step > 4 and step <20:
        print( step, percent + 'ов')
    elif step % 10 == 1:
        print( step, percent)
    elif step % 10 == 2 or step % 10 == 3 or step % 10 == 4:
        print( step, percent + 'а')
    else:
        print( step, percent + 'ов')
    step +=1