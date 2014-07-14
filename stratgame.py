'''
Created on 29.03.2014

@author: Chris
'''
import sys, os
# Setup PYTHONPATH
appPath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, os.path.join(appPath, "modules"))
sys.path.insert(1, os.path.join(appPath, "modules", "aview"))
sys.path.insert(1, os.path.join(appPath, "modules", "controller"))
sys.path.insert(1, os.path.join(appPath, "modules", "model"))
sys.path.insert(1, os.path.join(appPath, "modules", "util"))
sys.path.insert(1, os.path.join(appPath, "config"))

from consoleReader import ConsoleReader
import logging.config

def main():
    # Set logging config
    logging.config.fileConfig(os.path.join(appPath + '\\config\\log.config'))
    
    # Start the Console reader in a new Thread
    cr = ConsoleReader()
    cr.start()
    cr.join()
    
    
if __name__ == '__main__':
    main()