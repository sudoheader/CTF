## No Space Between Us Walkthrough

This one was a doozy. Mainly because of the way I went about it.

The problem statement says to interact with the bot @StoryTellerBot on the nahamsec discord.

After some tries with different stories, I started to noticing that it was random and that it would only go up to a certain number of stories, in this case it was 38, including 0. Meaning there was 38 stories in total but "story 38" did not return any stories, because again we start at 0.

So after doing this up to "story 37" I found that if the query was out of bounds or completely random, it would repeat 'Hmm you must want a story. I'm told I'm a good story teller! Just tell me which story you want - "story 1", maybe? or 2? or 12?'

Go back and read the problem statement again and see the part that says "there needs to be zero space between".

Anything familiar that you can think of?

Well if not, no worries, because I'll tell you what that "zero space" really means.

Copy and paste into a text editor one of the stories that the bot printed out. I suggest vim for this. Just few lines is really needed here.

Now look at the first few lines. Notice something? There is some weird string between the spaces for a few of the words, right?

They start with "<200c>" and "<200d>". Apparently, each zero-width string is not visible on Discord but it can be seen using vim for instance.

The whitespace character "<200c>" is supposed to represent the binary number 0 and "<200d>" the binary number 1.

Now do this: copy/paste each story into a text editor and take out all the words from it. In vim, you can select all lines in the text and do a search and replace for words with ":'<,'>s/\w//g" for the search and replace command.

##### NOTE: Make sure you have selected the first line "gg" in NORMAL mode and then "0". You would then need to switch to VISUAL mode with "Shift-V" and do "G" to select up to the end of the text in the editor. Then you can try that command.

This will not remove all the punctuations in the text so go one by one and delete those too.

Once you are done, you should open another text editor and for each "<200c>" input a 0 and "<200d>" input a 1.

I suggest to not do this using a text editor, because of the chance of error, and instead go to https://gchq.github.io/CyberChef/ where you can paste your text there.

It will not properly output anything except dots because, again, we are dealing with invisible whitespace characters so go to Operations and search for "Decode text".

Select from the drop down any encoding you wish. I suggest somthing easy that you can "Find / Replace" with like "IBM EBCDIC US-Canada (037 + Euro symbol) (1140)".

Now select the first three characters in the output. This will be 0.

Search in Operations for "Find / Replace". You will need to do this twice, (three times if you want to be more precise).

In the "Find / Replace" Recipe, enter the first 3 characters to replace for 0, and do the same for the next 3 to replace for 1 in the output.

Now you should get all 1's and 0's in the output. However, we need to replace the "." with a "\n" so copy the output text and in `vim`, search and replace all of the text for "." like so: ":'<,'>s/\./\n/g" or do it manually.

##### NOTE: I have not found a way to do this in CyberChef so ping me if you know a way to do it!

Last but not least copy our binary text from `vim` and in CyberChef paste it in a new tab or hit the circle with a diagonal line accross it for all the operations in the Recipe and search in Operations for "From Binary".

Here, with a delimiter set to "Space" or "None" we can see the flag.

PS: I througly enjoyed this challenges even with the pitfalls that I encountered!
Thanks to the author @Kkevsterrr#7469 for a great Steganography challenge!

Solution:

In case you still can't figure it out try out only parts of the text one at a time and then go from there.
One thing I have learn from CTF challenges is that if you can reduce the problem to something that can easily be solved, there is nothing stopping you from obtaining those flags!

So try it out! Otherwise read below for the solution.

Click here for more info: https://gchq.github.io/CyberChef/#recipe=Decode_text('IBM%20EBCDIC%20US-Canada%20(037%20%2B%20Euro%20symbol)%20(1140)'/disabled)Find_/_Replace(%7B'option':'Regex','string':'S%C3%98%C3%B0'%7D,'0',true,false,true,false/disabled)Find_/_Replace(%7B'option':'Regex','string':'S%C3%98%C3%BD'%7D,'0',true,false,true,false/disabled)Find_/_Replace(%7B'option':'Regex','string':'%5C%5C.'%7D,'',true,false,false,false/disabled)From_Binary('Space',8)&input=MDExMDAxMTAKMDExMDExMDAKMDExMDAwMDEKMDExMDAxMTEKMDExMTEwMTEKMDExMDAxMDEKMDAxMTAxMDAKMDExMDAxMDEKMDAxMTAxMDEKMDExMDAwMDEKMDExMDAxMDAKMDAxMTAwMTEKMDAxMTAwMTEKMDExMDAxMDEKMDExMDAwMTAKMDAxMTAwMDEKMDAxMTAxMTAKMDAxMTAxMDAKMDAxMTAwMTAKMDAxMTAxMTAKMDExMDAxMDAKMDAxMTAxMDEKMDAxMTAwMTAKMDExMDAwMTAKMDAxMTEwMDEKMDAxMTAxMDAKMDExMDAxMDEKMDAxMTAwMTEKMDAxMTEwMDEKMDAxMTEwMDAKMDExMDAxMDEKMDAxMTAxMDEKMDAxMTEwMDEKMDAxMTAwMTEKMDAxMTAxMDAKMDAxMTAxMTAKMDAxMTAxMTAKMDExMTExMDE

