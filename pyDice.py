from PIL import Image

numDice = 100

image = Image.open("example.png")
new_image = image.resize((10, 10))
new_image = new_image.convert('L')
pix = new_image.load()
new_image.save('output.png')

pix_val=list(new_image.getdata())
print(pix_val)
#print(min(pix_val))
#print(len(pix_val))
for i in range(len(pix_val)):
    #print("Spot: "+str(i)+ " Value: "+str(pix_val[i])+" New Value: ")
    if (pix_val[i] < 42):
        pix_val[i] = 1
    if (pix_val[i] >= 42 and pix_val[i] < 84):
        pix_val[i] = 2
    if (pix_val[i] >= 84 and pix_val[i] < 126):
        pix_val[i] = 3
    if (pix_val[i] >= 126 and pix_val[i] < 168):
        pix_val[i] = 4
    if (pix_val[i] >= 168 and pix_val[i] < 210):
        pix_val[i] = 5
    if (pix_val[i] >= 210):
        pix_val[i] = 6
    #print(pix_val[i])
    pass

print(pix_val)

#new_image.show()
