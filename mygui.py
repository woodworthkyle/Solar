#!/usr/bin/python

import sys

# SIP allows us to select the API we wish to use
import sip

# use the more modern PyQt API (not enabled by default in Python 2.x);
# must precede importing any module that provides the API specified
sip.setapi('QDate', 2)
sip.setapi('QDateTime', 2)
sip.setapi('QString', 2)
sip.setapi('QTextStream', 2)
sip.setapi('QTime', 2)
sip.setapi('QUrl', 2)
sip.setapi('QVariant', 2)

#from qt import *
from PyQt4 import *
from form1 import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Form1()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()
