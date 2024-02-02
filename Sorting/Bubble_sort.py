def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j+1] < arr[j]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
        
def main():
    arr = [13, 46, 24, 52, 20, 9]
    bubble_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()
    