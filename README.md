# PathingAlgo
For a programming competition, I was tasked with designing a pathing algorithm that solves mazes built with hexagonal grids


the hexagonal boxes are represented with the hexagonal effective coordinate system
postion is based on a a,r,c coordinate

example:

![HECS_Nearest_Neighbors](https://github.com/Spiratatoe/PathingAlgo/assets/95253269/d73ed832-48cf-40ab-a89a-1d171fe3ca26)



https://en.wikipedia.org/wiki/Hexagonal_Efficient_Coordinate_System

the code needs to read mazes that are sent to you via json files 

**Solution :**
I used an A* algorithm that follows the shortest path, if it reaches a dead end it comes backward to the next shortest path until it reaches the final position 

Once done it loops through the list of steps it took to find the official shortest path !



