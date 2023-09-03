## About
This is a typing test I made in Python as one of my first projects using version control.
The code is pretty poorly optimized with lots of unnecessary things like globals, and there are a decent amount of bugs.

If you are looking for a typing test written in Python, this will require some tinkering depending on your OS and the quality you want. Personally, I'd recommend MonkeyType if you don't care if the test is in Python or not.

## Issues
- On MacOS, pressing the backspace key will sometimes place a ^? instead of deleting the previous character. Not sure what triggers this issue but it has something to do with the way I got keyboard inputs.
- In Tmux, the same things tends to happen.
  - I have a thread about the above issues (https://github.com/sjsaug/typing_test/issues/1) if you are wanting to look more into it. I found a few fixes but they all caused something else to break, so in the end I only run the program on Windows/Linux.
