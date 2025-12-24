# with open("image1.png", "rb") as src:
#     with open("image2.png", "wb") as dst:
#         dst.write(src.read())

src = open("image1.png", "rb")
dst = open("image2.png", "wb")
dst.write(src.read())
