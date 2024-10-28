import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/moon/project/Pixhawkdrone/dev_ws/install/drone'
