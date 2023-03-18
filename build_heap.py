# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    number = len(data)
    for i in range (number // 2, -1, -1):
        mazākais_node = i
        kreisā_puse = 2 * i + 1
        labā_puse = 2 * i + 2

        if kreisā_puse < number and data[kreisā_puse] < data[mazākais_node]:
            mazākais_node = kreisā_puse
        if labā_puse < number and data[labā_puse] < data[mazākais_node]:
            mazākais_node = labā_puse
        if mazākais_node != i:
            swaps.append((i, mazākais_node))
            data[i], data[mazākais_node] = data[mazākais_node], data[i]
            mazākais_node = i

    return swaps

def main():
# TODO : add input and corresponding checks
# add another input for I or F
# first two tests are from keyboard, third test is from a file
# input from keyboard
    ievade = input()
    if "I" in ievade:
        try:
            n = int(input())
            data = list(map(int, input().split()))
            swaps = build_heap(data)
            print(len(swaps))
            for swap in swaps:
                print(swap[0], swap[1])
        except Exception as exception:
                print("Kļūda", str(exception))
                return
    if "F" in ievade:
        faila_nosaukums = input()
        mape = 'tests/'
        try:
            with open(mape + faila_nosaukums, 'r') as fails:
                n = int(fails.readline())
                data = list(map(int, fails.readline().split()))
            swaps = build_heap(data)
            print(len(swaps))
            for swap in swaps:
                print(swap[0], swap[1])
        except Exception as exception:
                print("Fails neeksistē", str(exception))
                return
    else:
        return
    # checks if lenght of data is the same as the said lenght
    if len(data) != n:
        return
    
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # calls function to assess the data 
    # and give back all swaps

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    if len(swaps) >= 4 * len(data):
        print("Pārāk liels cipars!")

    # output all swaps
if __name__ == "__main__":
    main()
