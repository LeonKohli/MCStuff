import csv
import math

records = []
with open("Coords\Coords.txt", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    name = next(reader)[0]
    next(reader)
    seen = set()
    removed_dupes = 0
    for row in reader:
        if tuple(row) in seen:
            removed_dupes += 1
        else:
            records.append(row)
            seen.add(tuple(row))
    records = [(math.sqrt(int(x)**2 + int(z)**2), int(x), int(z)) for x,z in records ]
    records.sort()
    records = [[x,z] for _,x,z in records ]

with open("Coords\OutputVox.txt", "w") as file:
    file.write("subworlds:NewFarm1\n")
    file.write("oldNorthWorlds:\n")
    file.write("seeds:\n")
    for i, record in enumerate(records):
        file.write(f"name:{i}{name},x:{record[0]},z:{record[1]},y:60,enabled:true,red:0.0025612116,green:0.67284745,blue:0.8256754,suffix:,world:End1,dimensions:the_end#\n")


print("Removed Dupes: ",removed_dupes)
print("Done")
