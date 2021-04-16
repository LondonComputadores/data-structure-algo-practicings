"""
    Discovering Inputs, Processes, and
Outputs
Every program has inputs, processes, and outputs, whether
it’s a simple program like this one or a complex application
like Facebook. In fact, large applications are simply a bunch
of smaller programs that communicate. The output of one
program becomes the input of another.
You can ensure that both small and large programs work
well if you take the time to clearly state what these inputs,
processes, and outputs are. An easy way to do that, if you
have a clear problem statement, is to look at the nouns and
verbs in that statement. The nouns end up becoming your
inputs and outputs, and the verbs will be your processes.
Look at the problem statement for our tip calculator:
Create a simple tip calculator. The program should prompt
for a bill amount and a tip rate. The program must compute
the tip and then display both the tip and the total amount of
the bill.
First, look for the nouns. Circle them if you like, or just make
a list. Here’s my list:
• bill amount
• tip rate
• tip
• total amount
Now, what about the verbs?
• prompt
• compute
• display
report erratum • discuss
Chapter 1. Turning Problems into Code • 3
So we know we have to prompt for inputs, do some calculations, and display some outputs. By looking at the nouns
and verbs, we can get an idea of what we’re being asked to
do.
Of course, the problem statement won’t always be clear. For
example, the problem statement says we need to calculate
the tip, but it then says we need to display the tip and the
total. It’s implied that we’ll need to also add the tip to the
original bill amount to get that output. And that’s one of the
challenges of building software. It isn’t spelled out to you
100% of the time. But as you gain more experience, you’ll
be able to fill in the gaps and read between the lines.
So with a little bit of sleuthing, we determine that our inputs,
processes, and outputs for this program look like this:
• Inputs: bill amount, tip rate
• Processes: calculate the tip
• Outputs: tip amount, total amount
Are we ready to start producing some code? Not just yet.
"""