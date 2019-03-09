#!/usr/bin/ python
# coding=utf-8
"""
/*******************************************************************************
 * Deep North Confidential
 * Copyright (C) 2018 Deep North Inc. All rights reserved.
 * The source code for this program is not published
 * and protected by copyright controlled
 *******************************************************************************/
"""

from reportlab.pdfgen import canvas
from azure.storage.blob import BlockBlobService
from azure.storage.blob.models import ContentSettings
import os
import time
import logging


class Pdf(object):
    '''
        @function:
            1.pdf base class:
            2.if you want to use this class,and you need to inherit this class 
                example:
                class NewPdf(pdf):
                    def __init__(self,pdf_config_object):
                        pdf_config_object.pdf_time_type = time_type
                        pdf_config_object.pdf_report_type = report_type
                        super(NewPdf,self).__init__(pdf_config_object)
    '''

    def __init__(self, pdf_config_object):

        '''
            @function: init a pdf file object and set the pdf save path and the pdf name
            @args:
                pdf_config_object : it is a config  object 
        '''
        self.pdf_name = None
        self.pdf_page_object = None
        self.pdf_config_object = pdf_config_object
        self.pdf_name = self.pdf_config_object.pdf_name + ".pdf"
        self.pdf_name = self.pdf_name.replace(' ', '_')
        try:
            if not os.path.exists(self.pdf_config_object.pdf_path):
                self.mkdir(self.pdf_config_object.pdf_path)
            self.pdf_page_object = canvas.Canvas(self.pdf_config_object.pdf_path + "/" + self.pdf_name, pagesize=(
            self.pdf_config_object.pdf_width, self.pdf_config_object.pdf_height))
            self.pdf_page_object.setTitle(self.pdf_name)
        except Exception as e:
            raise e
            print e

    def pdf_save(self):

        '''
            @function: it will save the pdf file to  pdf_path
        '''
        try:
            if self.pdf_page_object:
                self.pdf_page_object.save()
                return True
            else:
                return False
        except Exception as e:
            raise e
            return False

    def pdf_add_page(self):

        '''
            @function :it will add a new pdf page on the pdf file . 
        '''
        if self.pdf_page_object:
            self.pdf_page_object.showPage()
            return True
        else:
            return False

    def pdf_clean(self):

        '''
            @function: delete the pdf file . 
        '''
        try:
            os.system("rm -f %s/*" % self.pdf_config_object.pdf_path)
            return True
        except Exception as e:
            print e
            raise e
            return False

    def mkdir(path):
        if not os.path.isdir(path):
            mkdir(os.path.split(path)[0])
        else:
            return
        os.mkdir(path)