#merge sort implementation
#O(nlogn) time, O(n) space

def merge (a, l, m, r):
    left = a[l:m+1]
    right = a[m+1:r+1]
    left.append(max(a[m],a[r])+1)
    right.append(max(a[m],a[r])+1)

    j = 0
    k = 0
    for i in xrange (l,r+1):
        if (left[j] <= right[k]):
            a[i] = left[j]
            j += 1
        else:
            a[i] = right[k]
            k += 1

def mergeSortAux (a, l, r):
    if (l >= r):
        return
    m = l + (r-l)/2
    mergeSortAux(a,l,m)
    mergeSortAux(a,m+1,r)
    merge(a,l,m,r)

def mergeSort (a):
    mergeSortAux(a, 0, len(a)-1)

def main ():
    a = [5, 2, 13, 20, 43, 6]
    print a
    mergeSort(a)
    print a

main()
