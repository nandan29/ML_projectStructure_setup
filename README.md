# ML_projectStructure_setup
Creating containers , CICD pipeline , Deployment on Heroku

**taking base structure from projectDockerization--CICD REPO


1) created folder called housing

2) setup.py -> BASICALLY USED , TO INSTALL THE LIBRARIES (numpy , pandas etc etc) MENTIONED IN RQUIREMENTS.TXT FILE ( by doing this ,  we can avoid manually installing all the libraries by writing command pip install.....) .  it is also used when we have to publish libraries.
"""
python setup.py install
"""

***right now setup.py is giving some issues , so go with manual installation pip install -r requirements.txt

-e . => in requirements.txt will take care that package/folder conataining __init__.py ( example housing) gets installed along with other external libraries in txt file. (internally use setup.py file)

*** .egg file contains information abt our custom package ( example housing)


3) __init__.py -> we are converting housing into sort of module or package and for that __init__.py file is required.
Now this housing module can be called form any other file.