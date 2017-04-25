I've recently set up a home server running Linux and wanted to give an overview of the setup and some pitfalls that I fell down that can be avoided. First of all I couldn't have done it without the following guides below:

<a title="http://amirshk.com/blog/linux-home-server/" href="http://amirshk.com/blog/linux-home-server/" target="_blank">http://amirshk.com/blog/linux-home-server/</a>

<a title="http://linuxhomeserverguide.com/" href="http://linuxhomeserverguide.com/" target="_blank">http://linuxhomeserverguide.com/</a>

<a title="http://www.latentexistence.me.uk/zfs-and-ubuntu-home-server-howto/" href="http://www.latentexistence.me.uk/zfs-and-ubuntu-home-server-howto/" target="_blank">http://www.latentexistence.me.uk/zfs-and-ubuntu-home-server-howto/</a>

Using the guides above I was able to get the server up and running, the last one in particular was extremely helpful in getting ZFS working.

The current set up I have is a HP N54L running Ubuntu Server. It's an awesome little machine, and I've popped 2 x 2tb's of space into it for now, with an additional 2 bays for more storage when the time comes. I'm using it for a whole host of things, from a file server to media server. I'm using ZFS as my file system of choice, samba sharing for windows machines and NFS for the other linux machines. I've also got Virtualbox installed, hosting 2 more machines and keeping everything modularised. This lets me keep the main OS up and running constantly while only needing to reboot VM's as needed.

Some of the main issues I had with getting everything running I'll list below, along with my solutions:
<h3>Permissions</h3>
This was quite easily the most frustrating thing that I had to wrap my head around, not really being exposed to it much in Windows. Making sure that the groups and users have the same UID and GID across machines was the most important thing to ensure that my users had the correct permissions across the server. Also of note is that when setting up the samba share, the OS permissions override any samba permissions you have set which was a real cause of headache for me!
<h3>Shares</h3>
As I said above the first probem I had that was resolved was permissions and samba. I also found that it was best to not share the drives through ZFS but to just configure the samba shares through the normal means. This also gave me much greater control with the set up.

In setting everything up I ran into lots of issues, and I also found lots of solutions on the following websites below. I also started a thread which has some good advice and some write ups as I went along.

<a title="http://askubuntu.com/" href="http://askubuntu.com/" target="_blank">http://askubuntu.com/</a>

<a title="http://ubuntuforums.org/showthread.php?t=2210840" href="http://ubuntuforums.org/showthread.php?t=2210840" target="_blank">http://ubuntuforums.org/showthread.php?t=2210840</a>

I can definitely recommend the HP N54L if you're looking to set up a home server, it's a greta machine with space for 4 drives plus the OS drive if you flash the firmware to allow a HDD over the optical drive. There's a minor cult following with these microserver's and there are some people who've packed loads of laptop drives into them and really pushed them to the limits. I'm finding it great for not only hosting my work and library but as a media server and always-on machine.

&nbsp;