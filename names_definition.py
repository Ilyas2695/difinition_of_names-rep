def structure(file_start):

    d = dict()
    with open(file_start, "r", encoding="UTF-8") as file:
        f = file.read().replace(" — ", " - ")
        li = f.split("\n\n")
        for i in li:
            if "см" in i:
                li2 = i.split(" см. ")
                d.update({li2[0]: li2[-1]})
            else:
                li2 = i.split(" - ")
                d.update({li2[0]: li2[-1]})

    return d


def name_add(file_write):

    answer = input("would you like to add new name? yes/no ")
    if answer == "yes":
        with open(file_write, "a", encoding="UTF-8") as file2:
            new_word = input("write new name with a definition, (name - definition): ")
            f = file2.write("\n\n" + new_word)


def name_search_str(dict_names, name):
    check = False
    for i in dict_names:
        if name in i:
            check = i
            break

    return check


def name_search(dict_names, name):
    name = name_search_str(dict_names, name)
    if name:
        name2 = name_search_str(dict_names, dict_names[name])
        if name2:
            print(dict_names[name2])
        else:
            print(dict_names[name])

    else:
        name_add("Names.txt")


while True:
    name = input("write a name: ")
    dict_names = structure("Names.txt")
    name_search(dict_names, name)