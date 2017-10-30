#iterative version of merge sort (bottom up)
#start with a chunk size of 2 and double the chunk size in every pass

In every pass, partition the list into non-overlapping chunks of size whatever. Split every chunk into 2 and call merge on the 2 parts.
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

def nextLength(start, end):
    while start <= end:
        yield start
        start = start*2

#the last marge can be saved as follows:
#i specify the size of the chunks to be merged (and not the size of the merged chunk)
#j increases by the size of the merged chunk
def mergeSort (a):
    for i in nextLength(2,len(a)):
        print "i ",i
        for j in range(0, len(a), i):
            r = min(j+i-1,len(a)-1)
            print j,r
            m = j + (r-j)/2
            merge(a,j,m,r)
    merge(a,0,i-1,len(a)-1)
            
def main():
    a = [13,2,23,14,5,63,74,38,19]
    mergeSort(a)
    print a

main()
