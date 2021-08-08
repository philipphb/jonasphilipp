results = []
zahlen = []
target = input("Whats the target number?: ")
target = int((target))
for i in range(1,target+1):
    zahlen.append(i)
print(zahlen)
for zahl1 in zahlen:
    for zahl2 in zahlen:
        for zahl3 in zahlen:
            for zahl4 in zahlen:
                for zahl5 in zahlen:
                    if zahl1 + zahl2 + zahl3 + zahl4 + zahl5 == target:
                        print("Done", zahl1, zahl2, zahl3, zahl4, zahl5)
                        results.append(1)
print(len(results),"gesamt Ergebnisse")
