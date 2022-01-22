pictureMap = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
picture = ""

for i in pictureMap:
    for j in i:
        if not j:
            picture += " "
        elif j:
           picture += "$"
    picture += "\n"
print(picture)