from PIL import Image


class Converter:
    def __init__(self, file_name):
        self.fn = file_name
        with Image.open(f"./img/{self.fn}") as im:
            self.px = im.load()
            self.width,self.height = im.size
        self.rgbScale()
        self.rgb2bw()
    def rgbScale(self):
        self.rgb_scale = []
        for i in range(self.width):
            for j in range(self.height):
                self.rgb_scale.append(self.px[i, j])
        print(self.rgb_scale)
    def rgb2bw(self):
        im_bw = Image.new("L",(self.width,self.height))
        for i in range(self.width):
            for j in range(self.height):
                r,g,b = self.rgb_scale[i*self.height+j]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                im_bw.putpixel((i, j), gray)
        im_bw.save(f"./img/{self.fn.split('.')[0]}_bw.png")
        im_bw.show()



Converter(input("Enter file name with extention: "))
