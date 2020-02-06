import game as g

ball = g.Sprite("ball")
v_wall = g.Sprite("v-wall", 3,1)
h_wall = g.Sprite("h-wall",1,3)

scrn = g.Game(20,20)

scrn.add_sprite(ball,10,10)

scrn.add_sprite(v_wall,7,10)
scrn.add_sprite(h_wall,12,12)

scrn.print()

scrn.move_sprite(ball, 1,1)

scrn.print()

scrn.move_sprite(ball, 1,1)

scrn.print()

scrn.move_sprite(ball, 1,1)

