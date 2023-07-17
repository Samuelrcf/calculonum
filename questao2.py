import math
for i in range(1,10001):
    s = i/(i**4)
print(s)

for i in range(10001,0,-1):
    s2 = i/(i**4)
print(s2)

erro_absoluto_do_s = s - (math.pi**4/90)
print(erro_absoluto_do_s)

erro_absoluto_do_s2 = s2 - (math.pi**4/90)
print(erro_absoluto_do_s2)

erro_relativo_do_s = (s - (math.pi**4/90)) / (math.pi**4/90)
print(erro_relativo_do_s)

erro_relativo_do_s2 = (s2 - (math.pi**4/90)) / (math.pi**4/90)
print(erro_relativo_do_s2)

erro_percentual_do_s = (s - (math.pi**4/90)) / (math.pi**4/90) * 100
print(erro_percentual_do_s)

erro_percentual_do_s2 = (s2 - (math.pi**4/90)) / (math.pi**4/90) * 100
print(erro_percentual_do_s2)