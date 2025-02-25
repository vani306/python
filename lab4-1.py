s = "Vani Kosambia"
vowels = "aeiouAEIOU"
cnt = {i: s.count(i) for i in vowels if i in s}
print(cnt)
