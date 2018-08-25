##ToDo: maka an implementation
#The word in capital letters after (II) is the name of the driver in use
#/var/log/Xorg.0.log

"""
Markers: (--) probed, (**) from config file, (==) default setting,
	(++) from command line, (!!) notice, (II) informational,
	(WW) warning, (EE) error, (NI) not implemented, (??) unknown.
"""

"""
fix for "fonts.dir not found":
cd <path>
mkfontdir
"""

"""
] (WW) The directory "/usr/share/fonts/OTF" does not exist.
[    17.943] 	Entry deleted from font path.
[    17.943] "(WW) The directory "/usr/share/fonts/Type1" does not exist."
[    17.943] 	Entry deleted from font path.

mkdir /usr/share/fonts/OTF
mkfontdir /usr/share/fonts/OTF
"""

"""
ToDo: research how to fix the below warning:
(WW) Open ACPI failed (/var/run/acpid.socket) (No such file or directory)
"""

"""
ToDo: research how to fix the below warning:
[    29.939] (II) LoadModule: "intel"
[    29.939] (WW) Warning, couldn't open module intel
"""

"""
[    29.943] (II) LoadModule: "fbdev"
[    29.943] (WW) Warning, couldn't open module fbdev
[    29.943] (EE) Failed to load module "fbdev" (module does not exist, 0)
"""
