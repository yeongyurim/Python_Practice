ilist = [i for i in range(1,11)]
ilist = [i*i if i % 2 == 0 else i*i*i for i in ilist]
print(ilist)