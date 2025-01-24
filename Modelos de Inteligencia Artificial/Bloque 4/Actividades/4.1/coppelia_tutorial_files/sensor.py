#python

def sysCall_init():
    sim = require('sim')
    simVision = require('simVision')

def sysCall_vision(inData):
    simVision.sensorImgToWorkImg(inData['handle']) # copy the vision sensor image to the work image
    simVision.edgeDetectionOnWorkImg(inData['handle'], 0.2) # perform edge detection on the work image
    simVision.workImgToSensorImg(inData['handle']) # copy the work image to the vision sensor image buffer