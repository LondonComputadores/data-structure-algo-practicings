"""
   Writing the Algorithm in Pseudocode
An algorithm is a step-by-step set of operations that need
to be performed. If you take an algorithm and write code to
1. https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks
Chapter 1. Turning Problems into Code • 6
report erratum • discuss
perform those operations, you end up with a computer
program.
If you’re new to programming and not entirely comfortable
with a programming language’s syntax yet, you should
consider writing out the algorithm using pseudocode, an
English-like syntax that lets you think about the logic without
having to worry about paper. Pseudocode isn’t just for
beginners; experienced programmers will occasionally write
some pseudocode on a whiteboard when working with
teammates to solve problems, or even by themselves.
There’s no “right way” to write pseudocode, although there
are some widely used terms. You might use Initialize to state
that you’re setting an initial value, Prompt to say that you’re
prompting for input, and Display to indicate what you’re
displaying on the screen.
Here’s how our tip calculator might look in pseudocode:
TipCalculator
Initialize billAmount to 0
Initialize tip to 0
Initialize tipRate to 0
Initialize total to 0
Prompt for billAmount with "What is the bill amount?"
Prompt for tipRate with "What is the tip rate?"
convert billAmount to a number
convert tipRate to a number
tip = billAmount * (tipRate / 100)
round tip up to nearest cent
total = billAmount + tip
Display "Tip: $" + tip
Display "Total: $" + total
End
That’s a rough stab at how our program’s algorithm will
look. We’ll have to set up some variables, make some decisions based on the input, do some conversions, and put some
output on the screen. I recommend including details like
variable names and text you’ll display on the screen in
pseudocode, because it helps you think more clearly about
the end result of the program.
report erratum • discuss
Chapter 1. Turning Problems into Code • 7
Is this the best way we could write the program? Probably
not. But that’s not the point. By writing pseudocode, we’ve
created something we can show to another developer to get
feedback, and it didn’t take long to throw it together.
Best of all, we can use this as a blueprint to code this up in
any programming language. Notice that our pseudocode
makes no assumptions about the language we might end
up using, but it does guide us as to what the variable names
will be and what the output to the end user will look like.
Once you write your initial version of the program and get
it working, you can start tweaking your code to improve it.
For example, you may split the program into functions, or
you may do the numerical conversions inline instead of as
separate steps. Just think of pseudocode as a planning tool. 
"""