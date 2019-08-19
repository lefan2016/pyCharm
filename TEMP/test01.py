# coding=utf8

import os
import maya.mel as mel
import maya.cmds as cm
import shiboken2
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets

def get_maya_window():
    window = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(window), QtWidgets.QDialog)


PROGRESSBAR = mel.eval('string $temp = $gMainProgressBar')


def start_progress(count):
    cm.progressBar(PROGRESSBAR, e=True, beginProgress=True, isInterruptable=True, maxValue=max(count, 1))


def move_progress(message):
    cm.progressBar(PROGRESSBAR, e=True, step=1, status=message)


def end_progress():
    cm.progressBar(PROGRESSBAR, e=True, endProgress=True)


def get_start_dir(start_dir):
    if os.path.isfile(start_dir):
        start_dir = os.path.dirname(start_dir)
    elif os.path.isdir(start_dir):
        pass
    else:
        start_dir = cm.workspace(q=True, listFullWorkspaces=True)[0]
    return start_dir

