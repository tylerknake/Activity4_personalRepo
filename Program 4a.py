# Tyler Knake
# ISQA 3900 - 9/26/2021
# Program 4a - Takes a list of names as an argument, sorts the list, and then creates a new list with
# any duplicates from the first list removed. Prints both lists.

names = ['maria','maria','will','sam','maria','kahn','sam','barry','george','hank','belinda','maria','karthik']
names.sort()
print("Initial List of Names:")
print(names)

def removeDuplicates(list):
    uniques = []
    for x in list:
        if x not in uniques:
            uniques.append(x)
    print(uniques)

print()
print("List of Unique Names:")
removeDuplicates(names)