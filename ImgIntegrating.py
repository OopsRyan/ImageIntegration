# coding: utf-8
import os
from PIL import Image
from ImageFile import ImageFile


class ImageHandler:
    def __init__(self, image_file_list):
        self.image_file_list = image_file_list
        self.image_type_dict = dict()

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

    def image_integrating(self, targeted_file_path, images, output_path, output_name, \
                          restriction_max_width = None, restriction_max_height = None):

        # calculating the max height of the final image
        # for imgName in images:
        #     img_path = targeted_file_path + '/' + imgName
        #     if os.path.exists(img_path):
        #         image = Image.open(img_path)
        #         width, height = image.size
        #         if height > max_height:
        #             max_height = height
        #         total_width += width

        # creating a new image
        # new_img = Image.new('RGB', (total_width, max_height), 255)
        new_img = Image.new('RGB', (3866, 1920), 255)

        # integrating the images
        for imgName in images:
            img_path = targeted_file_path + '/' + imgName
            if os.path.exists(img_path):
                img = Image.open(img_path)
                for index in self.image_type_dict:
                    if imgName.find(index) != -1:
                        image_file = self.image_type_dict.get(index, None)
                        new_img.paste(img.resize(image_file.get_size()), image_file.get_ordination())

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
        new_img.save(save_path)
        return save_path






