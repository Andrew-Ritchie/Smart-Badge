import game as g

r = g.Game(6,6, debugger = False)

rock1 = g.Sprite("Rock", 2, 2)
rock2 = g.Sprite("Rock", 2, 2)
pebble = g.Sprite("pebble", 2 , 2)
fish = g.Sprite("fish")

r.print()
r.add_sprite(rock1, 2,0)
r.add_sprite(rock2, 4,3)
r.print()
r.move_sprite(rock1,2,2)
r.print()

