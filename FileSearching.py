# coding= utf-8
import os


class FileSearching:
    """A class for searching files.
    However, you cannot understander this file! I am sure.
    You would be confusing, if you keep going on."""

    def __init__(self, targeted_file_path, suffix, image_type_list):
        ''' suffix - .jpg
            count_keyword - bgh
        '''
        self.targeted_file_path = targeted_file_path
        self.file_list = os.listdir(self.targeted_file_path)  ### list_file is a list
        self.suffix = suffix
        self.count_keyword = image_type_list[0]
        self.image_type_list = image_type_list
        self.transactionNumber = 0

        # filtering
        self.get_image_list()
        # getting keywords
        self.keyword_list = list()
        self.keyword_dict = dict()
        self.get_keyword_list()
        # counting
        self.count_group_number()

    def get_image_list(self):
        for name in self.file_list:
            if not name.endswith(self.suffix):
                self.file_list.remove(name)
        # self.file_list = [self.file_list.remove(name) for name in self.file_list if name.endswith(self.suffix)][:]

    def get_keyword_list(self):
        # According to count_keyword, get all keywords and create a keyword list. ie. keyword = bgh
        for name in self.file_list:
            if name.find(self.count_keyword) != -1:
                keyword = name.split('_')[0]
                if keyword not in self.keyword_dict:
                    self.keyword_dict[keyword] = 1
                    self.keyword_list.append(keyword)

    def count_group_number(self):
        # counting group number by traversing the keyword list
        # and finding out whether other 3 types exit or not?--------------------------
        # ie. find the image with bgh number and not count_keyword 'bgh'
        # and then judge whether this image contains other types 'sfz_f', 'sfz_b', and 'ddh'
        # if so, it counts
        for keyword in self.keyword_list:
            for name in self.file_list:
                if name.split('_')[0] == keyword and name.find(self.count_keyword) == -1:
                    for kind in self.image_type_list[1:]:
                        if name.find(kind) != -1:
                            self.keyword_dict[keyword] = self.keyword_dict.get(keyword, 0) + 1
                            break
        print self.keyword_dict
        print self.keyword_list
        # find the key with value 4 in the keyword dictionary
        self.keyword_dict = {k: v for k, v in self.keyword_dict.iteritems() if v == 4}
        print self.keyword_dict

    def get_group_number(self):
        return len(self.keyword_dict)

    def get_keyword_dict(self):
        return self.keyword_dict

    def getFileNumber(cls):
        return len(cls.file_list)

    def printFileList(cls):
        print cls.file_list

