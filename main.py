import numpy as np
from PIL import Image, ImageOps


class Converter:
    def __init__(self, usage, file_name, low_limit=None, up_limit=None):
        # Reading user params
        self.fn = file_name
        self.low_lim = low_limit
        self.up_lim = up_limit
        # Opening file and converting to np array
        with Image.open(f"./img/{self.fn}") as self.im:
            self.px = self.im.load()
            self.width, self.height = self.im.size
        self.rgb_arr = np.asarray(self.im)
        print(self.rgb_arr)

        match usage:
            case 11:
                self.single_threshold(self.low_lim)
            case 12:
                self.double_threshold(self.low_lim, self.up_lim)
            case 21:
                self.rgb2gray()
            case 22:
                self.mask71()
        self.im_out = Image.fromarray(self.rgb_arr)
        # self.im_gray.save(f"./img/{self.fn.split('.')[0]}_bw.jpeg")
        self.im_out.show()

    def single_threshold(self, limit):
        self.rgb_arr = np.mean(self.rgb_arr, axis=2)
        self.rgb_arr[self.rgb_arr <= limit] = 0
        self.rgb_arr[self.rgb_arr != 0] = 255

    def double_threshold(self, lower_lim, upper_lim):
        self.rgb_arr = np.mean(self.rgb_arr, axis=2)
        self.rgb_arr[lower_lim <= self.rgb_arr] = 0
        self.rgb_arr[self.rgb_arr >= upper_lim] = 0
        self.rgb_arr[self.rgb_arr != 0] = 255

    def rgb2gray(self):
        im_temp = Image.fromarray(self.rgb_arr)
        # Image.new("L", (self.width, self.height))
        for i in range(self.width):
            for j in range(self.height):
                r, g, b = self.rgb_arr[j][i]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                im_temp.putpixel((i, j), (gray, gray, gray))
        im_temp_norm = ImageOps.equalize(im_temp)
        self.rgb_arr = np.asarray(im_temp_norm)

    def mask71(self):
        self.rgb_arr = np.mean(self.rgb_arr, axis=2)
        sum_area = np.cumsum(np.cumsum(self.rgb_arr, axis=0), axis=1)
        #TODO Finish mask

while True:
    print("Simple image processing program \n 1 | Convert colors to black and white "
          "\n 2 | Convert colors to gray scale\n 3 | Exit \n")
    choice = int(input())
    if choice == 1:
        choice = -1
        print("Would you like to use single or double threshold? \n 1 | Single \n 2 | Double \n 3 | Go back \n")
        while choice == -1:
            choice = int(input())
            if choice == 1:
                Converter(11, input("Enter file name with extension: "), int(input("Provide limit:")))
            elif choice == 2:
                Converter(12, input("Enter file name with extension: "), int(input("Provide lower limit:")),
                          int(input("Provide upper limit: ")))
            elif choice == 3:
                choice = -1
                break
            else:
                print("Wrong input try again \n")
    elif choice == 2:
        choice = -1
        print("Would you like to use histogram equation or mean filter? "
              "\n 1 | Histogram eq \n 2 | Mean filter \n 3 | Go back \n")
        while choice == -1:
            choice = int(input())
            if choice == 1:
                Converter(21, input("Enter file name with extension: "))
            elif choice == 2:
                Converter(22, input("Enter file name with extension: "))
            elif choice == 3:
                choice = -1
                break
            else:
                print("Wrong input try again \n")
    elif choice == 3:
        exit(1)
