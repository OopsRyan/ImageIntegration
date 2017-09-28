# coding= utf-8
from FileSearching import FileSearching
from ImgIntegrating import ImageHandler


class Preprocessor:
    def __init__(self, input_file_path, output_file_path, image_type_list):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.file_handler = FileSearching(self.input_file_path, "jpg", image_type_list)
        self.image_type_list = image_type_list

    def integrate_images(self, keyword):
        image_handle = ImageHandler(self.image_type_list, keyword)
        return image_handle.image_integrating(self.input_file_path, self.output_file_path, str(keyword)+"_final.jpg")

    def get_group_number_all(self):
        return self.file_handler.get_group_number()

    def get_keyword_dict(self):
        return self.file_handler.get_keyword_dict()


