s1, s2, s3, s4 = input(), input(), input(), input()

a = min(s1, s2, s3, s4)
b = max(s1, s2, s3, s4)
print((ord(a[-1])*ord(b[-1]))**2)