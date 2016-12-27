import pygame
from os import listdir
from os.path import isfile, join

DATA_DIRECTORY = "data"

pygame.init()
clock = pygame.time.Clock()

# Configuration for window size
XRES = 480
YRES = 360

loclist = []
drawlist = []

screen = pygame.display.set_mode((XRES,YRES))

# source from http://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def coordinatesToGraph(lat, lon):
    yp = translate(lat, -90, 90, YRES, 0)
    xp = translate(lon, -180, 180, 0, XRES)
    return xp, yp


def getIPlocations():
    onlyfiles = [f for f in listdir(DATA_DIRECTORY) if isfile(DATA_DIRECTORY + "/" + f)]
    for ipfile in onlyfiles:
        ipf = open(DATA_DIRECTORY + "/" + ipfile)
        thing = ipf.readline()
        ipf.close()
        splitthing = thing.split(",")
        loclist.append(splitthing)

    for item in loclist:
        drawlist.append(coordinatesToGraph(float(item[0]), float(item[1])))

def draw():
    screen.fill((255,255,255))
    screen.blit(picture, rect)
    for item in drawlist:
        pygame.draw.circle(screen, (255,0,0), (int(item[0]),int(item[1])), 2, 1)

getIPlocations()
picture = pygame.image.load("Equirectangular_projection_SW.jpg")
picture = pygame.transform.scale(picture, (XRES, YRES))
rect = picture.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit();
    draw()
    pygame.display.update()
    msElapsed = clock.tick(10)
