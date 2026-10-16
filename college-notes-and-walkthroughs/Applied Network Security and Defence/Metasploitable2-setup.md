# Setting up Metasploitable 2 VM on your Vbox

This setup guide/walkthrough will help you download, extract and add the "Metasploitable 2" VM on your virtual box.

## What is Metasploitable?
Metasploitable is a intentionally vulnerable machine that is developed by Rapid7 and has multiple versions, Metasploitable 2 and 3.  
(For the remainder of the guide/walkthrough I will refer to Metasploitable 2 as Meta 2 because its too long to type for me.)  
Meta 2 is an older and widely used Ubuntu linux based VM which is packed with the classic security flaws. It is usually used for cybersecurity training, practicing pen-testing and security testing tools.  
Meta 3 is a bit more modern and modular VM which supports both Ubuntu and Windows server environment.  
Since this is a vulnerable machine, NEVER expose it to the public internet or untrusted network or you could become a target for attacks. Always run this machine on a hypervisor like VirtualBox or VMware.

## Installation:
1. On your local browser, type in "Metasploitable 2 download". Click on this link which will take you to the download page. 
<img width="761" height="145" alt="image" src="https://github.com/user-attachments/assets/a308540a-640c-43c3-a3b8-62ff41a05c16" />

2. Click "Download" and wait for it to finish downloading. It should take a couple of minutes
<img width="927" height="510" alt="image" src="https://github.com/user-attachments/assets/b4ab9143-c6df-4367-b7b5-e82fef07f259" />

3. After you finish the download, head to the folder where it was downloaded and extract the zipped folder to a location of your choice.
<img width="461" height="374" alt="Screenshot 2026-10-16 094158" src="https://github.com/user-attachments/assets/0d15a308-8a4a-4934-82ff-2c0ed23b3ff0" />

4. Now that the extraction is done, you will see the extracted folder pop-up.
<img width="848" height="539" alt="Screenshot 2026-10-16 094232" src="https://github.com/user-attachments/assets/7bae8508-c437-4a0c-9807-4117439b967b" />

## Setting it up on your Vbox:
5. Now head on over to your VirtualBox application and click on "New".
<img width="959" height="539" alt="Screenshot 2026-10-16 094358" src="https://github.com/user-attachments/assets/7186d800-70e4-4b38-bd71-f1bf0ca2c423" />

6. Give your new VM a name, I named it "Metasploitable 2" for simplicity's sake and because its a good habit which otherwise could cause confusion if you have multiple VM's like me. Also select the folder where your Meta 2 files are located.
<img width="593" height="412" alt="Screenshot 2026-10-16 095243" src="https://github.com/user-attachments/assets/b9856afd-1f34-4a37-a61a-5196255e4bd1" />

7. After you have done that, now we dont have an ISO file here to insert, instead we are going to click on the "Specify Virtual Hard Disk" drop-down and select the "Use Existing Virtual Hard Disk" option. 
<img width="598" height="415" alt="Screenshot 2026-10-16 095259" src="https://github.com/user-attachments/assets/8b34706d-e3ef-487a-9f53-051f1fefbc90" />

Click on the "Folder" icon on the right side of the bar. Click the "Add" button where you will have to navigate to the extracted folder and select the file with the ".vmdk" file extension. Once everything is loaded in and done, click Choose.
<img width="1291" height="960" alt="image" src="https://github.com/user-attachments/assets/bdc2f0da-29bd-429e-b5d7-034981944a12" />

9. After clicking Finish, You should see the new VM appear in your list.
<img width="1917" height="1071" alt="image" src="https://github.com/user-attachments/assets/566a9557-3fe0-420e-ad0f-b0f0512ec856" />

10. That's the easy part done. Now you are going to have to check if all your configuration is correct or not. Select your Meta 2 VM and click on settings. In the General settings, make sure it matches what the images shows.
<img width="957" height="538" alt="Screenshot 2026-10-16 100837" src="https://github.com/user-attachments/assets/515c2ddd-690c-4aac-b993-7a63b786940d" />
<img width="956" height="533" alt="Screenshot 2026-10-16 100754" src="https://github.com/user-attachments/assets/e395a654-c87a-47bf-ae66-133baaca1ccd" />

11. Go to the "Network" window inside "Settings", There you will configure the network settings to match the image. This is done so that the Meta 2 machine will not have access to the public internet but remains discoverable by your local Kali machine to practice on.
<img width="581" height="381" alt="image" src="https://github.com/user-attachments/assets/ce7e74fd-e257-4993-8832-429ccf6f9f05" />

12. After all that is done, you can start your VM, It will open in a new window and will initialize.
<img width="359" height="266" alt="Screenshot 2026-10-16 101325" src="https://github.com/user-attachments/assets/ad773f85-fd67-4368-a689-d2e55fc44e0e" />

13. You can login with the already given credentials on the screen. Pretty insecure right? 
<img width="560" height="391" alt="Screenshot 2026-10-16 101405" src="https://github.com/user-attachments/assets/2128189a-f6f2-469c-a856-9df826d60953" />

As always, if you faced any difficulty or problems while following this walkthrough/guide, dont hesitate to google it and straigten them out. The art of googling is an 
underrated skill.  
Remember that this is a vulnerable machine and to be careful while performing operations on it. If you feel anything is unclear to you 
or you didnt understand anything feel free to contact me on my [Discord](https://discord.gg/CzrgWEsfK) or you can just google it.  
Either way, Stay curious and explore new things and always keep learning!

-Syed Abdul Rauf, 2026.
