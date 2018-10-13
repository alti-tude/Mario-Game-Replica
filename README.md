# Super Borio Bro V2.3.5.8 (boring ppl since sometime in August)
~20171018  

### Running the game:  
* "python3 main.py" in the root Directory
* configs are in config.py (better left untouched tho)

### Controls:  
1. w to jump
2. a to move left
3. d to move right
4. x to fire (only in boss battle)
5. q to quit

### Enemies:
    1. jump on enemies to kill them
        mmm
        {o}    ->   Goombas (movement and collision detection enebled)
        w w

         + 
        / \    ->   Fast Roomba (smart, like really smart)
        uuu
    
    2 Boss (figure that one out)


### What is unique here?
    * endless replayability due to random level generation
        - get a new challenge everytime you start anew, with no impossible levels!
    
    * COLOR (with the american spelling!!!)

    * level components like pits, bridges and platforms

    * power ups
        - it is said that this box contains the soul of Bowser v0.2, but all you see is cotton candy
            *
           *H*  -> get extra health
            *
    * bullets
        - yep, that happened. Not so family friendly anymore.... hmm... 
        - only for the boss tho :D
    * score
        - for everything you do
    * coins
        - for the lack of a better bullet point
    * progress bar for each level
    * easy extensible stat printing


### OOP(s):
* Inheritance(entity class is inherited by enemies and player)
* Polymorphism(various features are overided of the entity class to 
  give the player and different enemies)
* Encapsulated
* Abstracted

### Bonus:
* smart enemies
* color
* clouds that disappear due to condensation when you touch them

### Directory structure:
├── Board.py  
├── build_level.py  
├── collectible.py  
├── config.py  
├── enemies.py  
├── entity.py  
├── GLOBAL.py  
├── input.py  
├── main.py  
├── Player.py  
└── requirements.txt  
