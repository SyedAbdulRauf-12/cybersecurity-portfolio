# Setting up a pfSense firewall VM on your VirtualBox

This is a guide / walkthrough to setup a pfsense firewall standalone machine on your VirtualBox, 
you need a pfSense ISO image, proper hardware allocation, and at least two virtual network adapters 
(one for WAN and one for LAN) all of which will be available on your laptop assuming it has decent specs.

## What is pfSense firewall? 
pfSense is a Netgate-maintained, FreeBSD-based open-source router and stateful firewall configured entirely through 
a web GUI with built-in VPN, multi-WAN, and modular package support (e.g., Snort, Squid).  
If you didnt get all that technical jargon then think of pfSense as a digital security guard and traffic controller for your network—it blocks online threats, directs internet traffic, and lets you manage everything through a simple website.

## Download and Install
Lets get right into the downloading and installation of pfSense firewall, a *pre-requisite* is that you need to sign up for a netgate account because even though the community edition
is free, Netgate treats it like a product that you have to go through billing for. Follow along with the steps given below.

1. Open up your browser and type "pfsense download" into your search bar or copy the URL from the image given below. Press the blue download button.
<img width="929" height="512" alt="image" src="https://github.com/user-attachments/assets/fd159745-d624-4e6b-bfb0-32958a0bc19f" />

2. It should take you to this page, make sure you have completed the *pre-requisite*. Now select the "AMD64 ISO IPMI/Virtual Machine".
Click on the "Add to cart" button.
<img width="929" height="511" alt="image" src="https://github.com/user-attachments/assets/aa86432b-b3df-46f9-9c93-c986e96ac6e8" />

3. After clicking add to cart, a window should pop-up from below like shown in the image. Press "Enter cart".
<img width="929" height="509" alt="image" src="https://github.com/user-attachments/assets/da3f69f3-b734-4e08-b845-c2695ab3a971" />

4. Proceed to checkout the free product in our cart.
<img width="929" height="511" alt="image" src="https://github.com/user-attachments/assets/479c1c8a-c818-465a-9d60-822ce9242a2b" />

If you see the image below, then you didnt complete the *pre-requisite*.
<img width="928" height="510" alt="image" src="https://github.com/user-attachments/assets/8d8ac0aa-a207-4c13-9613-fb5db92498c5" />
For those of you who completed the *pre-requisite*, you will see the following screens. You enter your details and finish the order by checking the
box and clicking on "Complete Order".
<img width="583" height="449" alt="image" src="https://github.com/user-attachments/assets/5737faa3-2d7b-4e3c-b18d-46b0f013469d" />
<img width="1153" height="708" alt="image" src="https://github.com/user-attachments/assets/7dddfb31-9ecf-449f-8748-039c5527cf16" />

5. After that, you will be shown this screen. Click on the download now button for our net-gate installer.
<img width="930" height="461" alt="Screenshot 2026-10-16 205310" src="https://github.com/user-attachments/assets/7ea39056-eb3c-497b-a4ff-25e1d42961bf" />

6. The download will start on your browser. After it is completed, It will show up on your browsers downloads.
<img width="929" height="509" alt="Screenshot 2026-10-16 205531" src="https://github.com/user-attachments/assets/b8dde5a0-acca-428d-92f3-8862e46786a5" />

7. The download is now complete and now we got to extract it to continue with our installation. Select a destination folder of your choice.
Preferrably with good space.
<img width="438" height="360" alt="Screenshot 2026-10-16 205921" src="https://github.com/user-attachments/assets/79cfde1b-e6d4-48e4-8c74-9aaa11bdfff2" />

8. This is after the file has finished the extraction. Now the next steps are important and be careful while doing it. Dont be afraid to start over again and again.
<img width="539" height="530" alt="Screenshot 2026-10-16 205944" src="https://github.com/user-attachments/assets/51422891-7cc1-404d-841a-2e5d696c71ad" />

9. Open the VirtualBox application and click on "New". We have to mount the ISO file and install the pfSense firewall into VirtualBox.
<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/61e8bc60-4841-4eaf-9a57-a953ff5b0527" />
  
10. In the window that pops up, We must name the new machine, following best practices we name is "pfsense_firewall". Next, we select the folder where the ISO file is located.
We select the directory and head on to the ISO file upload. It will show us the ISO file, we select it and click on "Open".
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7617a755-153d-4b95-bcac-2354d1aeb446" />

