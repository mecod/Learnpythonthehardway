#$language = "Python"
#$interface = "1.0"

# AutoResponder.py
#
# Description:
#	Demonstrates how to set up a list of commands/text that get sent to the
#	remote as soon as a corresponding "trigger" string/text is detected from
#	the remote system. 
#	Once launched, this script will run indefinitely until the session is
#	disconnected or the application is closed.  To stop the script, choose
#	"Cancel" from SecureCRT's main "Script" menu.
#
# Demonstrates:
# - How to use the Session.Connected property to determine if the current
#   tab has an active connection.
# - How to wait for one of multiple string values to appear, and detect
#   which one was found using the Screen.WaitForStrings method.
#
def Response_cr():
    crt.Screen.Send("\r")
	
def Response_enable():
    crt.Screen.Send("enable\r")
	
def Response_debug_sup():
    crt.Screen.Send("debug support\r")
	
def Response_factory():
    crt.Screen.Send("facotry\r")
	
def Response_fac_menu_1():
    crt.Screen.Send("1")
	
def Response_fac_menu_2():
    crt.Screen.Send("f")

def Response_fac_power():
    crt.Screen.Send("\0x1B")
	
response = {
    1: Response_cr(),
    2: Response_enable(),
    3: Response_debug_sup(),
    4: Response_factory(),
    5: Response_fac_menu_1(),
    6: Response_fac_menu_2(),
    7: Response_fac_power(),
}

def Main():
	tab = crt.GetScriptTab()

	if tab.Session.Connected != True:
		crt.Dialog.MessageBox(
			"Error.\n" +
			"This script was designed to be launched after a valid "+
			"connection is established.\n\n"+
			"Please connect to a remote machine before running this script.")
		return

	# Ensure that we don't "miss" data coming from the remote by setting
	# our Screen's Synchronous flag to true.
	tab.Screen.Synchronous = True

	while True:
		# WaitForStrings as called here will wait for an occurence of one
		# of the strings that is part of the g_vWaitFors array defined
		# above.  When one of the strings is detected, the index of the
		# string withint the array will be returned as the value of the
		# nIndex variable.  Note that nIndex will be 1-based, rather than
		# 0-based.
		nIndex = tab.Screen.WaitForStrings(g_vWaitFors)
		


		# Now that we've discovered text in the "nIndex"th item of our array,
		# send the "nIndex"th item of the g_vRespondWiths array:
		# tab.Screen.Send(g_vRespondWiths[nIndex] + "\n")

		# Now that we've sent the corresponding command, loop back up to the
		# top and wait again for another trigger string to appear...


g_vWaitFors = [
	"%SYS-5-COLDSTART: System coldstart.",
	"Ruijie>",
	"Ruijie#",
	"Ruijie(support)#",
	"生产测试程序一级菜单",
	"生产测试模式",
	"电源测试",
	"Waiting for 8",
	"Waiting for 9",
	"Waiting for 10"]

g_vRespondWiths = [
	"en",
	"Command 2",
	"Command 3",
	"Command 4",
	"Command 5",
	"Command 6",
	"Command 7",
	"Command 8",
	"Command 9",
	"Command 10"]
	
Main()

