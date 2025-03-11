def sum_avg(n1, n2, n3, n4, n5):
    total= n1+n2+n3+n4+n5
    average= total/5
    return total, average

marks=[86, 89, 90, 92, 94]
total, average= sum_avg(*marks)

print(f"total marks: {total}")
print(f"average marks: {average}")
