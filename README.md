# ML_projectStructure_setup
Creating containers , CICD pipeline , Deployment on Heroku

**taking base structure from projectDockerization--CICD REPO

STEPS:-
1) created folder called housing and within that __init__.py file.
2) setup.py file
3)run command pip install -r requirements.txt ( as python setup.py install is giving problems)




NOTES:-

point 1:-
setup.py -> 
1) to install all the libraries mentioned in RQUIREMENTS.TXT file ( by doing this ,  we can avoid manually installing all the libraries by writing command pip install -r requirements.txt) .  [LINE NO 34]
2) to install our custom packages , in our case housing [LINE NO 33]
"""
python setup.py install
"""

***If setup.py is giving some issues in running, so go with manual installation pip install -r requirements.txt.But remember :-
     ADDING -e . in requirements.txt will take care that package/folder conataining __init__.py ( example housing) gets installed .  
    -e . internally use setup.py file  
    find_packages() is equivalent to -e . 



2) .egg file contains information abt our custom package ( example housing)


3) __init__.py -> we are converting housing into a package and for that __init__.py file is required.
Now this housing package can be called form any other file.