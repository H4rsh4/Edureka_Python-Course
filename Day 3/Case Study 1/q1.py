point = [0,0]
commands = ["UP 5", "DOWN 3","LEFT 3","RIGHT 2"]
for command in commands:
    steps = command.split()
    if steps[0] == 'UP':
        point[1]+=int(steps[1])
    elif steps[0] == 'DOWN':
        point[1]-=int(steps[1])
    elif steps[0] == 'RIGHT':
        point[0]+=int(steps[1])
    elif steps[0] == 'LEFT':
        point[0]-=int(steps[1])
x1 = 0
y1 = 0
x2 = point[0]
y2 = point[0]

'''Distance formula: S = ((x2-x1)**2+(y2-y1)**2)**1/2   or math.sqrt((x2-x1)**2+(y2-y1)**2)'''
Final_Distance = ( (x2-x1)**2 + (y2-y1)**2 )**(1/2)