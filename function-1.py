def count(str):
    str="VanIKOSambia"
    lower=0
    upper=0

    for i in str:
        if(i.islower()):
            lower+=1
        else:
            upper+=1

    return {'lowercase': lower, 'uppercase': upper}
result= count(str)
print(result)
    
