# SLES-Drone
The homepage for the SLES Robotics Drone Project.

This repository will contain the python script that will detect GPIO input and pass information on to the flight controller running the drone (and any other files necessary for the project).

# Cloning the Script

The main script is called flightcontroller.py and cloning it to a linux system such as a raspberry pi is very simple. 
Simply navigate to the directory that you want the script in and run "git clone https://github.com/conifer0us/SLES-Drone Drone_Script".
This command will create a directory called Drone_Script and within it construct a .git filesystem. This .git filesystem should contain all necessary code files and this README.md file as well. 

# Editing the Script

Editing the script will be easy to do online through GitHub for small changes, as it allows collaborative editing (although not in real time like Google Docs). 
Once you create a GitHub account, you should be able to go to https://github.com/conifer0us/SLES-Drone and the project files will be stored there to edit. Once you are done making edits, select make new branch for this commit and start a pull request. This option is incredibly important because it allows for editing on personal time, but code will not be officially updated to include your edits until everyone has discussed and agreed that the code additions are valuable ones. Once it is agreed upon, the request will be committed and the code updated. 

# A Better Way to Edit the Script

Once your computer has been set up with SSH keys to connect to the GitHub server, files have been included in the repository that make it easy to pull changes and push changes. First, in the command line, run "./pull_changes.sh" (this may need to be preceded with a 'sudo' in order to run the script as administrator). This will automatically update your device's information to that available on the server. Once you are done editing the script, run "./push_changes.sh" to update the server. This command will ask you for a short and long git commit message. Provide a simple summary in the short message and a longer description in the long commit message. This is important so that everyone can see what changes you made to the script later on. 