# Optimal Shipping Routes

This project models a fictional shipping route within a set Map. The "Map" consists of a grid, where every tile is a possible location. The ship must find an optimal route through all of the water tiles, to each of the port tiles, within an inputted timestep for the model to complete its objective. 

Note: if you get an error relating to dsharp, it may be that the dsharp.py file does not know where to find the dsharp file within our project's local directory. The dsharp.py file is located in your local librairy, within 
```
python3.8/site-packages/nnf
```
You must then change the string on line 75 in that file to the path of the dsharp file within our project's local directory:
```
ShippingRoutes/bin/dsharp
```


## Structure
* `run.py`: File that drives the program, where user input is accepted and the model is solved accordingly. 
* `theory.py`: File that contains the working body of the model, where all the interaction with bauhaus is conducted.
* `scenarios.py`: File that generates the five different working maps, outputs them visually, and places ships on the visually displayed map. 

## Dependencies
Install the following for the project to work:
```bash
pip install tabulate
```
```bash
pip install pprint
```
```bash
pip install bauhaus
```