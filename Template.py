import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

Project_Name = "MLProject"

List_of_files= [".github/workflows/.gitkeep",
f"src/{Project_Name}/__init__.py" ,
f"src/{Project_Name}/components/__init__.py",   
f"src/{Project_Name}/utils/__init__.py"  , 
f"src/{Project_Name}/utils/common.py"   ,
f"src/{Project_Name}/config/__init__.py"   ,
f"src/{Project_Name}/config/configuration.py",   
f"src/{Project_Name}/pipeline/__init__.py"  , 
f"src/{Project_Name}/entity/__init__.py"   ,
f"src/{Project_Name}/entity/config_entity.py"  , 
f"src/{Project_Name}/constants/__init__.py"   ,
"config/config.yaml",
"params.yaml",
"schemaa.yaml",
"main.py",
"app.py",
"Dockerfile",
"requirements.txt"  ,
"setup.py",
"research/trails.ipynb",
"templates/index.html"  ,
"test.py"

]



for filepath in List_of_files:
    filepath= Path(filepath)
    filedir,filename= os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating_directory; (filrdir) for the file:{filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
         pass
        logging.info(f"create empty file:{filepath}")


    else:
          logging.info(f"{filename} is already exists")