Highlight a word in a string given its index position
====

Example:
----
string = `This is an example string`
position = 2   

<pre>
» This is an example string   
»         ^
</pre>

Invalid indices result in the following behaviour:
----
string = `This is an example string`
position = -1   

<pre>
» This is an example string   
»                           ^
</pre>
