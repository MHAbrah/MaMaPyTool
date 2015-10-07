import unittest
import pymel.core as pm
import maya.cmds as cmd

class Test_TestMayaConnection(unittest.TestCase):
    def setUp(self):
        pm.commandPort(n=':54321', stp='python')

    def tearDown(self):
        pm.commandPort(n=':54321', cl=True)
    
    def test_A(self):
        from datetime import datetime
        maya_connection = MayaConnection()
        print "Sending code"
        maya_connection.send_code("import sys\nsys.stdout.write('MayaConnection test: ({0})')".format(datetime.now().time()))

if __name__ == '__main__':
    unittest.main()
