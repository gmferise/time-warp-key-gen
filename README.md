# Installation and Usage
No package manager is required. Run using python 3.9+

Usage: `python key_generator.py`

# Original Prompt:
Let's rewind back to the year 1995 -- computers aren't super powerful, size is of the essence, and software piracy was still in its relative infancy. Pretend you've got a shareware program that you'd like to distribute and a key server to build -- gotta keep it protected for as long as possible before someone figures out a crack. The key will be generated ahead of time and printed on the inside cover of the CD case; we can't modify the program each time the CD is stamped, so every CD needs to be able to accept every generated key... without calling home.

What we're looking to do is build the logic behind a conceptual keyserver. We won't be actually building the endpoints, just the scriptable bits. 

## Goal:

A pair of functions: a generator and a validator. The generator takes in no arguments and spits out a "random" key with attributes (length, specific characters, etc.) of your choosing. If that key is fed into the validator (as the only argument) then the validator should be able to respond with a boolean showing whether or not the key is valid (and, in theory, the person actually paid us money to use our software). The generator and the validator cannot communicate (like import each other, use shared functions, etc. -- they must be completely separate entities).

You can make it as cryptographically secure as you want, but keep in mind that the goal is just to outwit people trying to steal your stuff. How would they first try to break it? How can we stop them for the longest amount of time while expending the absolute minimum amount of effort on our side?

Upload your solution as a gist on GitHub and submit the URL. Try to use only pieces of the standard library (hint: take a look at `hashlib`, `hmac`, and / or `secrets` in Python. Alternatively, maybe `ord` and `chr` are your friends here?)

