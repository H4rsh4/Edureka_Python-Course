from math import sin, cos, atan2, sqrt, radians

# Formula : https://ttarnawski.usermd.net/2017/08/17/haversine-formula/


pos = [(radians(43.089316), radians(-79.066355)),(radians(34.152464),radians(77.576112))]

R = 6371 #Radius of Earth

deltaLat = pos[1][0]-pos[0][0]
deltaLon = pos[1][1]-pos[0][1]

a = (   sin(deltaLat/2)**2
            +  
        cos(pos[0][0])
            *
        cos(pos[1][0])
            *
        sin(deltaLon/2)**2
    )
c = 2* atan2(sqrt(a), sqrt(1-a))
d = R*c
print(f'{round(d,3)} KM')
