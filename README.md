# captureone_aspectpad
This program gives an image a frame, padding it out to a specified aspect ratio, center & colour.
The defaults are an instagram friendly aspect ratio of 1080 * 1350 and a black background.
Colour can be changed by passing one to add_padding.


Copy and paste the following into an automator "shell script" command.
Shell must be set to "bin/bash" and Pass Input must be set to "as argument"

*/usr/local/bin/python3 [your path] "$1"*

*[your path]* can be found by dragging this python file onto a terminal window and copy-pasting the
output. Don't forget to remove the [] surrounding [your path]!
