'''
Created on 31 Mar 2020

@author:     Simon M.C.Yuen
@contact:    simoncpeg@gmail.com
'''


class ChamberManager(object):
    '''
    This class is to simulate the particle movement inside a chamber.  The particles would
    continue to move until all are out of the chamber. The animate function would return the
    locations of particles at each moment.
    '''
   
    def __init__(self, speed, initCondition):
        self.speed = speed
        self.chamberSize = len(initCondition)       
        self.leftwardParticles = [False] * self.chamberSize
        self.rightwardParticles = [False] * self.chamberSize
       
        i = 0
        for c in initCondition:
            if (c == 'L'):
                self.leftwardParticles[i] = True
            if (c == 'R'):
                self.rightwardParticles[i] = True 
            i = i + 1
         
    def move(self):
        for x in range(self.chamberSize):
            if (self.leftwardParticles[x]):
                self.leftwardParticles[x] = False 
                if (x - self.speed >= 0):
                    self.leftwardParticles[x - self.speed] = True
                  
        for x in reversed(range(self.chamberSize)):
            if (self.rightwardParticles[x]):
                self.rightwardParticles[x] = False  
                if (x + self.speed < self.chamberSize):
                    self.rightwardParticles[x + self.speed] = True
                              
    def isEmptyChamber(self):
        result = True
        for x in range(self.chamberSize):
            if (self.leftwardParticles[x] or self.rightwardParticles[x]) :
                result = False
        return result

    def getParticleLocation(self):
        particleLocations = ''
        for x in range(self.chamberSize):
            if (self.leftwardParticles[x] or self.rightwardParticles[x]):
                particleLocations += 'X'
            else:
                particleLocations += '.'
        return particleLocations       
    
    def animate(self):
        animations = list()
        animations.append(self.getParticleLocation())
        while (not self.isEmptyChamber()):
            self.move()
            animations.append(self.getParticleLocation())
        return animations
    
