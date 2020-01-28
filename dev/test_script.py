import game as g

r = g.Game(5,12, debugger = True)
r.print()

rock = g.Sprite("Rock", 2, 2)
pebble = g.Sprite("pebble", 2 , 2)
fish = g.Sprite("fish")

r.add_sprite(rock, 2,1)
r.print()
r.move_sprite(rock, 12, 1)
r.print()
