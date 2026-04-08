a = input()
one = a.find('h')
two = a.rfind('h')
a = a[:one]+a[two+1:]
print(a)