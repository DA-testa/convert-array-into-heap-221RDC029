# python3
def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    number = len(data)
    for i in range (number // 2, -1, -1):
        atrast_mazako(data, number, i, swaps)

    return swaps

def atrast_mazako(data, number, i, swaps):
    mazākais_node = i
    kreisā_puse = 2 * i + 1
    labā_puse = 2 * i + 2

    # kods iet cauri labajam un kreisajam child, lai atrastu mazāko vērtību un pēc tam
    # to apmaina ar pašreizēju node vērtību, ja mazākā vērtība nav pašreizējā node vērtība

    # Pārbauda vai kreisās puses child ir mazākais parent
    if kreisā_puse < number and data[kreisā_puse] < data[mazākais_node]:
        mazākais_node = kreisā_puse
    # Pārbauda vai labās puses child ir mazākais parent
    if labā_puse < number and data[labā_puse] < data[mazākais_node]:
        mazākais_node = labā_puse
    # Ja mazākais node nav parent, tad apmaina ar vietām un vēlreiz iet cauri kokam
    if mazākais_node != i:
        swaps.append((i, mazākais_node))
        data[i], data[mazākais_node] = data[mazākais_node], data[i]
        atrast_mazako(data, number, mazākais_node, swaps)

    return swaps

def main():
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
    # and give back all swaps
    # output all swaps
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # this number should be less than 4n (less than 4 * len(data))
    if len(swaps) >= 4 * len(data):
        print("Pārāk liels cipars!")

if __name__ == "__main__":
    main()

