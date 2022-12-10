"""
    Driving Design with Tests
One of the best ways to design and develop software is to
think about the result you want to get right from the start.
Many professional software developers do this using a formal process called test-driven development, or TDD. In TDD,
you write bits of code that test the outputs of your program
or the outputs of the individual programs that make up a
larger program. This process of testing as you go guides you
toward good design and helps you think about the issues
your program might have.
TDD does require some knowledge about the language
you’re using and a little more experience than the beginning
developer has out of the gate.
However, the essence of TDD is to think about what the
expected result of the program is ahead of time and then
work toward getting there. And if you do that before you
write code, it’ll make you think beyond what the initial
requirements say. So if you’re not quite comfortable doing
formal TDD, you can still get many of the benefits by creating
Chapter 1. Turning Problems into Code • 4
report erratum • discuss
simple test plans. A test plan lists the program’s inputs and
its expected result.
Here’s what a test plan looks like:
Inputs:
Expected result:
Actual result:
You list the program inputs and then write out what the
program’s output should be. And then you run your program and compare the expected result with the actual result
your program gives out.
Let’s put this into practice by thinking about our tip calculator. How will we know what the program’s output should
be? How will we know if we calculate it correctly?
Well, let’s define how we want things to work by using some
test plans. We’ll do a very simple test plan first.
Inputs:
bill amount: 10
tip rate: 15
Expected result:
Tip: $1.50
Total: $11.50
That test plan tells us a couple things. First, it tells us that
we’ll take in two inputs: a bill amount of 10 and a tip rate of
15. So we’ll need to handle converting the tip rate from a
whole number to a decimal when we do the math. It also
tells us we’ll print out the tip and total formatted as currency.
So we know that we’d better do some conversions in our
program.
Now, one test isn’t enough. What if we used 11.25 as an
input? Using a test plan, what should the output be? Try it
out. Fill in the following plan:
Input:
bill amount: 11.25
tip rate: 15
Expected result:
Tip: ???
Total: ???
report erratum • discuss
Chapter 1. Turning Problems into Code • 5
I assume you just went and used a calculator to figure out
the tip. If you ran the calculation, your calculator probably
said the tip should be 1.6875.
But is that realistic? Probably not. We would probably round
up to the nearest cent. So our test plan would look like this:
Input:
bill amount: 11.25
tip rate: 15
Expected result:
Tip: $1.69
Total: $12.94
We just used a test to design the functionality of our program; we determined that our program will need to round
up the answer.
When you’re going through the exercises in this book, take
the time to develop at least four test plans for every program,
and try to think of as many scenarios as you can for how
people might break the program. And as you get into the
more complicated problems, you may need a lot more test
plans.
If you’re an experienced software developer who wants to
get started with TDD, you should use the exercises in this
book to get acquainted with the libraries and tools your
favorite language has to offer. You can find a list of testing
frameworks for many programming languages at
Wikipedia.1 You can read Kent Beck’s Test-Driven Development: By Example to gain more insight into how to design
code with tests, or you can investigate any number of more
language-specific resources on TDD.
So now that we have a clearer picture of the features the
program will have, we can start putting together the algorithm for the program.
"""