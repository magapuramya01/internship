class PDFFile:
    def open(self):
        print("PDF file opened")


class WordFile:
    def open(self):
        print("Word file opened")


def open_file(obj):
    obj.open()


open_file(PDFFile())
open_file(WordFile())