11. After we are done with that, we must make sure that we change the OS to "BSD", the other fields will change automatically after selecting it in the 1st.
We now click on "Finish".
<img width="1188" height="819" alt="image" src="https://github.com/user-attachments/assets/3abcd438-06ea-4f57-af6c-02275ace3f84" />

12. After finishing that, We will see the pfsense_Firewall machine listed among our other VM's.
Pat yourself on the back for making it this far, we got to celebrate the little wins in life! Lets start it up and actually set it up!
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/12f912f9-06b7-4cbf-a5c1-04cf7dfe6cc6" />
<img width="362" height="203" alt="image" src="https://github.com/user-attachments/assets/7411f6fb-05e7-48b2-8796-0f0a70ce48a1" />

13. Now after this, It gives you a few seconds before it starts its autoboot.
It should look something like the image given below. Give it a few seconds.
<img width="368" height="205" alt="image" src="https://github.com/user-attachments/assets/0066e8ba-353c-47e4-acb0-7561d52f5a99" />

14. After that, it should open up the image given below. Point to note is that this doesnt capture your mouse and it has no role to play here.
Everything is done using the keyboard.
<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/d087afde-6d35-4656-b726-8e166f111ef7" />

15. Then, it moves to the next window where it will ask to start the install or perform some other actions, they are irrelevant for us right now
but feel free to explore.
<img width="554" height="250" alt="image" src="https://github.com/user-attachments/assets/a889f21c-38ae-4033-bea3-0ce9eef26888" />

16. Just keep hitting enter (give it a few moments in case it feels unresponsive) for the default settings until
you hit this screen.
<img width="618" height="250" alt="image" src="https://github.com/user-attachments/assets/898fbaf0-a677-4cf5-b42d-ddc4d2c8ec7b" />

As we dont have the pfSense plus subscription, we will now be proceeding with the "Free" Community edition of pfSense. Press Enter.

18. Just keep hitting enter with the default selections because they are already on the recommended settings. 
<img width="474" height="234" alt="image" src="https://github.com/user-attachments/assets/5d7c4849-1eec-4fd4-bd77-2a93f3a78483" />

It will ask us for confirmation to wipe the disk and re-writing on the disk. Since we are using Vbox, it will be stored in the VBox hard drive. Press Enter.  

<img width="418" height="186" alt="image" src="https://github.com/user-attachments/assets/c9d05535-e8b5-4e3e-a617-a735cef134e7" />  

When it asks the version, select the **_Current Stable Version_** and hit ENTER.  

19. Now wait until the installation finishes. It should take a few minutes.
<img width="370" height="194" alt="Screenshot 2026-10-18 140733" src="https://github.com/user-attachments/assets/6327fc37-372f-4ec3-b6e7-c7bb4c57c53d" />

After it is done, it will display a pop-up.  

<img width="418" height="154" alt="image" src="https://github.com/user-attachments/assets/e06dfb28-833e-45d9-b9ec-f1dea35a0534" />  

But do not press ENTER right away, we need to remove the ISO file that is mounted, so when it re-boots, it should boot up from the
virtual hard disk we just installed it to and not the ISO file. 

21. Go to the window in which the machine is running and select **"Devices"**, from the drop-down, select **"Optical-Drives"**
Then you should see the current ISO file selected and click on remove disk from virtual drive. If another window pops up, click on force stop and then reboot the machine.
<img width="1620" height="489" alt="image" src="https://github.com/user-attachments/assets/9445e571-afc4-4583-9846-577d0e7e3c6d" />

It should reboot normally. If it doesnt and opens a terminal at the bottom of the machine window, then just select **"Machine"** at the top of the window
and select **"Reset"**. It should finish normally and reboot, You should be able to see this screen.  
<img width="366" height="206" alt="image" src="https://github.com/user-attachments/assets/cf7b45c8-4cf7-4c02-aefc-879b2bdfb3f1" />  
Don't worry if the screen is not EXACTLY the same as what you would see. I have made a different guide for setting up the networks for pfsense.


That is all for this guide / walkthrough. If at all you faced any troubles or problems during the download or installation that I didnt cover
please do not hesitate to google your problem and straighten it out. I will attach the link to Net-Gate's original installation walkthrough for more in-depth information which I highly recommend reading.  
[Net-Gate Walkthrough](https://docs.netgate.com/pfsense/en/latest/install/install-walkthrough.html)  

Googling is an underrated skill and can make life much easier.  
As always, stay curious, explore and learn from your experiences!

-Syed Abdul Rauf, 2026.

