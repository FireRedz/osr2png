import json, os
from types import SimpleNamespace
from shutil import copyfile

import logging, sys
from autologging import logged, TRACE, traced

def getSizeMultiplier(height):
    return height/720 # HOW IS THIS WORKING

def getSizeMultiplier_(pixel: int):
    ''' this is retarded how tf am i supposed to calc resize shit '''
    defaultPixel = 921600 # 1280x720
    return (pixel/defaultPixel)*1


@logged
@traced
def loadConfig():
    if not os.path.isfile('config.json'):
        print('no config found!')

        copyfile('res/config.sample.json', 'config.json')



    with open('config.json') as file:
        res = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))

    return res


def saveConfig(settings):
    with open('config.json', 'w') as f:
        f.write(json.dumps(settings.__dict__, indent=4))

    print('Config Saved!')


def checkFolder(settings):
    if not os.path.isdir(settings.outdir):
        os.mkdir(settings.outdir)
    if not os.path.isdir('cache'):
        os.mkdir('cache')