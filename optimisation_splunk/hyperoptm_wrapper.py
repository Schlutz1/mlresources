import os 
import subprocess
import sys

import logging
wrapped_script="hyperoptm.py"


_SPLUNK_HOME=os.environ['SPLUNK_HOME']
_SPLUNK_PYTHON_PATH = os.environ['PYTHONPATH']
os.environ['LD_LIBRARY_PATH']='' #hack to stop splunk libries loading instead of system

if sys.platform == "win32":
    logfilename = 'searchcommand2_app.log'
    _APP_BIN_HOME=_SPLUNK_HOME + "\\etc\\apps\\aiam-ml-core\\bin"
    _NEW_PYTHON_PATH = "C:\\opt\\Anaconda2\\python"
    os.environ['PYTHONPATH'] = _NEW_PYTHON_PATH
    my_process = _APP_BIN_HOME + "\\" + wrapped_script
elif sys.platform == "darwin" or sys.platform == "linux" or sys.platform == "linux2":
    logfilename = 'searchcommand2_app.log'
    _APP_BIN_HOME = _SPLUNK_HOME + "/etc/apps/aiam-ml-core/bin"
    _NEW_PYTHON_PATH = _SPLUNK_HOME + "/etc/apps/aiam-ml-core/python/bin/python"
#    _NEW_PYTHON_PATH =  "/usr/bin/python"
    os.environ['PYTHONPATH'] = _NEW_PYTHON_PATH
    my_process = _APP_BIN_HOME + "/" + wrapped_script




logging.basicConfig(filename=logfilename, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
mylogger = logging.getLogger("ourlogger")
mylogger.debug("wrapper: sys.argv=%s" % sys.argv) 



argstr=''
for thing in sys.argv:
    argstr=argstr + " " + thing

# [os.environ['PYTHONPATH'], my_process, _SPLUNK_PYTHON_PATH, sys.argv]
#p = subprocess.Popen([os.environ['PYTHONPATH'], my_process, _SPLUNK_PYTHON_PATH ] + sys.argv[1:] , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
#p = subprocess.Popen([os.environ['PYTHONPATH'], my_process, sys.argv], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p = subprocess.Popen([os.environ['PYTHONPATH'], my_process, _SPLUNK_PYTHON_PATH ] + sys.argv[1:] , stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
#output = p.communicate()[0]
#sys.stdout.write(output)
#sys.stdout.flush()

