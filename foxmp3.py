
"""
Name: mp3fox
Author: Madf0x
Version: 1
Date: 10/8/2010
Note: sourceforge hosting by ichib0d
Desc:
mp3fox rips audio(think songs :) ) from flash files found in 
firefox's cache. It does this by acting as a wrapper for 
ffmpeg(so install that to run this). It operates on the first found 
firefox profile in /home/(username)/.mozilla/firefox/
If someone who knows a better way of directly ripping audio from .flv 
files lets me know I may try to implement it so ffmpeg isn't relied on. 
"""

import os
import pwd
import commands

#get the user name for path finding
user = pwd.getpwuid(os.getuid())[0]

#construct paths for music and the firefox cache
path = '/home/' + user + '/.mozilla/firefox/'
end_path = '/home/' + user + '/Music/'
profile = os.listdir(path)
path = path + profile[2] + '/Cache/'
cache_list = os.listdir(path)

#for naming later
counter = 0
for num in range(len(cache_list)):
    #check filetypes with the file utility
    chkedfile = commands.getoutput('file ' + path + cache_list[num])
    splitfile = chkedfile.split(' ')
    """hack here! flash vids file type starts with  Macromedia, so we check for that to cover multiple flash file types, theres probably a better way"""
    if splitfile[1] == 'Macromedia':
        counter += 1
        #do the hard work of audio conversion.
        cmd = 'ffmpeg -i ' + path + cache_list[num] + ' -ab 128 -ar 44100 ' + end_path + 'song' + str(counter) + '.mp3'       
        commands.getoutput(cmd)
    else:        
        pass


