# Virtual Box and Kali Linux setup 
This is a guide to setting up your first Virtualization software (Virtual Box) and Virtual Machine (Kali Linux).
The pre-requisites for setting them up is to have a decent laptop and storage space.  
I will list my own laptop specifications down here so you can get a baseline to compare:
- 8GB Ram
- Intel i5 10th Gen processor
- 512GB SSD
- Windows 11 Home

## Virtual Box Download and Installation

Follow the steps below to setup your Virtual Box:
1. Open up your browser and type in "Virtual Box download" or you can enter the URL that is seen in the browser and it should open up this page on your browser.
<img width="959" height="512" alt="Lab-1 00" src="https://github.com/user-attachments/assets/e888005d-452d-43b7-ab81-5e264ac27855" />

2. Click on the Windows host link in the Virtual Box packages. Non-Windows users can click on your corresponding Operating System.
<img width="959" height="475" alt="Lab-1 01" src="https://github.com/user-attachments/assets/59ed9623-e641-4eaa-9723-a9b12c47902d" />

3. The respective package will download to your PC; you can check it in your browsers download history.
<img width="520" height="63" alt="Lab-1 02" src="https://github.com/user-attachments/assets/dc53edd9-59b4-44e9-8aa0-345328d437cf" />

4. Once you run it, It will ask you for permission to make changes to your device then the Virtual Box installation wizard will run where you can configure the install location. I have changed it to the "D:/Oracle" folder, but you can keep the default installation location. This is after the installation is done we can see the folder.
<img width="845" height="476" alt="Lab-1 03" src="https://github.com/user-attachments/assets/98a3bc7c-8ccf-4784-8965-7c62860bcf25" />

5. You can see the Virtual Box folder. The contents of this folder are not exactly relevant right now, but if you are curious, feel free to explore.
<img width="844" height="516" alt="Lab-1 04" src="https://github.com/user-attachments/assets/a3679fad-61c9-41f0-a30f-bae424b1ad2d" />

6. After your installation, the following window will pop up which is the Virtual Box window. If this pops up, it means your installation was successful, Congratulations! If it doesn't, then you can manually open the Virtual Box application by clicking the desktop icon or the "VirtualBox.exe" file that you can find in the folder of step 5.
<img width="722" height="508" alt="Lab1 6" src="https://github.com/user-attachments/assets/f1066a57-3a0c-4410-91a7-ddef3d36e3fe" />

---

## Kali Linux Virtual Machine Download and Installation

Follow along these steps to download and install your very first Kali Linux VM:
1. Type the following on your browser and click on the link.
<img width="959" height="476" alt="Lab-1 0" src="https://github.com/user-attachments/assets/82358c88-9d6f-480c-83e5-57b25848d969" />

2. It will open up this page. Click on Download.
<img width="959" height="539" alt="Lab-1 1" src="https://github.com/user-attachments/assets/0723eef0-5ea3-4c74-b899-d87742f72f37" />

3. Choose your platform. Since we are going to be using it as a VM, select Virtual Machines.
<img width="959" height="539" alt="Lab-1 2" src="https://github.com/user-attachments/assets/343b8e49-d83b-4dc9-b4b9-e447d311fa57" />

4. Click on Virtual Box. The Download will start. It is a big file, so you will have to wait for a bit unless your internet speed is really good.
<img width="959" height="539" alt="Lab-1 3" src="https://github.com/user-attachments/assets/ccf62117-2036-41c4-9c63-9aa38af05a7a" />

5. After the download has completed, you can go the downloads folder and extract all the files to a folder of your preference.
<img width="462" height="392" alt="Lab-1 4" src="https://github.com/user-attachments/assets/fb9193c0-50da-4e44-8a49-e8a13c11aa08" />

6. After it is done extracting, you should see a folder pop up like this. If you see this, Congratulations! Your download and extraction was successful!
<img width="833" height="509" alt="Lab-1 5" src="https://github.com/user-attachments/assets/029fbe3c-30c8-423b-8f14-d0b92e804a07" />

## Setting up your Virtual Box with Kali Linux

Now that we have finished installing both of our requirements, lets get into how we are actually going to access this Kali Linux machine using the V-box. Below you'll find the exact steps to follow:

1. Open up the V-box and click on the big Green Plus sign, that says "Open".
<img width="722" height="508" alt="Lab1 6" src="https://github.com/user-attachments/assets/21ff20c5-a9be-42c4-a611-833e94d6fd78" />

2. It will open a pop-up as shown below, where you have to select the Kali Linux machine for V-box.
<img width="829" height="539" alt="Lab-1 7" src="https://github.com/user-attachments/assets/8779700e-1fb7-4dfa-9fe6-377ceaeb88b3" />

3. After you select that, you should see some changes in your V-box window. Once you see the machine has loaded in, you can click on the Start machine button i.e. the big Green Arrow pointing to the right.
<img width="959" height="539" alt="Lab-1 8" src="https://github.com/user-attachments/assets/bd932174-4f17-45de-8994-9f755ec2f445" />

4. It should show that the machine is running and then we wait for the machine to boot up.
<img width="959" height="539" alt="Lab-1 9" src="https://github.com/user-attachments/assets/36c2280f-da78-4884-944d-f99c223d4c57" />

5. After booting up, Another window appears with our Kali Linux machine intializing and then we are shown the login screen.
<img width="845" height="539" alt="Lab-1 10" src="https://github.com/user-attachments/assets/ef5eaab4-f7a1-4c58-b413-4b1c97acdd72" />

6. The default Username and Password to our VM is "kali". Enter those credentials in.
<img width="840" height="540" alt="Lab-1 11" src="https://github.com/user-attachments/assets/6938cbc0-c29a-4934-99a5-18046c45b8d6" />

7. And then you should be logged in! Kali Linux comes preloaded with all the hacking tools, so its not necessary for you to download them seperately.
<img width="892" height="540" alt="Lab-1 x" src="https://github.com/user-attachments/assets/1e75e0f1-3651-48b1-9182-96186354e162" />

8. Take your time exploring and customizing your new Kali Linux VM. The tools are all listed out when you click on the Kali button on the top left of your screen.
<img width="647" height="470" alt="Lab-1 12" src="https://github.com/user-attachments/assets/6b05d788-8a87-4e1b-bb69-165cf95f094c" />

If at all you faced any problems at any step of this setup guide/walkthrough, don't be shy to google your problem and straighten it out.  
Googling is also a very important skill to have. 
Be curious, explore and try things out because that is the way to learn. 

-Syed Abdul Rauf, 2026



















