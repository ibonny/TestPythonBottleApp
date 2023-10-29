try:
    wl = open("wholelist.txt", "r")
except:
    print("File not found.")

    exit(1)

try:
    states = open("states.txt", "w")
except e:
    print("Cannot open file for writing: " + e)

try:
    capitals = open("capitals.txt", "w")
except e:
    print("Cannot open file for writing: " + e)

linecount = 0

for line in wl:
    fields = line.split("\t")

    states.write(fields[0].strip() + "\n")
    capitals.write(fields[1].strip() + "\n")

    linecount += 1

wl.close()
states.close()
capitals.close()

print("Read in and wrote out %d lines." % (linecount))
