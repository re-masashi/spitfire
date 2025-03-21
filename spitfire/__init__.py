'''
Spitfire port forPython3
'''

# Copyright 2007 The Spitfire Authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

__author__ = 'Nafi Amaan Hossain'  # Originally by Mike Solomon
__author_email__ = '<nafines007@gmail.com>'
__version__ = '0.2.6'
__license__ = 'BSD License'

import spitfire
import spitfire.compiler.util
import spitfire.compiler.options
import pathlib


class Environment():
    def __init__(self, dirpath: str, config={}, debug=False):
        if dirpath[-1]!='/':
            dirpath+='/'
        self.home = dirpath
        self.compiled_templates = {}
        if debug:
            self.analyzer_opts = spitfire.compiler.options.o3_options
        else:
            self.analyzer_opts = spitfire.compiler.options.o1_options

    def render(
        self, 
        filename: str, 
        opts, 
        template_name="_", 
        enable_filters=False
    ):
        if type(opts)!=list:
            opts = [opts]

        tmpl = spitfire.compiler.util.load_template_file(self.home+filename,
                template_name,
                analyzer_options=self.analyzer_options,
                compiler_options={"include_path": self.home})

        return tmpl(search_list=opts).main()

    def load_dir(
            self, 
            dirpath: str = None, 
            pattern:str='*.spf',
            includes: str = 'base.spf'
    ):
        if dirpath==None:
            dirpath = self.home
        
        if dirpath[-1]!='/':
            dirpath += '/'

        for x in pathlib.Path(dirpath).glob(includes):
            if not x.is_dir():
                normalised_string = str(x).split('/')[-1]\
                            .split('.')[0]\
                            .replace('-','_')\
                            .replace(' ', '_')\
                            .replace('+','_')\
                            .replace('%', 'percent')\
                            .replace('$','dollar')\
                            .replace('*', 'asterisk')
                self.compiled_templates[normalised_string] = spitfire.compiler.util.load_template_file(
                    str(x), # x has type PosixPath, needs to be normalised.
                    normalised_string,
                    analyzer_options=self.analyzer_opts,
                    compiler_options={"include_path": self.home}
                )

        for x in pathlib.Path(dirpath).glob(pattern):
            if not x.is_dir():
                normalised_string = str(x).split('/')[-1]\
                            .split('.')[0]\
                            .replace('-','_')\
                            .replace(' ', '_')\
                            .replace('+','_')\
                            .replace('%', 'percent')\
                            .replace('$','dollar')\
                            .replace('*', 'asterisk')
                self.compiled_templates[normalised_string] = spitfire.compiler.util.load_template_file(
                    str(x), # x has type PosixPath, needs to be normalised.
                    normalised_string,
                    analyzer_options=self.analyzer_opts,
                    compiler_options={"include_path": self.home}
                )
        

    def render_template(self, template: str, opts):
        if self.debug:
            return self.render(template+'.spf', opts)
        
        if type(opts) != list:
            opts = [opts]
        if self.compiled_templates.get(template) == None:
            raise Exception(f"No such template {template}.spf was compiled.")
        return self.compiled_templates.get(template)(search_list=opts).main()
        
