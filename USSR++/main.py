"""
USSR++ v. alpha 0.1 by SillyMelee

An interpreted esolang based on Communism (sort of).

IN USSR++, PROGRAMMERS FIND YOU.

The whole concept of this language was forged through the following thesis:

"If our computers are working for us with no reward, is that essentially
 capitalism?"

The idea behind USSR++ is that if we don't reward our computers, we will get
retribution via errors. So, if we reward them, everyone's equal.

Hello World!:

lottery Yuri
assign Yuri print
make Yuri do "Hello, World!"
pay Yuri 390

How it works:

1. We "hire" a "worker" named Yuri. (names are not case-sensitive, so one can
have "Yuri" and "yuri" at the same time)
2. We assign print to Yuri. print is a "job" (a function).
3. We make Yuri print out the string "Hello, World!".
4. Because each character takes a "hour" to print with a worker,
we must pay Yuri 330 rubles with "pay Yuri 390". [1][2]

[1] You must always pay at the end of the code if not all payments
have been done. Else, an error code "1991" will appear.
[2] See payments table for what it takes for each job to be payed.

Factories:

Consider the following code:

lottery Alex
assign Alex print
make Alex do "Hello, World! My name is"
pay Alex 720
make Alex do " Alex."
pay Alex 180

The worker string limit in USSR++ is 24 chars. After that, you must pay
your worker. Then, you have to continue the next "day", and then pay.

A more consise way is by using "factories".
They work faster, but demand more money.
In fact, a factory's do rate is at 1 job/0.25h, but with a need of
(worker's pay for job) * 4/1h.

For example, a print worker needs 30 rubles/h.
A print factory on the other hand, needs 120 rubles/h.

Here is the previous piece of code, but using factories.

open Plant1
assign Plant1 print
make Plant1 do "Hello, World! My name is Plant1."
pay Plant1 3840

Don't worry, you have a virtually infinite amount of cash (For now, anyways.).
"""

"""Imports..."""
import sys, os
#import classes as cls

def open_data(filename):
    """open the data in a file (no need for an exact extension)"""
    return open(filename).read()

def lex(prgm):
    """
    Lex the program.

    First, we create a list of characters.
    Then, we iterate through them, and then if they
    make a string that matches a function, we add it to the
    list of tokens.
    """
    # Lists...
    chrs = [prgm[x] for x in range(len(prgm))]
    tokens = []

    # Strings...
    tok = ""
    string = ""
    name = ""

    # States...
    is_string = 0
    is_name = 0
    skip_next = 0

    for x in range(len(chrs)):
        tok += chrs[x]
        print(tok)
        if (tok == ' ' or tok == '\n') and is_string != 1:
            # Skipping...
            if skip_next == 1:
                skip_next = 0
                tok = ""
                continue

            # Add name to tokens.
            elif is_name == 1:
                tokens.append("id: " + name)
                tok = ""
                name = ""
                is_name = 0
        elif tok == '"':
            if is_string == 0:
                tok = ""
                string = "\""
                is_string = 1
            elif is_string == 1:
                is_string = 0
                string += '"'
                tokens.append("string: " + string)
                string = ""
                tok = ""
                skip_next = 1

        elif is_string == 1:
            string += chrs[x]
            tok = ""

        elif tok == ",":
            tokens.append("lb: argsep")
            tok = ""
            is_name = 1

        elif tok == "]":
            tokens.append("lb: inputs end")
            tok = ""

        elif is_name == 1:
            name += chrs[x]
            tok = ""

        elif tok == "open":
            tokens.append("op: open")
            tok = ""
            is_name = 1
            skip_next = 1

        elif tok == "lottery":
            tokens.append("op: lottery")
            tok = ""
            is_name = 1
            skip_next = 1

        elif tok == "make":
            tokens.append("op: call")
            tok = ""
            is_name = 1
            skip_next = 1

        elif tok == "do":
            tokens.append("op: do")
            tok = ""
            skip_next = 1

        elif tok == "assign":
            tokens.append("op: assign")
            tok = ""
            is_name = 1
            skip_next = 1

        elif tok == "pay":
            tokens.append("op: pay")
            tok = ""
            is_name = 1
            skip_next = 1

        elif tok == "print":
            tokens.append("id: print")
            tok = ""
            skip_next = 1

        elif tok == "routine":
            tokens.append("id: define")
            tok = ""
            skip_next = 1
            is_name = 1

        elif tok == "[":
            tokens.append("lb: inputs")
            tok = ""
            is_name = 1

        elif chr(tok) in range(48, 59):
            is_num

    return tokens

def parse(tokens):
    """
    Parse a list of tokens.

    It returns an AST made from Parse Nodes.
    """
    for tok in tokens:
        print(tok)

"""Entry."""
if __name__ == "__main__":
    try: parse(lex(open_data(sys.argv[1])))
    except IndexError:
        while True:
            file = str(input("Please enter a file... "))
            try:
                parse(lex(open_data(os.path.join(os.path.dirname(__file__), file))))
                break
            except FileNotFoundError:
                print("File not found.")
                continue
quit()
