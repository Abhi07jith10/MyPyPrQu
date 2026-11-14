students = [
    ["Abhi", 85, 90, 78],
    ["Arun", 70, 65, 80],
    ["Meera", 92, 88, 95],
    ["Anu", 60, 75, 68]
]

dictionary_students={}
for i in students:
    dictionary_students[i[0]]=i[1:]

highest=0
for j in dictionary_students:
    if sum(dictionary_students[j])>highest:
        highest=sum(dictionary_students[j])
        char=j
print(char,highest)

for k in dictionary_students:
    average=sum(dictionary_students[k])//len(dictionary_students[k])
    print(k,average)


    




    





    
    
    

