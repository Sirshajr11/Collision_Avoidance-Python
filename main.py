import math
import pygame

from ROBOT import Graphics ,robot ,Ultrasonic


MAP_DIMENSIONS=(600,1200)

#Environment Graphics
gfx=Graphics(MAP_DIMENSIONS,'Robot.png','Enviro.png')


#The AUV
start=(200,300)
Robot=robot(start,0.01*3779.52)

#Sensor
sensor_range=250,math.radians(40)
uLtra_sonic=Ultrasonic(sensor_range,gfx.map)

dt=0
last_time=pygame.time.get_ticks()

running=True

#Simulation Loop
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    dt=(pygame.time.get_ticks()-last_time)/1000
    last_time=pygame.time.get_ticks()

    gfx.map.blit(gfx.map_img,(0,0))

    Robot.kinematics(dt)
    gfx.draw_robot(Robot.x,Robot.y,Robot.heading)
    point_cloud=uLtra_sonic.sense_obstacle(Robot.x,Robot.y,Robot.heading)
    Robot.avoid_obstacles(point_cloud,dt)
    gfx.draw_sensor_data(point_cloud)

    pygame.display.update()


