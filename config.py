dispWidth = 99
dispHeight = 30


boardWidth = 999
boardHeight = dispHeight

temp = 0

seed = boardWidth

bullet_sprite = [
    list("@")
]

boss_sprite = [
    list("*******"),
    list("*******"),
    list("*******"),
    list("*******"),
    list("*******"),
    list("*******")
]
#player_code = 1
player_sprite = [
    list("\\o/"),
    list("{ }"),
    list("L L")
]


goomba_sprite = [
    list("mvm"),
    list("{o}"),
    list("w w")
]
goomba_points = 10


fastroomba_sprite = [
    list(" + "),
    list("/ \\"),
    list("uuu")
]
fastroomba_points = 10

cloud_sprite = [
    list("   __   _    "),
    list(" _(  )_( )_  "),
    list("(_ _  _ _  _)")
]

coin_sprite = [
    list("$$"),
    list("$$")
]
coin_points = 5


valid_ip = [
    'w', 'a', 'd'
]

health_sprite = [
    list(" * "),
    list("*H*"),
    list(" * ")
]
tick_size = 0.02
jump_limit = 7
land_code = 3
player_health = 5