from subprocess import check_output

x = check_output('du -s ./* -b | sort -hr', shell=True).decode('utf8')
# x = check_output('dir', shell=True).decode('cp1250')
l = x.split('\n')
l = [i.split("\t", 1) for i in l]
l = [(int(i[0]), i[1]) for i in l]
m = l[0][0]
l = [((i[0]*40//m)*'*', i[1]) for i in l]
l = '\n'.join(['%40s %s' % i for i in l])
print(l)
