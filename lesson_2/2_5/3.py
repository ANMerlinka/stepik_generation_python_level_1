#Мандарины
#n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?

s = int(input())
m = int(input())

c = m // s
print(c)

h = m - (c * s) 
print(h)