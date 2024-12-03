
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# FireBall Survival
## CS110 B1 Final Project  Fall Semester 2024

## Team Members

Matthew Ko

***

## Project Description

This project will be a game where you control a simple character to survive as long as you can while fireballs shoot at you 
2 options for difficulty which are normal and hard mode which will change the speed of the fireballs at the start to make them harder to dodge
2 characters to pick from, with one being slower but small while one is faster but normal sized

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Increasing difficulty as time goes on
2. Timer to compare to friends
3. Different types of fireballs
4. 2 different characters to play
5. 2 difficulty options

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1 test Movement | Press Up/down/left/right|character will move up/down/left/right  |
|  2 Test menus    |Click the start button to see if it starts game, click Quit button to test if it ends the game, and back to menu button sends you back to start|Start button starts the gane, and quit button exits the game and back to menu button sends you back      |
   3 Test game over screen|Test if game over screen shows up if I force a game over by making a game over button|Game over screen appears when i click escape key and exit 
   4 Test collision|Test if touching the fire rectangle can interact with character or if character can go out of bounds|Character can't go out of bounds and collides with fire
   5 Test errors|Test any keys that might cause an error|No errors caused by any invalid inputs