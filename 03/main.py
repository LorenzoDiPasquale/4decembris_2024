a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # šis ir mainīgais

num = int(input("Choose a number: ")) # jūs saņemat numuru terminālī

new_list = [] # parsēt tukšu sarakstu

for i in a: # analizē mainīgos lielumus
    if i < num: # salīdziniet, ja mainīgais "num" ir mazāks par "i"
        new_list.append(i) # pievienot mainīgo "new list" uz "i"

print(new_list) # terminālī ierakstiet mainīgo "new_list".