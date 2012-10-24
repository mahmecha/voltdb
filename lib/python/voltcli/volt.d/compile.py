# This file is part of VoltDB.

# Copyright (C) 2008-2012 VoltDB Inc.
#
# This file contains original code and/or modifications of original code.
# Any modifications made by VoltDB Inc. are licensed under the following
# terms and conditions:
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os

@VOLT.Command(description = 'Run the VoltDB compiler to build the catalog.',
              cli_options = (
                  VOLT.BooleanOption('-C', '--conditional', 'conditional',
                                     'build only when the catalog file is missing'),
                  VOLT.StringOption('-c', '--catalog', 'catalog',
                                    'the application catalog jar file path',
                                    required = True),
                  VOLT.StringOption('-p', '--classpath', 'classpath',
                                    'additional colon-separated Java CLASSPATH directories')))
def compile(runner):
    if not runner.opts.conditional or not os.path.exists(runner.opts.catalog):
        runner.java.execute('org.voltdb.compiler.VoltCompiler',
                            None,
                            runner.project_path,
                            runner.opts.catalog,
                            *runner.args,
                            classpath = runner.opts.classpath)
