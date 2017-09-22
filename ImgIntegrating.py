# coding: utf-8
import os
from PIL import Image
from ImageFile import ImageFile


class ImageHandler:
    def __init__(self, image_type_list, keyword):

        self.image_type_list = image_type_list
        self.keyword = keyword
        self.image_type_dict = dict()
        self.delta = 100  # border
    # init the image dictionary which contains four types of photos
    def init_image_type_dict(self):
        self.image_type_dict.setdefault("bgh", ImageFile("bgh", (0, 0), (1080, 1920)))       # express number
        self.image_type_dict.setdefault("sfz_f", ImageFile("sfz_f", (1080, 0), (1706, 960)))     # the front image of ID card
        self.image_type_dict.setdefault("sfz_b", ImageFile("sfz_b", (1080, 960), (1706, 960)))     # the back image of ID card
        self.image_type_dict.setdefault("ddh", ImageFile("sfz_f", (2786, 0), (1080, 1920)))       # transaction number

    def image_resize(self, img, size):
        """resize the img"""
        try:
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            img = img.resize(size)
        except Exception:
            pass
        return img

    def image_integrating(self, input_path, output_path, output_name, \
                          restriction_max_width = None, restriction_max_height = None):

        canvas_width = 0
        canvas_height = 0
        mid_width = 0
        # calculating the max height of the final image
        for image_type in self.image_type_list:
            img_path = input_path + '/' + self.keyword + "_"+image_type+".jpg"
            if os.path.exists(img_path):
                image = Image.open(img_path)
                width, height = image.size
                if image_type == self.image_type_list[0]:
                    canvas_height = height
                    canvas_width += width
                elif image_type == self.image_type_list[1] or image_type == self.image_type_list[2]:
                    if mid_width < width:
                        mid_width = width
                elif image_type == self.image_type_list[3]:
                    canvas_width += width
        canvas_width += mid_width

        # creating a new image
        # new_img = Image.new('RGB', (total_width, max_height), 255)
        new_img = Image.new('RGB', (canvas_width + self.delta, canvas_height), (255,255,255))

        # integrating the images
        img_path = input_path + '/' + self.keyword + "_" + self.image_type_list[0] + ".jpg"
        img = Image.open(img_path)
        w0, h0 = img.size
        new_img.paste(img, (0, 0))

        img_path = input_path + '/' + self.keyword + "_" + self.image_type_list[1] + ".jpg"
        img = Image.open(img_path)
        w1, h1 = img.size
        new_img.paste(img, (w0, 0))

        img_path = input_path + '/' + self.keyword + "_" + self.image_type_list[2] + ".jpg"
        img = Image.open(img_path)
        w2, h2 = img.size
        new_img.paste(img, (w0, h1))

        img_path = input_path + '/' + self.keyword + "_" + self.image_type_list[3] + ".jpg"
        img = Image.open(img_path)
        w3, h3 = img.size
        new_img.paste(img, (w0 + w1, 0))

        # if restriction_max_width and total_width >= restriction_max_width:
        #     ratio = restriction_max_width / float(total_width)
        #     max_height = int(max_height * ratio)
        #     total_width = restriction_max_width
        #     new_img = imageResize(new_img, size=(total_width, max_height))
        #
        # if restriction_max_height and max_height >= restriction_max_height:
        #     ratio = restriction_max_height / float(max_height)
        #     max_height = restriction_max_height
        #     total_width = int(total_width * ratio)
        #     new_img = imageResize(new_img, size=(total_width, max_height))

        if not os.path.exists(output_path):
            os.makedirs(output_path)
        save_path = '%s/%s' % (output_path, output_name)
        return new_img.save(save_path) is None







