easy = True
duplicates = 0

while easy:
    input_word = list(input("enter a word: "))
    unique = len(input_word)
    duplicate_list = []

    for i in range(len(input_word)):
        isDuplicate = False
        for k in range(len(duplicate_list)):
            if input_word[i] == duplicate_list[k]:
                print(f"{input_word[i]} is already a duplicate")
                isDuplicate = True
        for j in range(i + 1, len(input_word)):
            if input_word[i] == input_word[j] and isDuplicate==False:
                duplicates += 1
                duplicate_list.append(input_word[i])
                print(f"{input_word[i]} has been declared a duplicate")
                isDuplicate = True
            else:
                print(f"{input_word[i]} is unique")

    unique = unique - duplicates

    print("".join(input_word), "has", unique, "unique characters. The duplicates are: ", duplicate_list)

    input_word = input("do you want to enter another word: ")

    if input_word == "N":
        easy = False
    else:
        easy = True
        duplicates = 0