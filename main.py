import numpy as np
from PIL import Image


class Converter:
    def __init__(self, file_name,low_limit,up_limit):
        self.fn = file_name
        self.low_lim = low_limit
        self.up_lim = up_limit
        with Image.open(f"./img/{self.fn}") as self.im:
            self.px = self.im.load()
            self.width,self.height = self.im.size
        self.rgbScale()
        self.rgb_scale = self.double_threshold(self.rgb_scale,self.low_lim, self.up_lim)
        #Single treshold
        #self.rgb_scale = self.single_threshold(self.rgb_scale, self.low_lim)
        self.im_gray = Image.fromarray(self.rgb_scale)
        self.im_gray.show()
        #self.rgb2bw()
    def rgbScale(self):
        self.rgb_scale = np.asarray(self.im)
        '''for i in range(self.width):
            for j in range(self.height):
                self.rgb_scale.append(self.px[i, j])'''
        #print(self.rgb_scale)

    def single_threshold(self,arr,limit):
        arr = np.mean(arr,axis=2)
        arr[arr <= limit] = 0
        arr[arr != 0] = 255
        return arr
    def double_threshold(self,arr,lower_lim,upper_lim):
        arr = np.mean(arr,axis=2)
        arr[lower_lim <= arr] = 0
        arr[arr >= upper_lim] = 0
        arr[arr != 0] = 255
        return arr
    def rgb2bw(self):
        self.im_gray = Image.fromarray(self.rgb_scale)
        #Image.new("L", (self.width, self.height))
        for i in range(self.width):
            for j in range(self.height):
                r,g,b = self.rgb_scale[i*self.height+j]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                self.im_gray.putpixel((i, j), gray)
        self.im_gray.save(f"./img/{self.fn.split('.')[0]}_bw.png")
        self.im_gray.show()




Converter(input("Enter file name with extention: "),int(input("Provide lower limit:")),int(input("Provide upper limit: ")))
