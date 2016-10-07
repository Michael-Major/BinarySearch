#Michael Major HW Assignment 6: Binary Search

def bsearch(lst,key,start,length):
    if (length-1) < start:
        return -1
    elif lst[start+((length-1)-start)//2] == key:
        return start+((length-1)-start)//2
    elif lst[start+((length-1)-start)//2] >= key:
        return bsearch(lst,key,start,(start+((length-1)-start)//2))
    else:
        return bsearch(lst,key,(start+((length-1)-start)//2)+1,length)

lst = ['boa','cat','dog','eel','fish','gerbil','hamster','pig','tarantula']
key = str(input("Enter a pet: "))
while key != '':
    if bsearch(lst,key,0,len(lst)) == -1:
        print(key,"is not in the list!")
        key = str(input("Enter a pet: "))
    else:
        print(key,"is at index",bsearch(lst,key,0,len(lst)))
        key = str(input("Enter a pet: "))
