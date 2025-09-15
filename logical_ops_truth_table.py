value = [True,False]
print("A\tB\tA&B\tA|B\t!A\t!B")
for a in value:
    for b in value:
        print(a,"\t",b,"\t",a and b,"\t",a or b,"\t",not a,"\t",not b)