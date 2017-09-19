# coding: utf-8
import os
import sys
from FileSearching import FileSearching
from ImgIntegrating import ImageHandler


target_file_path = raw_input("Please enter the target file path:")
file_handle = FileSearching(target_file_path)
print file_handle.getFileNumber()
print file_handle.calculateTransactionNumber("Ruby", ".pdf")

image_file_list = ["bgh", "sfz_f", "sfz_b", "ddh"]
tempImages = ["0011111_bgh.jpg", "0011111_sfz_f.jpg", "0011111_sfz_b.jpg", "0011111_ddh.jpg"]
output_path = "/Users/ryan/Documents/ImgIntegration"
output_name = "0011111_final.jpg"

image_handle = ImageHandler(image_file_list)
image_handle.init_image_type_dict()
print image_handle.image_integrating(target_file_path, tempImages, output_path, output_name, None, None)
