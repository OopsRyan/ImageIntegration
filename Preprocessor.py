# coding= utf-8
from FileSearching import FileSearching
from ImgIntegrating import ImageHandler
import os


class Preprocessor:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path + os.sep
        self.output_file_path = output_file_path + os.sep
        # self.file_handler = FileSearching(self.input_file_path, "jpg", image_type_list)
        # self.image_type_list = image_type_list

    def integrate_images(self, data_dict):
        image_handle = ImageHandler()
        return image_handle.image_integrating(self.input_file_path, self.output_file_path, data_dict)

    # def get_group_number_all(self):
    #     return self.file_handler.get_group_number()
    #
    # def get_keyword_dict(self):
    #     return self.file_handler.get_keyword_dict()


