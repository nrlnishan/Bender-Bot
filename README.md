# Bender-Bot

Bender bot is a simple python based CLI project to save todos or some text. You can interact with Bender 🤖, our friendly robot to save your snippets or todos in command line. 

## What you can do with Bender

Create a simple todos or snippets or whatever. Just write something and ask bender to save it. Want to know what you have saved? Ask bender to display it. Don't need it? Ask bender to delete it. Run the file ```bender.py``` and interact with Bender 🤖

## Commands

>[new]

* Usage: 
bender new

* What it does:
Bender starts to capture what you write

>[save] [argument]

* Usage:
bender save #mytodos

* What it does:
Bender saves what you wrote under the hashtag that you provided as an argument

>[discard]

* Usage:
bender discard

* What it does:
Bender discards whatever you were writing and starts listening for your other commands

>[list] [argument]

* Usage:
bender list --tags
bender list #mytodos

* What it does:
Bender lists out all the hashtags that you have saved. If you specify particular hashtag as shown above, bender displays the content which was saved under that hashtag

>[exit]

* Usage:
bender exit

* What it does:
Bender goes to sleep.









