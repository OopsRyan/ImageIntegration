# coding: utf-8
import os
import sys


class FileSearching:
    """A class for searching files."""

    def __init__(self, targeted_file_path):
        self.targeted_file_path = targeted_file_path
        self.file_list = os.listdir(self.targeted_file_path)  ### list_file is a list
        self.transactionNumber = 0

    def getFileNumber(cls):
        return len(cls.file_list)

    def printFileList(cls):
        print cls.file_list

    def calculateTransactionNumber(cls, prefix, suffix):
        for name in cls.file_list:
            if name.startswith(prefix) and name.endswith(suffix):
                cls.transactionNumber += 1
        return cls.transactionNumber
