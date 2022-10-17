# SLES-Drone
The homepage for the St. Luke's Episcopal School Robotics Drone Project.

This repository was part of a project to create a working drone during the spring/summer of 2020. The scripts here handle wireless communication between a piloting computer and the drone, sending and receiving command inputs over a local network and passing flight control commands to a controller board. 

# Cloning the Script

The main script is called flightcontroller.py and cloning it to a linux system such as a raspberry pi is very simple. 
Simply navigate to the directory that you want the script in and run "git clone https://github.com/conifer0us/SLES-Drone Drone_Script".
This command will create a directory called Drone_Script and within it construct a .git filesystem. This .git filesystem should contain all necessary code files and this README.md file as well. 

# Editing the Script

Editing the script will be easy to do online through GitHub for small changes, as it allows collaborative editing (although not in real time like Google Docs). 
Once you create a GitHub account, you should be able to go to https://github.com/conifer0us/SLES-Drone and the project files will be stored there to edit. Once you are done making edits, select make new branch for this commit and start a pull request. This option is incredibly important because it allows for editing on personal time, but code will not be officially updated to include your edits until everyone has discussed and agreed that the code additions are valuable ones. Once it is agreed upon, the request will be committed and the code updated. 

# A Better Way to Edit the Script

Once your computer has been set up with SSH keys to connect to the GitHub server, files have been included in the repository that make it easy to pull changes and push changes. First, in the command line, run "./pull_changes.sh" (this may need to be preceded with a 'sudo' in order to run the script as administrator). This will automatically update your device's information to that available on the server. Once you are done editing the script, run "./push_changes.sh" to update the server. This command will ask you for a short and long git commit message. Provide a simple summary in the short message and a longer description in the long commit message. This is important so that everyone can see what changes you made to the script later on. 

# What Each File Does

Flightcontroller.py is a python script to be used for drone testing purposed on the raspberry pi itself. This should be run as a superuser (sudo) and reads only keyboard input into the pi, not over the network.

Network_FlightController.py is the same as flightcontroller.py except it reads network input instead of direct keyboard input. This script is started automatically by the startsession.py script, and it should not be necessary to start it manually except for testing purposes. If it is started manually from the Linux terminal with network access on port 9000 piped into it. This looks like "nc -lk -p 9000 | sudo python3 Network_FlightController.py". To send output information over the network as well so that ReadSession.sh is capable of capturing it, pipe the output data of the function into "nc ip_of_controller 9001". This can be very confusing, and startsession.py does it automatically, so I would not recommend toying with piping inputs and outputs from the network. 

startsession.py is the script that is run by whatever computer is being used as the controller. This script starts the network enabled flightcontroller script on the raspberry pi and directs the output through the network as well. It is important to change the ip of the raspberry pi and controller computer in the script (these are variable names with comments beside them telling that they need to be changes). The port used to direct communication to the pi is port 9000, and port 9001 is used to send script output back to the controller computer. 

ReadSession.sh is a shell script that should be run to read the session data coming from the raspberry pi. ReadSession.sh should be run from the command line using ./ReadSession.sh in a separate window from the startsession.py window. _Keep the startsession.py and ReadSession.sh windows both open at the same time. Your focus should be on the startsession.py window to send input to the pi, and the ReadSession.sh window is reading the data that the pi is sending to you._

pull_changes.sh should be run ./pull_changes.sh and pulls the changes made to the script on this repository down to your local machine. If this fails because of an error with username/password or ssh keys, simply run 'git pull' or 'sudo git pull'. 

push_changes.sh should be run ./push_changes.sh and pushes all changes that you have made to any of these files to this remote repository. This requires two messages, a short message and a longer, more detailed one. Make these messages clear so that someone looking back on what you have pushed can understand what you have done. 