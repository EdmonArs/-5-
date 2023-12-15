s = input("Введите текст: ")
t = len(s)
l_count = sum(1 for i in s if i.islower())
u_count = sum(1 for i in s if i.isupper())
l_proc = (l_count / t)*100
u_proc = (u_count / t)*100
print("Процент строчных букв: ", round(l_proc, 2), "%")
print("Процент прописных букв: ", round(u_proc, 2), "%")