#!/usr/bin/env python3
#! /usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
Main command-line interface to PyInstaller.
"""
# from  PyInstaller import  *
import  os

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    #opts=['main_Qthread.py','-F','-w','--icon=ic.ico','--name=DHCP_Client_Simulator v1.1','--version-file=version.txt']
    #opts=['Main_DHCP.py','-F','-w','--icon=ic.ico','--add-data=window1.ui;.','--add-data=icon.png;.','--name=DHCP_Client_Simulator v1.5','--clean']
    opts=['Jacky_main.py','-F','-w','--icon=ic.ico','--add-data=jacky_gui.ui;.','--name=Jacky_first_gui','--clean']
    #opts=['Main_DHCP.py','-F','-w','--icon=ic.ico','--add-data=window1.ui;.','--add-data=window2.ui;.','--add-data=icon.png;.','--name=DHCP_Client_Simulator v1.5','--clean']

    run(opts)
    #run_makespec(opts)
