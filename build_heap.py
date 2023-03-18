# python3

def heapify(data, i, swaps):
    number = len(data)
    mazākais_node = i
    kreisā_puse = 2 * i + 1
    labā_puse = 2 * i + 2

    if kreisā_puse < number and data[kreisā_puse] < data[mazākais_node]:
        kreisā_puse = mazākais_node
    if labā_puse < number and data[labā_puse] < data[mazākais_node]:
        labā_puse = mazākais_node
    if mazākais_node != i:
        swaps.append((i, mazākais_node))
        data[i], data[mazākais_node] = data[mazākais_node], data[i]
        heapify(data, mazākais_node, swaps)

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    number = len(data)
    for i in range (number // 2, -1, -1):
        heapify(data, i, swaps)
    return swaps

def main():
    try:
    # TODO : add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
        ievade = input()
        if "I" in ievade:
            n = int(input())
            data = list(map(int, input().split()))
        if "F" in ievade:
            faila_nosaukums = input()
            mape = 'tests/'
            try:
                with open(mape + faila_nosaukums, 'r') as fails:
                    n = int(fails.readline())
                    data = list(map(int, fails.readline().split()))
            except Exception as exception:
                    print("Fails neeksistē", str(exception))
                    return
        # checks if lenght of data is the same as the said lenght
        assert len(data) == n

        # calls function to assess the data 
        # and give back all swaps
        swaps = build_heap(data)

        # TODO: output how many swaps were made, 
        # this number should be less than 4n (less than 4*len(data))
        if len(swaps) >= 4 * len(data):
            print("Pārāk liels cipars!")

        # output all swaps
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

    except Exception as exception:
        print("Kļūda!", exception)

if __name__ == "__main__":
    main()
