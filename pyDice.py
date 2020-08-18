from PIL import Image

#numDice = 100
numDiceWide = 50
numDiceTall = 50

image = Image.open("example.png")
dieOne = Image.open("one.png")
dieTwo = Image.open("two.png")
dieThree = Image.open("three.png")
dieFour = Image.open("four.png")
dieFive = Image.open("five.png")
dieSix = Image.open("six.png")
diceImageWidth, diceImageHeight = dieOne.size
new_image = image.resize((numDiceWide, numDiceTall))
new_image = new_image.convert('L')
pix = new_image.load()

pix_val=list(new_image.getdata())
print(pix_val)
#print(min(pix_val))
#print(len(pix_val))
for i in range(len(pix_val)):
    #print("Spot: "+str(i)+ " Value: "+str(pix_val[i])+" New Value: ")
    if (pix_val[i] < 42):
        pix_val[i] = 6
    if (pix_val[i] >= 42 and pix_val[i] < 84):
        pix_val[i] = 5
    if (pix_val[i] >= 84 and pix_val[i] < 126):
        pix_val[i] = 4
    if (pix_val[i] >= 126 and pix_val[i] < 168):
        pix_val[i] = 3
    if (pix_val[i] >= 168 and pix_val[i] < 210):
        pix_val[i] = 2
    if (pix_val[i] >= 210):
        pix_val[i] = 1
    #print(pix_val[i])
    pass
outSize = (diceImageWidth*numDiceWide,diceImageHeight*numDiceTall)
#Creates a black image
output_image = Image.new('L', outSize, color=0)
for i in range(len(pix_val)):
    xLocation = int((int(diceImageWidth)*i))%(diceImageWidth*numDiceWide)
    yLocation = int(i/numDiceWide)*diceImageHeight
    #print ("x" + str(xLocation))
    #print ("y" + str(yLocation))
    #print (i)
    if (pix_val[i] == 1):
        output_image.paste(dieOne, (xLocation,yLocation))
    if (pix_val[i] == 2):
        output_image.paste(dieTwo, (xLocation,yLocation))
    if (pix_val[i] == 3):
        output_image.paste(dieThree, (xLocation,yLocation))
    if (pix_val[i] == 4):
        output_image.paste(dieFour, (xLocation,yLocation))
    if (pix_val[i] == 5):
        output_image.paste(dieFive, (xLocation,yLocation))
    if (pix_val[i] == 6):
        output_image.paste(dieSix, (xLocation,yLocation))
    pass
output_image.save('output.png')
#print(pix_val)

#new_image.show()
