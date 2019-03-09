#!/usr/bin/ python
# coding=utf-8
"""
/*******************************************************************************
@auther:Frederick HOu
@email:frederick_hou@163.com
@date:2019/03/09
 *******************************************************************************/
"""
import random
import time
import logging
import sys
sys.path.append('../')
from pdf_lib.pdf_ui import *


logger = logging.getLogger(__name__)


class PdfPage(PdfUI):

    def __init__(self, pdf_config_object):
        self.pdf_config_object = pdf_config_object
        PdfUI.__init__(self, pdf_config_object)


    def add_first_page(self):
        '''
        add your page
        '''

        self.pdf_add_page()

