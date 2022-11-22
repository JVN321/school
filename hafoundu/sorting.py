def sorting(filename):
  name = filename.split("/")[1]
  infile = open(filename)
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()
  words.sort()
  outfile = open("admissionsorted/" + name, "w+")
  for i in words:
    outfile.writelines(i)
    outfile.writelines("\n")
  outfile.close()


sorting("admissionnumbers/bnvv.amserp.in.txt")
'''
sorting("admissionnumbers/bav.amserp.in.txt")
sorting("admissionnumbers/bmv.amserp.in.txt")
sorting("admissionnumbers/bmv.amserp.in.txt")
sorting("admissionnumbers/bvme.amserp.in.txt")
sorting("admissionnumbers/bvmer.amserp.in.txt")
sorting("admissionnumbers/bvmg.amserp.in.txt")
sorting("admissionnumbers/bvvt.amserp.in.txt")
sorting("admissionnumbers/bnvv.amserp.in.txt")
'''