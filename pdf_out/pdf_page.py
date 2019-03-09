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
        chart_data = [25,65,330]
        chart_lable=['index','a']
        data = []
        data.append(chart_data)
        self.pdf_drawBar(data)
        self.pdf_add_page()

