l=[]
with open("running-config.cfg","rt") as in_file:
  a=in_file.read()
  b=a.split("!")
  print(b)
