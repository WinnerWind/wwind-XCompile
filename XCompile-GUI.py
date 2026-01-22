#!/usr/bin/python3
import sys
import subprocess
import os

SPLASH = r"""
 __    __   ______                                     __  __           
/  |  /  | /      \                                   /  |/  |          
$$ |  $$ |/$$$$$$  |  ______   _____  ____    ______  $$/ $$ |  ______  
$$  \/$$/ $$ |  $$/  /      \ /     \/    \  /      \ /  |$$ | /      \ 
 $$  $$<  $$ |      /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |$$ |$$ |/$$$$$$  |
  $$$$  \ $$ |   __ $$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$ |$$    $$ |
 $$ /$$  |$$ \__/  |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$ |$$ |$$$$$$$$/ 
$$ |  $$ |$$    $$/ $$    $$/ $$ | $$ | $$ |$$    $$/ $$ |$$ |$$       |
$$/   $$/  $$$$$$/   $$$$$$/  $$/  $$/  $$/ $$$$$$$/  $$/ $$/  $$$$$$$/ 
                                            $$ |                        
                                            $$ |                        
                                            $$/                         

   ___                       ____      _      ___                  _      ___         __
  / _ \___ ______ _  ___    / __/___  | | /| / (_)__  ___  ___ ___| | /| / (_)__  ___/ /
 / , _/ -_) __/  ' \/ _ \   > _/_ _/  | |/ |/ / / _ \/ _ \/ -_) __/ |/ |/ / / _ \/ _  / 
/_/|_|\__/\__/_/_/_/\___/  |_____/    |__/|__/_/_//_/_//_/\__/_/  |__/|__/_/_//_/\_,_/  

"""

def yn_prompt(text):
	output = input(text +" [y/n]: ")
	return (output.lower() == "y" or output.lower() == "yes")


print(SPLASH)

include_global_compose = yn_prompt("Include the global compose file bundled with your system?")
overwrite_compose = yn_prompt("Overwrite your compose file? (NO UNDO!)")
set_bindings = yn_prompt("Apply your new bindings? (May not work in Wayland based DEs)")

command = "cat Bindings/* | ./XCompile.py " + \
		("--include-global-compose" if include_global_compose else "") + " > " + \
		("~/.XCompose" if overwrite_compose else "compose.txt") + \
		(" && setxkbmap" if set_bindings else "")

print("---------------")
print("Will run")
print(">>> "+command)
print("")
print("The following files will be compiled")
print(os.listdir("Bindings/"))
if not yn_prompt("Proceed?"):
	print("Aborted.")
	sys.exit(1)

subprocess.run(command, shell=True)
print("Done! Thanks for using XCompose!")

sys.exit(0)

