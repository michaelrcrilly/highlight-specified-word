Highlight a word in a string given its index position
====

Example:
----
string = `This is an example string`
position = 2

» This is an example string   
»         ^

Invalid indices result in the following behaviour:
----
string = `This is an example string`
position = -1

» This is an example string   
»                           ^
