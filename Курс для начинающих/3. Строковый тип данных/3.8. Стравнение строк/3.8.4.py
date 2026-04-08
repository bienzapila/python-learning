s1, s2, s3 = input(), input(), input()

mx = max(s1, s2, s3)
mn = min(s1, s2, s3)
avg = min(max(s1,s2), max(s1,s3), max(s2,s3))

print(f'{mn} {avg} {mx}')