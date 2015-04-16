# ====================================================================
# Copyright (c) 2007 Open Source Applications Foundation.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions: 
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software. 
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
# ====================================================================
#

import sys, os

from unittest import TestCase, main
from PyICU import *


class TestCharset(TestCase):

    def testDetect(self):

        detector = CharsetDetector()
        detector.setText('foo')

        match = detector.detect()
        self.assert_(match.getName() == 'UTF-8')

    def testDetectAll(self):

        detector = CharsetDetector('foo')

        matches = detector.detectAll()
        self.assert_(matches[0].getName() == 'UTF-8')

    def testDeclared(self):

        detector = CharsetDetector('beaut\xe9 probable', 'iso-8859-1')

        self.assert_("ISO-8859-1" in (m.getName()
                                      for m in detector.detectAll()))

    def testUnicode(self):

        string = 'beaut\xe9 probable'
        ustring = unicode(CharsetDetector(string).detect())

        self.assert_(ustring.encode('iso-8859-1') == string)
        
        

if __name__ == "__main__":
    main()