#!/usr/bin/python
# -*- coding : utf-8 -*-

# OCR
class OCR(object):

    def __init__(self):
        self.processor = None

    def run(self):
        self.processor.crop()
        self.processor.touch()


class Process(object):
    def crop(self):
        raise NotImplementedError

    def touch(self):
        raise NotImplementedError


class Processor1(Process):
    def crop(self):
        print ('processor 1 cropping')

    def touch(self):
        print ('processor 1 touching')


class Processor2(Process):
    def crop(self):
        print ('processor 2 cropping')

    def touch(self):    
        print ('processor 2 touching')

# Clients
if __name__ == "__main__":
    ocr = OCR()

    ocr.processor = Processor1()
    ocr.run()

    ocr.processor = Processor2()
    ocr.run()
