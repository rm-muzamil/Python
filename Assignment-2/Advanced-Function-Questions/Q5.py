# Write a function that takes a list and removes all duplicate elements.
def duplicate_remover(element_list):
    seen = set()
    result = []
    for item in element_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
lst = [1,2,32,21,23,3,34,5,6,6,6,7,7,5,6]
result = duplicate_remover(lst)
print(result)