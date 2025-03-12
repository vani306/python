def count_boys_girls():
  x=[('kabir', 'saumya', 'neal', 'vihang'), 'vani', 'avani', ('vedant',), 'prachi']
  boys= 0
  girls= 0
  for i in x:
     if isinstance(i, tuple):
        boys += 1
     else:
        girls +=1

  return boys, girls
boys, girls= count_boys_girls()

print(f"no. of boys: {boys}")
print(f"no. of girls: {girls}")
   
