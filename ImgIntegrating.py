# coding= utf-8
import os
from PIL import Image


class ImageHandler:
    def __init__(self):
        self.delta = 100

    def image_resize(self, img, size):
        """resize the img"""
        try:
            if img.mode not in ('L', 'RGB'):
                img = img.convert('RGB')
            img = img.resize(size)
        except Exception:
            pass
        return img

    def image_integrating(self, input_path, output_path, image_dict, \
                          restriction_max_width = None, restriction_max_height = None):

        canvas_width = 0
        canvas_height = 0

        final_width_img1 = 480.0
        final_width_img3 = 260.0
        # final_height_img3 = 60

        # creating a new image
        # new_img = Image.new('RGB', (total_width, max_height), 255)

        # integrating the images
        img_path0 = input_path + 'delivery number'+os.sep + image_dict.get('Ref', '') + os.sep + "0001.jpg"
        try:
            img0 = Image.open(img_path0)
            w0, h0 = img0.size
            canvas_width += w0
        except Exception:
            return image_dict.get('Ref', '')

        img_path1 = input_path + image_dict.get('Joint file', '')
        try:
            img1 = Image.open(img_path1)
            w1, h1 = img1.size
            ratio1 = 600.0/final_width_img1
            img1 = self.image_resize(img1, size=(int(final_width_img1), int(h1/ratio1)))
            w1, h1 = img1.size
        except Exception:
            return image_dict.get('Ref', '')
        canvas_width += w1
        # img_path = input_path + os.sep + self.keyword + "_" + self.image_type_list[2] + ".jpg"
        # img2 = Image.open(img_path)
        # w2, h2 = img2.size
        # # ratio = int(600/480)
        # img2 = self.image_resize(img2, size=(int(final_width_img1), int(h2/ratio1)))
        # canvas_width += final_width_img0

        try:
            img_path3 = input_path + 'receipts' + os.sep + image_dict.get('Ref', '') + os.sep + "0001.jpg"
            img3 = Image.open(img_path3)
            w3, h3 = img3.size
            ratio2 = final_width_img3/w3
            img3 = self.image_resize(img3, size=(int(final_width_img3), int(h3/ratio2)))
            w3, h3 = img3.size
        except Exception:
            return image_dict.get('Ref', '')

        canvas_width += final_width_img3
        canvas_width = int(canvas_width)
        canvas_height = max([h0, h1, h3])

        new_img = Image.new('RGB', (canvas_width + self.delta, canvas_height), (255, 255, 255))
        new_img.paste(img0, (0, 0))
        new_img.paste(img1, (w0, 0))
        new_img.paste(img3, (int(w0+w1), 0))
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
        save_path = '%s%s' % (output_path, image_dict.get('Ref', '') + '.jpg')
        new_img.save(save_path)
        return ''
