#xndir_2 (Write a function that removes an element at a specified index from a list. Handle the IndexError by raising a custom exception if the index is out of range.)
def remove(m:list,n:int):
    if m[n] not in m:
        raise IndexError("there is not that index")
    m.pop(n)
    return m
print(remove([1,2,3,4],2))
