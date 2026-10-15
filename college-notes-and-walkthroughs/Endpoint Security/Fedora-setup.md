# Setting up a Fedora VM on your VirtualBox

If you have already installed Oracle VirtualBox on your system, that is great!  
If not, no worries! You can check the Kali and Vbox setup in Applied security and Network defense directory.

The steps are pretty simple and as of this moment (Oct, 2026) the latest release of Fedora is the Fedora workstation 44. 
1. You can head to this URL or google "Fedora Download" on your browser. Click on the "Download" button for Intel and AMD systems.
<img width="929" height="510" alt="image" src="https://github.com/user-attachments/assets/7d06dd7a-e235-4b52-b698-8d2ef98ecd1b" />

2. It should show up in your browsers download queue or history like given below
<img width="314" height="53" alt="image" src="https://github.com/user-attachments/assets/046264dc-5f4f-4b01-905c-56140f5de31f" />

3. Now open up the Vbox and click on new.
<img width="431" height="524" alt="image" src="https://github.com/user-attachments/assets/7903f2c1-6c91-4571-a70a-ed308f6ce282" />

4. Name your VM, I put in "Fedora" for simplicity sake. After that you have to select the folder in which your ISO file was downloaded.
Note that we need only the folder, not the actual ISO. Vbox has the default path for its VMs but since our ISO file is in a different location
we need to change that by clicking on others and specifying the folder.
<img width="593" height="410" alt="image" src="https://github.com/user-attachments/assets/fc513664-1eab-4d43-9add-6377120459dc" />

5. After specifying the folder, select the ISO file. Note that this step can be different based on where your ISO file is located in. It's default download location will be the "Downloads" folder unless specified otherwise.
<img width="466" height="354" alt="image" src="https://github.com/user-attachments/assets/cab1b0bd-f43a-40f1-b610-5a60405cd2b4" />

6. Select the ISO file and load it in.
<img width="464" height="347" alt="image" src="https://github.com/user-attachments/assets/73821e7c-6dd6-42b8-92c6-965339c3d22a" />

7. You will see your new Virtual Machine window as given below and we just have to click the finish button.
<img width="596" height="412" alt="image" src="https://github.com/user-attachments/assets/3727f5c0-d6d1-402b-9426-c1f76bbfe52e" />

8. Now you will notice a new machine has been added to your list of VMs. Now a thing to check is the actual details of your VM. Vbox defaults to the lowest settings possible but Fedora (GNOME) requires a recommended 4GB RAM and decent Video memory and 2 CPU cores to work comfortably.
If your laptop has a good amount of RAM (16GB/32GB), good video memory and multiple CPU cores then it is completely fine and we can change the settings. Here I have already changed it to the recommended settings for the GNOME desktop.
<img width="925" height="499" alt="image" src="https://github.com/user-attachments/assets/e54a477b-278f-4ffc-a076-4810291205de" />

9. If you see different numbers and specifications then you can easily modify them by going to the settings.
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/1d54db06-1ecb-4345-b999-5b93addc2374" />

10. In the System settings, you can change the base memory then scroll down to change video memory. You can then go to the Processor tab and change number of cores to 2.
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/3224aaec-b43b-44ba-ae97-e76293d160c7" />
<img width="954" height="536" alt="image" src="https://github.com/user-attachments/assets/bb43132d-81ba-4b1f-b7f8-d66f03307719" />
<img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/ef52dec4-5421-44b9-b753-293205b241c8" />

11. Now we can start the VM. After starting it, you will see the VM open in a new window. You can follow the on-screen instructions for installing the Fedora ISO and finish it.
After the install is done, you should restart your VM. and you are all good to go!
<img width="477" height="309" alt="image" src="https://github.com/user-attachments/assets/d49628a6-0f56-44fe-bcb1-0b0811d08f8a" />

If at all you faced any difficulties or problems during the installation or setting up process that I didnt cover here then please dont be shy to use google and find out the solution.
Googling is also an art and using it effectively makes a lot of difference.

-Syed Abdul Rauf



