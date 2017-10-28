
def insertionSort (a):
    for i in range(1,len(a)):
        key = a[i]
        j = i
        while (j > 0 and key < a[j-1]):
            a[j] = a[j-1]
            j-=1
        a[j] = key
        

def main ():
    a = [6,4,7,1,3]
    print a
    insertionSort(a)
    print a

main()


