from subprocess import check_output

x = check_output('du -s ./* -b | sort -hr', shell=True).decode('utf8').split("\n")
# x = check_output('dir', shell=True).decode('cp1250')
l = [i.split("\t") for i in x]
print(l)
l = [(int(i[0]), i[1]) for i in l[:-1]]
m = l[0][0]

l = [((i[0]*40//m)*'*', i[1]) for i in l]
l = '\n'.join(['%40s %s' % i for i in l])
print(l)
