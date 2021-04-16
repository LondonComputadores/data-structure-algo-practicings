"""
    Turning Problems into Code
If you’re new to programming, you may wonder how
experienced developers can look at a problem and turn it
into runnable code. It turns out that writing the actual code
is only a small part of the process. You have to break down
the problem before you can solve it. If you’ve ever watched
an experienced programmer, it may look like they just
cracked open their code editor and banged out a solution.
But over the years, they’ve broken down hundreds, if not
thousands, of problems, and they can see patterns. If you’re
just starting out, you might not know how to do that. So in
this chapter we’ll look at one way to break down problems
and turn them into code. And you can use this approach to
conquer the problems in the rest of this book.

Understanding the Problem
One of the best ways to figure out what you have to do is to
write it down. If I told you that I wanted a tip calculator
application, would that be enough information for you to
just go and build one? Probably not. You’d probably have
to ask me a few questions. This is often called gathering
requirements, but I like to think of it as figuring out what
features the program should have.
Think of a few questions you could ask me that would let
you get a clearer picture of what I want. What do you need
to know to build this application?
Got some questions? Great. Here are some you might ask:
report erratum • discuss
• What formula do you want to use? Can you explain how
the tip should be calculated?
• What’s the tip percentage? Is it 15% or should the user
be able to modify it?
• What should the program display on the screen when
it starts?
• What should the program display for its output? Do
you want to see the tip and the total or just the total?
Once you have the answers to your questions, try writing
out a problem statement that explains exactly what you’re
building. Here’s the problem statement for the program
we’re going to build:
Create a simple tip calculator. The program should prompt
for a bill amount and a tip rate. The program must compute
the tip and then display both the tip and the total amount of
the bill.
Example output:
What is the bill? $200
What is the tip percentage? 15
The tip is $30.00
The total is $230.00

What do I do with complex
programs?

Break down the large program into smaller features that are
easier to manage. If you do that, you’ll have a better chance of
success because each feature can be fleshed out. And most
complex applications out there are composed of many smaller
programs working together. That’s how command-line tools in
Linux work; one program’s output can be another program’s
input

If you’re ready to open your text editor and hammer out the
code, you’re jumping way ahead of yourself. You see, if you
don’t take the time to carefully design the program, you
might end up with something that works but isn’t good
quality. And unfortunately, it’s very easy for something like
that to get out into the wild. For example, you hammer out
Chapter 1. Turning Problems into Code • 2
report erratum • discuss
your program without testing, planning, or documenting it,
and your boss sees it, thinks it’s done, and tells you to release
it. Now you have untested, unplanned code in production,
and you’ll probably be asked to make changes to it later.
Code that’s poorly designed is very hard to maintain or
extend. So let’s take this tip calculator example and go
through a simple process that will help you understand what
you’re supposed to build.
"""