l = ['ale', 'teste', 'fukano']
t = ('ale', 'teste', 'fukano')
s = {'ale', 'teste', 'fukano'}

print(l[0])
l[0] = 'alejandro'
print(l[0])

l.append('new')
l.remove('ale')

print(l)

s.add('new')
s.remove('ale')

print(s)