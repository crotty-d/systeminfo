# -*- coding: utf-8 -*-

'''
Created on 25 Jan 2018

@author: Darragh Crotty
'''

import platform

def get_machine_info():
    """Gets basic machine information via platform module"""
    return platform.machine()

def get_platform_info():
    """Gets basic platform information via platform module"""
    return platform.platform()
    
def get_version_info():
    """Gets version information via platform module"""
    return platform.version()


def main():
    """Prints some basic information about the system"""
    
    print('Machine:', platform.machine())

    print('OS:', platform.platform())
    
    print('OS version:', platform.version())
    
    
if __name__ == '__main__':
    main()
