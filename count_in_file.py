with open("count_txt.txt","w") as file:
    file.write("hello world bye world bye ok bye")
n = int(input())
with open("count_txt.txt","r") as file:
    data =file.read()
listE =data.split(" ")
dec ={}
for i in listE:
    dec[i] = listE.count(i)

sorted_dic =dict(sorted(dec.items(),reverse= True, key=lambda item: item[1]))
sorted_list =list(sorted_dic.keys())



for i in range(n):
    print(f"{i+1} - word: {sorted_list[i]} {sorted_dic[sorted_list[i]]} times")