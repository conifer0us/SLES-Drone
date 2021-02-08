# SLES-Drone
The homepage for the SLES Robotics Drone Project.

This repository will contain the python script that will detect GPIO input and pass information on to the flight controller running the drone (and any other files necessary for the project).

# Cloning the Script

The main script is called flightcontroller.py and cloning it to a linux system such as a raspberry pi is very simple. 
Simply navigate to the directory that you want the script in and run "git clone https://github.com/conifer0us/SLES-Drone Drone_Script".
This command will create a directory called Drone_Script and within it construct a .git filesystem. This .git filesystem should contain all necessary code files and this README.md file as well. 

# Editing the Script

Editing the script will be easiest to do online through GitHub, as it allows collaborative editing (although not in real time like Google Docs). 
Once you create a GitHub account, you should be able to go to https://github.com/conifer0us/SLES-Drone and the project files will be stored there to edit. Once you are done making edits, select make new branch for this commit and start a pull request. This option is incredibly important because it allows for editing on personal time, but code will not be officially updated to include your edits until everyone has discussed and agreed that the code additions are valuable ones. Once it is agreed upon, the request will be committed and the code updated. 

# Cloning the Script Directly

I have not yet tested this, but when cloning a specific file from this repository instead of the entire filestructure, you can run "git clone https://github.com/conifer0us/SLES-Drone/main/{filename}". This way, no more files are copied than necessary. 
