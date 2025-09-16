def convert(dollar, rate):
    return [d * rate for d in dollar]

def main():
    n = int(input("How many dollar amounts will you enter? "))
    dollar = [float(input(f"Enter dollar amount #{i+1}: ")) for i in range(n)]
    
    peso = convert(dollar, 57.17)
    yen = convert(dollar, 146.67)

    print(f"{'Dollar($)':<15}{'Phil Peso(P)':<15}{'Jpn Yen (Y)':<15}")
    for d, p, y in zip(dollar, peso, yen):
        print(f"{d:<15.0f}{p:<15.2f}{y:<15.2f}")

main()
