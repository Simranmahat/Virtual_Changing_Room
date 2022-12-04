from PIL import Image
import sys
 
def convertImage():
    objectid=sys.argv[1]
    
    
    img = Image.open("media/product_image/glass{}.png".format(objectid))
    img = img.convert("RGBA")
 
    datas = img.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save("FilterApply/Glasses/glass{}.png".format(objectid))
    print("Successful")
 
convertImage()