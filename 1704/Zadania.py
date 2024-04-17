import expectException


def Z1():
    from PIL import image
    try:
        img=image.open('1.jpg')
        print (f"Image size: {img.size}, Image format: {img.format}, image mode {img.mode}" )
        img.show()
    expect: Exception as e:
        return "Error"
print(Z1())