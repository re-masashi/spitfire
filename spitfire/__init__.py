'''
Spitfire port forPython3
'''

# Copyright 2007 The Spitfire Authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

__author__ = 'Nafi Amaan Hossain'  # Originally by Mike Solomon
__author_email__ = '<nafines007@gmail.com>'
__version__ = '0.2.0'
__license__ = 'BSD License'

import spitfire
import spitfire.compiler.util
import spitfire.compiler.options
import os


class Environment():
    def __init__(self, dirpath: str, config={}):
        self.home = dirpath

    def render(self, filename: str, opts: [{}], template_name="_", enable_filters=False):

        o3_opts = spitfire.compiler.options.o3_options

        tmpl_o3 = spitfire.compiler.util.load_template_file(self.home+filename,
                                                       template_name,
                                                       analyzer_options=o3_opts)
        return tmpl_o3(search_list=opts).main()
