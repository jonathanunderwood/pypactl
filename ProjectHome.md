Utility for advanced control pulseaudio server via command line interface, written in python.

pactl tool, that go with pulseaudio server, don't have some functions, that I need, so I created the similar interface in python to advanced control pulseaudio sever via command line.

For example, when I changing the volume in 5.1 channel sync to 0% or 100%, pulseaudio breaks all per-channel volume configuration.

It is my first development version.

At now it can only do the mute, set volume, increase/decrease volume and every time it restores the per-channel volumes to initial balance, described in config.

Working commands:

$ pypactl sink **id** toggle _#toggle mute/unmute sink_

$ pypactl sink **id** setvolume **val** _#set sink volume to val, and restores per-channel volumes. Min 0, max 100._

$ pypactl sink **id** incvolume **val** _#increase/decrease volume by value, you can set negative value for decrease, for example -2_

Per-channel volumes at now is hardcoded in pypactl file:
# custom channel volumes for volume
# front left, front right, rear left, rear right, front center, subwoofer
vol4channels = [70,70,90,90,100,60]

You can specify your custom values for this array.

## Examples: ##

$ pypactl sink 0 incvolume -3 _#decrease volume for first sink to 3%_