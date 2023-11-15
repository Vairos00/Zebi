os.system('git pull')
# exit(' Wait Tool On updating ')
zebi=platform.architecture()[0]
if zebi=="32bit":__import__("zebi32")
elif zebi=="64bit":__import__("zebi64")