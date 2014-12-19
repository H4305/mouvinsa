MouvINSA
========

Directory Structure
-------------------
- __app__: the flask app
- __db__: database relative files
- __diagrams__: project diagram files
- __env__: vagrant environment files
- __mockups__: UI mockups and models (.psd files are to big too be shared)
- __presentations__: presentation files

Installing the environment
--------------------------

Make sure you have a fast internet connection, you will be downloading something around 800Mb.

- Download Vagrant: https://www.vagrantup.com/downloads.html
- Install vagrant.

- Git clone this project.
- Open a shell, go to the env directory
- Run: vagrant up
- Wait for the installation process

###TA-DA!

Now you can access your server at the adress:
> http://localhost:8080

The MySQL server is available at `localhost:3306`

######Some useful vagrant commands:
  - __vagrant up__: lauches the virtual machine
  - __vagrant ssh__: connects to the virtual machine through ssh
  - __vagrant reload__: reloads the virtual machine
  - __vagrant halt__: stops the virtual machine
  - __vagrant destroy__: destroys the virtual machine

If you need to install something new to the virtual machine don't do it directly via ssh.
Add the necessary commands to the `vagrant/provisioning.sh` file, destroy the VM and install it again.
This way you can commit and share the exact same environment with everyone else.

Pushing & Branch rules
----------------------
If you have something working, that you can show, even if it is not finished and every other changes from the others are well integrated with yours, you can push it into "master".
When everybody agreed on the changes we can push it into "final".
At the end, we can push it in "prod"

__ When you are working and testing, use your OWN branch  ! __

### A little reminder

To create a branch : ```git checkout -b NomDeLaNouvelleBranch```
To switch to another branch : ```git checkout LaBranche```
To merge a branch into another : 
```
git checkout laBranchDansLaquelleOnVeutMerger
git merge laBrancheAMerger
```


##Have fun :)
