def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
                arr[j],arr[j-1] = arr[j-1], arr[j]
                j -= 1
        
def main():
    arr = [13, 46, 24, 52, 20, 9]
    insertion_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()
    