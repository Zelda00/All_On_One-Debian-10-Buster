#!/usr/bin/env python3

import os, sys, traceback
if os.getuid() != 0:
	print ("\033[1;33m   OOPS !! This Script Needs (sudo) Or (su) Privledges To Ronning It, Thank You")
	sys.exit()
def main():
	try:
		print ('''
\033[1;36m############################################################################
\033[1;m     please visite https://www.debian.org/index.en.html for more help\033[1;36m 
\033[1;36m############################################################################
''')
		def inicio1():
			while True:
				print ('''
\033[1;33m[1] \033[1;37mRestore Your Debian Buster Repositories & Refresh Repo
\033[1;33m[2] \033[1;37mView Categories ...
\033[1;33m[3] \033[1;37mEnable 32bit Architecture: 386i
    (required for installtion 32 bit packages such as Steam) 
\033[1;33m[4] \033[1;37mDebian Support (Access Web.Page Tex.Mode Only). To exit type: q
\033[1;33m[5] \033[1;37mMigration Full Upgrade To new Debian Release 
              \033[1;37m"add code name "?" after running this operation at commande line"
			''')
				opcion0 = raw_input("\033[1;36mkat > \033[1;m")			
				while opcion0 == "1":
					print ('''
\033[1;33m[1] \033[1;37mAdd Debian linux repositories
\033[1;33m[2] \033[1;37mUpdate Repo
\033[1;33m[3] \033[1;37mRemove all Debian linux repositories
\033[1;33m[4] \033[1;37mAdd the Mono repository to your system (dev repositorie)
					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("echo deb http://deb.debian.org/debian buster main contrib non-free main contrib non-free >> /etc/apt/sources.list")
						cmd2 = os.system("echo deb-src http://deb.debian.org/debian buster main contrib non-free >> /etc/apt/sources.list")
					        cmd3 = os.system("echo deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free >> /etc/apt/sources.list")
                                                cmd4 = os.system("echo deb-src http://deb.debian.org/debian-security/ buster/updates main contrib non-free >> /etc/apt/sources.list")
                                                cmd5 = os.system("echo deb http://deb.debian.org/debian buster-updates main contrib non-free >> /etc/apt/sources.list")
                                                cmd6 = os.system("echo deb-src http://deb.debian.org/debian buster-updates main contrib non-free >> /etc/apt/sources.list")
#BackPort Repo
                                                cmd7 = os.system("echo deb http://deb.debian.org/debian buster-backports >> /etc/apt/sources.list")
                                                cmd8 = os.system("echo deb-src http://deb.debian.org/debian buster-backports main contrib non-free >> /etc/apt/sources.list")
                                        elif repo == "2":
						cmd3 = os.system("apt update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"
						delete_list = ["deb http://deb.debian.org/debian buster main contrib non-free"]
						delete_list = ["deb-src http://deb.debian.org/debian buster main contrib non-free"]
						delete_list = ["deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free"]
						delete_list = ["deb-src http://deb.debian.org/debian-security/ buster/updates main contrib non-free"]
						delete_list = ["deb http://deb.debian.org/debian buster-updates main contrib non-free"]
						delete_list = ["deb-src http://deb.debian.org/debian buster-updates main contrib non-free"]
						delete_list = ["deb http://deb.debian.org/debian buster-backports main contrib non-free"]
						delete_list = ["deb-src http://deb.debian.org/debian buster-backports main contrib non-free"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll Debian linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "go home":
						inicio1()
					elif repo == "4":
                                                repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
						file = open('/etc/apt/sources.list', 'r')
						print (file.read())
                                                cmd1 = os.system("apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF")
                                                cmd2 = os.system("echo '# Mono-Dev repositories | Added by GoldFish\ndeb https://download.mono-project.com/repo/debian stable-buster main >> /etc/apt/sources.list.d/mono-official-stable.list")
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
				if opcion0 == "3":
					print ('''\\\\\\\\ Architecture i386 ////''')
					repo = raw_input("\033[1;32mDo you want to enable architecture i386 ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("dpkg --add-architecture i386")
						cmd2 = os.system("apt update")
				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to access to debian support? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt install links2 -y && clear && links2 https://www.debian.org/support")
				elif opcion0 == "5":
 						cmd1 = os.system("cp /etc/apt/sources.list /etc/apt/sources.list_backup && sed -i 's/old-releaase-name/new-release-name/g' /etc/apt/sources.list && apt update && clear && apt -y uprade && clear && apt dist-upgrade && apt autoclean && cat /etc/os-release")
				def inicio():
					while opcion0 == "2":
						print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m
\033[1;33m[1] \033[1;37mDebian Packages (SoftWare)	         
\033[1;33m[2] \033[1;37mDependencies			   				  
\033[1;33m[3] \033[1;37mFix Issue 
\033[1;33m[4] \033[1;37mBasic System & Hardware Information
									
\033[1;35m[*] Select Back
			 ''')
						print ("\033[1;32mSelect a category number or press (back) to return to menu.\n\033[1;m")
						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "go home":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("exit")
						while opcion1 == "1":
							print ('''
\033[1;36m=+[Debian Packages\033[1;m
\033[1;33m[1] \033[1;37mcmake				\033[1;33m[30] \033[1;37mlinks2
\033[1;33m[2] \033[1;37mgparted				\033[1;33m[31] \033[1;37mmake 
\033[1;33m[3] \033[1;37mgit			                         \033[1;33m[32] \033[1;37minkscape 
\033[1;33m[4] \033[1;37mgdebi				\033[1;33m[33] \033[1;37mflatpak 
\033[1;33m[5] \033[1;37mmousepad			                 \033[1;33m[34] \033[1;37mbash-completion 
\033[1;33m[6] \033[1;37mgedit				\033[1;33m[35] \033[1;37mnmap
\033[1;33m[7] \033[1;37mffmpeg 				\033[1;33m[36] \033[1;37mhtop
\033[1;33m[8] \033[1;37mffmpeg:i386			\033[1;33m[37] \033[1;37mgvfs-backends (andro-device detect) 
\033[1;33m[9]\033[1;37mputty  	                        \033[1;33m[38] \033[1;37mpython3-pip 
\033[1;33m[10] \033[1;37mlibdvdcss2    		       	\033[1;33m[39] \033[1;37msquashfs-tools  
\033[1;33m[11] \033[1;37m\033[1;37mlibdvd-pkg 	        \033[1;33m[40] \033[1;37mp7zip-full 
\033[1;33m[12] \033[1;37mffmpegthumbnailer 		\033[1;33m[41] \033[1;37mpotential dependency 
\033[1;33m[13] \033[1;37mgstreamer1.0-plugins-ugly      \033[1;33m[42  \033[1;37minstall all debian packages  
\033[1;33m[14] \033[1;37mgstreamer1.0-libav 		\033[1;33m[43] \033[1;37mbashtop 
\033[1;33m[15] \033[1;37mtumbler-plugins-extra 			 
\033[1;33m[16] \033[1;37mfirmware-linux 				 
\033[1;33m[17] \033[1;37mfirmware-linux-nonfree 			 
\033[1;33m[18] \033[1;37mintel-microcode 				 
\033[1;33m[20] \033[1;37munrar 					 
\033[1;33m[21] \033[1;37mfile-roller 				  
\033[1;33m[22] \033[1;37mbroadcom packages 				 
\033[1;33m[23] \033[1;37mgufw 					  
\033[1;33m[24] \033[1;37mbleachbit 					    
\033[1;33m[25] \033[1;37mbluetooth
\033[1;33m[26] \033[1;37mjava default-jre				  
\033[1;33m[27] \033[1;37mlsscsi				          
\033[1;33m[28] \033[1;37mwget   				          
\033[1;33m[29] \033[1;37myoutube-dl 					   
 
\033[1;35m[*] Back 				 
						''')
							print ("\033[1;32mInsert the number of the package to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install -y cmake && apt autoclean")
							elif opcion2 == "2":
								cmd = os.system("apt install -y gparted && apt autoclean")
                                                        elif opcion2 == "3":
								cmd = os.system("apt install -y git && apt autoclean")
							elif opcion2 == "4":
								cmd = os.system("apt install -y gdebi && apt autoclean")
							elif opcion2 == "5":
								cmd = os.system("apt install mousepad -y && apt autoclean")
							elif opcion2 == "6":
								cmd = os.system("apt install gedit -y && apt autoclean")
							elif opcion2 == "7":
								cmd = os.system("apt install ffmpeg -y && apt autoclean")
							elif opcion2 == "8":
								cmd = os.system("apt install ffmpeg:i386 -y && apt autoclean")
							elif opcion2 == "9":
								cmd = os.system("apt install putty -y && apt autoclean")
							elif opcion2 == "10":
								cmd = os.system("apt install libdvdcss2 -y && apt autoclean")
							elif opcion2 == "11":
								cmd = os.system("apt install libdvd-pkg -y && apt autoclean")
							elif opcion2 == "12":
								cmd = os.system("apt install ffmpegthumbnailer -y && apt autoclean")
							elif opcion2 == "13":
								cmd = os.system("apt install gstreamer1.0-plugins-ugly -y && apt autoclean")
							elif opcion2 == "14":
								cmd = os.system("apt install gstreamer1.0-libav -y && apt autoclean")
							elif opcion2 == "15":
								cmd = os.system("apt install tumbler-plugins-extra -y && apt autoclean")
							elif opcion2 == "16":
								cmd = os.system("apt install firmware-linux -y && apt autoclean")
							elif opcion2 == "17":
								cmd = os.system("apt install firmware-linux-nonfree -y && apt autoclean")
							elif opcion2 == "18":
								cmd = os.system("apt install intel-microcode -y && apt autoclean")
							elif opcion2 == "19":
								cmd = os.system("apt install rar -y && apt autoclean")
							elif opcion2 == "20":
								cmd = os.system("apt install -y unrar -y && apt autoclean")
							elif opcion2 == "21":
								cmd = os.system("apt install file-roller -y && apt autoclean")
							elif opcion2 == "22":
								cmd = os.system("apt install broadcom-sta-dkms broadcom-sta-common firmware-brcm80211 -y && apt autoclean")
							elif opcion2 == "23":
								cmd = os.system("apt install gufw -y && apt autoclean")
							elif opcion2 == "24":
								cmd = os.system("apt install bleachbit -y && apt autoclean")
							elif opcion2 == "25":
								cmd = os.system("apt install bluetooth blueman bluez-firmware bluez-cups bluez-tools -y && apt autoclean")
							elif opcion2 == "26":
								cmd = os.system("apt update && apt install default-jre -y && apt autoclean")
							elif opcion2 == "27":
								cmd = os.system("apt install -y lsscsi && apt autoclean")
							elif opcion2 == "28":
								cmd = os.system("apt install -y wget && apt autoclean")
							elif opcion2 == "29":
								cmd = os.system("apt install youtube-dl -y && apt autoclean")
							elif opcion2 == "30":
								cmd = os.system("apt install links2 -y && apt autoclean")
							elif opcion2 == "31":
								cmd = os.system("apt install make -y && apt autoclean")
							elif opcion2 == "32":
								cmd = os.system("apt install inkscape -y && apt autoclean")
							elif opcion2 == "33":
								cmd = os.system("apt install flatpak -y && apt autoclean")
							elif opcion2 == "34":
								cmd = os.system("apt install -y bash-completion && apt autoclean")
							elif opcion2 == "35":
								cmd = os.system("apt install nmap -y && apt autoclean")
							elif opcion2 == "36":
                                                                cmd = os.system("apt install htop -y && apt autoclean")
							elif opcion2 == "37":
								cmd = os.system("apt install -y gvfs-backends && apt autoclean")
							elif opcion2 == "38":
								cmd = os.system("apt install -y python3-pip && apt autoclean")
							elif opcion2 == "39":
								cmd = os.system("apt install squashfs-tools -y && apt autoclean")
							elif opcion2 == "40":
								cmd = os.system("apt install p7zip-full -y && apt autoclean")
							elif opcion2 == "41":
								cmd = os.system("apt install -y unrar rar libncurses-dev flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf && apt autoclean")
							elif opcion2 == "42":
                                                                cmd = os.system("apt update && apt install putty git gdebi cmake gparted gedit ffmpeg ffmpeg:i386 libdvdcss2 libdvd-pkg ffmpegthumbnailer gstreamer1.0-libav gstreamer1.0-plugins-ugly tumbler-plugins-extra firmware-linux firmware-linux-nonfree intel-microcode gufw file-roller broadcom-sta-dkms broadcom-sta-common firmware-brcm80211 inkscape make cmake lsscsi bleachbit bluetooth blueman bluez-firmware libncurses-dev flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf bluez-cups bluez-tools default-jre wget youtube-dl links2 p7zip-full squashfs-tools python3-pip gvfs-backends htop nmap bash-completion flatpak && apt autoclean -y && apt autoclean")
                                                        elif opcion2 == "43":
                                                                cmd = os.system("echo '# Debian linux repositories | Added by GoldFish\ndeb http://ftp.fr.debian.org/debian/ buster main >> /etc/apt/sources.list && apt update && apt install -y python3-psutil bashtop && apt autoclean && bashtop") 
                                                        elif opcion2 == "back":
								inicio()
							elif opcion2 == "go home":
								inicio1()   
							elif opcion2 == "0":
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "2":
							print ('''
\033[1;36m=+[Dependencies\033[1;m

 \033[1;33m[1] \033[1;37mninja-build 			\033[1;33m[36] \033[1;37mlibnspr4
 \033[1;33m[2] \033[1;37mpython3-pip 		        \033[1;33m[37] \033[1;37mlibpango-1.0-0
 \033[1;33m[3] \033[1;37mpython3-setuptools 		        \033[1;33m[38] \033[1;37mlibpangocairo-1.0-0
 \033[1;33m[4] \033[1;37mmeson 		                \033[1;33m[39] \033[1;37mlibstdc++6
 \033[1;33m[5] \033[1;37mvalac 				\033[1;33m[40] \033[1;37mlibx11-6
 \033[1;33m[6] \033[1;37mdebhelper 				\033[1;33m[41] \033[1;37mlibx11-xcb1
 \033[1;33m[7] \033[1;37mlibcairo2-dev 			\033[1;33m[42] \033[1;37mlibxcb1
 \033[1;33m[8] \033[1;37mlibgranite-dev 			\033[1;33m[43] \033[1;37mlibxcomposite1
 \033[1;33m[9] \033[1;37mlibgtk-3-dev 		        \033[1;33m[44] \033[1;37mlibxcursor1
\033[1;33m[10) \033[1;37mlibxml2-dev 			\033[1;33m[45] \033[1;37mlibxdamage1
\033[1;33m[11) \033[1;37mlibgee-0.8-dev 			\033[1;33m[46] \033[1;37mlibxext6                   
\033[1;33m[12) \033[1;37mlibarchive-dev      	        \033[1;33m[47] \033[1;37mlibxfixes3
\033[1;33m[13) \033[1;37mlibgtksourceview-3.0-dev 		\033[1;33m[30] \033[1;37mlibfontconfig1                   
\033[1;33m[14) \033[1;37mlibmarkdown2-dev 			\033[1;33m[31] \033[1;37mlibgcc1                          
\033[1;33m[15) \033[1;37mlibssl-dev 				\033[1;33m[32] \033[1;37mlibgconf-2-4                     
\033[1;33m[16) \033[1;37mgconf-service 		        \033[1;33m[33] \033[1;37mlibgdk-pixbuf2.0-0              
\033[1;33m[17) \033[1;37mlibasound2 				\033[1;33m[34] \033[1;37mlibglib2.0-0                     
\033[1;33m[18) \033[1;37mlibatk1.0-0 libc6			\033[1;33m[35] \033[1;37mlibgtk-3-0                      
\033[1;33m[19) \033[1;37mlibcairo2                           \033[1;33m[48] \033[1;37mlibxi6  
\033[1;33m[20) \033[1;37mlibcups2                            \033[1;33m[49] \033[1;37mlibxrandr2
\033[1;33m[21) \033[1;37mlibdbus-1-3                         \033[1;33m[50] \033[1;37mlibxrender1 
\033[1;33m[22) \033[1;37mlibexpat1                           \033[1;33m[51] \033[1;37mlibxss1
\033[1;33m[23) \033[1;37mlibfontconfig1                      \033[1;33m[52] \033[1;37mlibxtst6
\033[1;33m[24) \033[1;37mlibgcc1                             \033[1;33m[53] \033[1;37mca-certificates 
\033[1;33m[25) \033[1;37mlibgconf-2-4                        \033[1;33m[54] \033[1;37mfonts-liberation 
\033[1;33m[26) \033[1;37mlibgdk-pixbuf2.0-0                  \033[1;33m[55] \033[1;37mlibappindicator1
\033[1;33m[27) \033[1;37mlibnspr4                            \033[1;33m[56] \033[1;37mlibnss3
\033[1;33m[28) \033[1;37mlibglib2.0-0                        \033[1;33m[57] \033[1;37mlsb-release
\033[1;33m[29] \033[1;37mlibgtk-3-0                          \033[1;33m[58] \033[1;37mxdg-utils
                                          
\033[1;35m0) Install all Dependencies				 
						''')
							print ("\033[1;32mInsert the number of the package to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install ninja-build -y && apt autoclean")
							elif opcion2 == "2":
								cmd = os.system("apt install python3-pip -y && apt autoclean")
							elif opcion2 == "3":
								cmd = os.system("apt install python3-setuptools -y && apt autoclean")
							elif opcion2 == "4":
								cmd = os.system("apt install meson -y && apt autoclean")
							elif opcion2 == "5":
								cmd = os.system("apt install valac -y && apt autoclean")
							elif opcion2 == "6":
								cmd = os.system("apt install debhelper -y && apt autoclean")
							elif opcion2 == "7":
								cmd = os.system("apt install libcairo2-dev -y && apt autoclean")
							elif opcion2 == "8":
								cmd = os.system("apt install libgranite-dev -y && apt autoclean")
							elif opcion2 == "9":
								cmd = os.system("apt install libgtk-3-dev -y && apt autoclean")
							elif opcion2 == "10":
								cmd = os.system("apt install libxml2-dev -y && apt autoclean")
							elif opcion2 == "11":
								cmd = os.system("apt install libgee-0.8-dev -y && apt autoclean")
							elif opcion2 == "12":
								cmd = os.system("apt install libarchive-dev -y && apt autoclean")
							elif opcion2 == "13":
								cmd = os.system("apt install libgtksourceview-3.0-dev -y && apt autoclean")
							elif opcion2 == "14":
								cmd = os.system("apt install libmarkdown2-dev -y && apt autoclean")
							elif opcion2 == "15":
								 cmd = os.system("apt install libssl-dev -y && apt autoclean")
							elif opcion2 == "16":
								cmd = os.system("apt install gconf-service -y && apt autoclean")
							elif opcion2 == "17":
								cmd = os.system("apt install libasound2 -y && apt autoclean")
							elif opcion2 == "18":
								cmd = os.system("apt install libatk1.0-0 libc6 -y && apt autoclean")
							elif opcion2 == "19":
								cmd = os.system("apt install libcairo2 -y && apt autoclean")
							elif opcion2 == "20":
								cmd = os.system("apt install libcups2 -y && apt autoclean")
							elif opcion2 == "21":
								cmd = os.system("apt install libdbus-1-3 -y && apt autoclean")
							elif opcion2 == "22":
								cmd = os.system("apt install libexpat1 -y && apt autoclean")
							elif opcion2 == "23":
								cmd = os.system("apt install libfontconfig1 -y && apt autoclean")
							elif opcion2 == "24":
								cmd = os.system("apt install libgcc1 -y && apt autoclean")
							elif opcion2 == "25":
								cmd = os.system("apt install libgconf-2-4 -y && apt autoclean")
							elif opcion2 == "26":
								cmd = os.system("apt install libgdk-pixbuf2.0-0 -y && apt autoclean")
							elif opcion2 == "27":
								cmd = os.system("apt install libnspr4 -y && apt autoclean")
							elif opcion2 == "28":
								cmd = os.system("apt install libglib2.0-0 -y && apt autoclean")
							elif opcion2 == "29":
								cmd = os.system("apt install libgtk-3-0 -y && apt autoclean")
							elif opcion2 == "30":
								cmd = os.system("apt install libfontconfig1 -y && apt autoclean")
							elif opcion2 == "31":
								cmd = os.system("apt install libgcc1 -y && apt autoclean")
							elif opcion2 == "32":
								cmd = os.system("apt install libgconf-2-4 -y && apt autoclean")
							elif opcion2 == "33":
								cmd = os.system("apt install libgdk-pixbuf2.0-0 -y && apt autoclean")
							elif opcion2 == "34":
								cmd = os.system("apt install libglib2.0-0 -y && apt autoclean")
							elif opcion2 == "35":
								cmd = os.system("apt install libgtk-3-0 -y && apt autoclean")
                                                        elif opcion2 == "36": 
                                                                cmd = os.system("lapt install libnspr4 -y && apt autoclean")
                                                        elif opcion2 == "37":
                                                                cmd = os.system("apt install libpango-1.0-0 -y && apt autoclean")
                                                        elif opcion2 == "38":
                                                                cmd = os.system("apt install libpangocairo-1.0-0 -y && apt autoclean") 
                                                        elif opcion2 == "39":
                                                                cmd = os.system("apt install libstdc++6 -y && apt autoclean")
                                                        elif opcion2 == "40":
                                                                cmd = os.system("apt install libx11-6 -y && apt autoclean")
                                                        elif opcion2 == "41":
                                                                cmd = os.system("apt install libx11-xcb1 -y && apt autoclean") 
                                                        elif opcion2 == "42":
                                                                cmd = os.system("apt install libxcb1 -y && apt autoclean")
                                                        elif opcion2 == "43":
                                                                cmd = os.system("apt install libxcomposite1 -y && apt autoclean")
                                                        elif opcion2 == "44":
                                                                cmd = os.system("apt install libxcursor1 -y && apt autoclean")
                                                        elif opcion2 == "45":
                                                                cmd = os.system("apt install libxdamage1 -y && apt autoclean")
                                                        elif opcion2 == "46":
                                                                cmd = os.system("apt install libxext6 -y && apt autoclean")
                                                        elif opcion2 == "47":
                                                                cmd = os.system("apt install libxfixes3 -y && apt autoclean")
                                                        elif opcion2 == "48":
                                                                cmd = os.system("apt install libxi6 -y && apt autoclean")
                                                        elif opcion2 == "49":
                                                                cmd = os.system("apt install libxrandr2 -y && apt autoclean")
                                                        elif opcion2 == "50":
                                                                cmd = os.system("apt install libxrender1 -y && apt autoclean")
                                                        elif opcion2 == "51":
                                                                cmd = os.system("apt install libxss1 -y && apt autoclean")
                                                        elif opcion2 == "52":
                                                                cmd = os.system("apt install libxtst6 -y && apt autoclean")
                                                        elif opcion2 == "53":
                                                                cmd = os.system("apt install ca-certificates -y && apt autoclean")
                                                        elif opcion2 == "54":
                                                                cmd = os.system("apt install fonts-liberation -y && apt autoclean")
                                                        elif opcion2 == "55":
                                                                cmd = os.system("apt install libappindicator1 -y && apt autoclean")
                                                        elif opcion2 == "56":
                                                                cmd = os.system("apt install libnss3 -y && apt autoclean")
                                                        elif opcion2 == "57":
                                                                cmd = os.system("apt install lsb-release -y && apt autoclean")
                                                        elif opcion2 == "58":
                                                                cmd = os.system("apt install xdg-utils -y && apt autoclean")
 							elif opcion2 == "back":
								inicio()
							elif opcion2 == "go home":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt install ninja-build python3-pip python3-setuptools meson valac debhelper libcairo2-dev libgranite-dev libgtk-3-dev libxml2-dev libgee-0.8-dev libarchive-dev libgtksourceview-3.0-dev libmarkdown2-dev libssl-dev gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 | libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils libx11-xcb1 -y && apt autoclean")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "3" :
							print ('''
\033[1;36m=+[Fix Issues ...\033[1;m
\033[1;33m[1] \033[1;37mFix Missing Mouse & Keyboard
\033[1;33m[2] \033[1;37mSandBox Simplenote (chrome-sandbox), use one of 
    \033[1;37mgive permission to fix that (4755,root:root,755 -R) 
\033[1;33m[3] \033[1;37mFix Garebled Screen, (graphics card AMD) XFCE,LXDE,LXQT,...
    \033[1;37madd codes at startup & reboot system 
\033[1;33m[4] \033[1;37mFix Screen Tering "(Nvidia)" Issues XFCE,LXDE,LXQT,...
    \033[1;37madd codes at startup & reboot system
\033[1;35m[0] Back Man Menu				 
						''')
							print ("\033[1;32mSelect the number .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
							        cmd = os.system("apt update && apt install -y xserver-xorg-input-all && reboot")
							elif opcion2 == "2":
								cmd = os.system("chmod 4755 /opt/Simplenote/chrome-sandbox") 
							elif opcion2 == "3":
								print ('''
\033[33m***************************************************************************************************** 
\033[33m* \033[1;36m################################################################################################# \033[33m*
\033[33m* #\033[1;m glx-AMD.txt && echo xfconf-query -c xfwm4 -p /general/vblank_mode -t string -s 'glx' --create\033[1;36m # \033[33m*
\033[33m* \033[1;36m################################################################################################# \033[33m*
\033[33m*****************************************************************************************************
''')
							elif opcion2 == "4":
                                                                print ('''
\033[33m****************************************************************************************************************
\033[33m* \033[1;36m############################################################################################################ \033[33m*
\033[33m* #\033[1;m nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"\033[1;36m # \033[33m*
\033[33m* \033[1;36m############################################################################################################ \033[33m*
\033[33m****************************************************************************************************************
''')
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "go home":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4" :
							print ('''
\033[1;36m=+[Displaying Basic System & Hardware Information\033[1;m
\033[1;33m[1] \033[1;37mRelease
\033[1;33m[2] \033[1;37mDisplaying All Information of Uname
\033[1;33m[3] \033[1;37mDisk info
\033[1;33m[4] \033[1;37muniversal serial bus (usb) info
\033[1;33m[5] \033[1;37mHost Name Control	
\033[1;33m[6] \033[1;37mIp Address
\033[1;33m[7] \033[1;37mLinux Kernel Name
\033[1;33m[8] \033[1;37mLinux Kernel Release
\033[1;33m[9] \033[1;37mLinux Kernel Version
\033[1;33m[10] \033[1;37mnodename host
\033[1;33m[11] \033[1;37mMachine Hardware Architecture (i386,x86_64,etc.)
\033[1;33m[12] \033[1;37mProcessor Type
\033[1;33m[13] \033[1;37mHardware Platform
\033[1;33m[14] \033[1;37mOperating System information
\033[1;33m[15] \033[1;37mDetailed Hardware Information
\033[1;33m[16] \033[1;37mCPU Information 
\033[1;33m[17] \033[1;37mBlock Device Information
\033[1;33m[18] \033[1;37mInformation About Other Devices PCI & SCSI 
\033[1;33m[19] \033[1;37mShow Ship Network Devive

\033[1;35m[0] Back Man Menu 
						''')
							print ("\033[1;32mchoose a number to show the result, or [back] to return to man menu.\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("cat /etc/*-release ")
							elif opcion2 == "2":
								cmd = os.system("uname -a")
							elif opcion2 == "3":
								cmd = os.system("fdisk -l")
							elif opcion2 == "4":
								cmd = os.system("lsusb")
							elif opcion2 == "5":
								cmd = os.system("hostnamectl")
							elif opcion2 == "6":
								cmd = os.system("ip link")
                                                        elif opcion2 == "7":
								cmd = os.system("uname -s")
                                                        elif opcion2 == "8":
								cmd = os.system("uname -r")
                                                        elif opcion2 == "9":
								cmd = os.system("uname -v")
                                                        elif opcion2 == "10":
								cmd = os.system("uname --nodename")
                                                        elif opcion2 == "11":
								cmd = os.system("uname --m")
                                                        elif opcion2 == "12":
                                                                cmd = os.system("uname -p")
                                                        elif opcion2 == "13":
                                                                cmd = os.system("uname -i")
                                                        elif opcion2 == "14":
                                                                cmd = os.system("uname -o")
                                                        elif opcion2 == "15":
                                                                cmd = os.system("lshw -short")
                                                        elif opcion2 == "16":
                                                                cmd = os.system("lscpu")   
                                                        elif opcion2 == "17":
                                                                cmd = os.system("lsblk -a")  
                                                        elif opcion2 == "18":
                                                                cmd = os.system("lspci && lsscsi")  
                                                        elif opcion2 == "19":
                                                                cmd = os.system("lspci | grep Network")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "go home":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "5":
							print ('''
\033[1;36m=+[Devlopment tools \033[1;m
\033[1;33m[1] \033[1;37mOder Mono Dev-Tools Mono
\033[1;33m[2] \033[1;37mMono-dev
\033[1;35m[0] back 
				''')
							print ("\033[1;32mComment...!!!.\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install apt-transport-https dirmngr gnupg ca-certificates && clear")
							elif opcion2 == "2":
								cmd = os.system("apt update && apt install -y mono-devel && clear")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "go home":
								inicio1()
				inicio()
		inicio1()
	except KeyboardInterrupt:
		print (" \033[1;45mClean Your Apt Cache & Reboot Your PC, Thank You\033[1;m")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)
if __name__ == "__main__":
    main() 
