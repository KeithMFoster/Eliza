# Eliza - A Python Example
# 
# Copyright 2023 Keith Foster
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial 
# portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import json
import re
import random


# read_data(input file name)
# This function will read the filename that is passed by name and return the contents to the caller. The file
# must be in JSON format.
def read_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


# chat(variable object in json format)
# This is the main loop of the program. It will take the psychobabble json contents and start the session with you
# as its patient. As you input sentences into the input string, the string is broken down using regular expressions
# and matched with the contents of the reflections JSON file. If a match is found in the psychobabble JSON contents,
# then the response is generated from the matched response. If by chance there is no response, everything will fall out
# and the "I don't understand" response will be given. Everything is kept in a loop until the user inputs a single q to
# quit.
def chat(psychobabble):
    reflections = read_data("reflections.json")
    user_input = input("You: ")
    while user_input != 'q':
        response = None
        for pattern, responses in psychobabble:
            match = re.match(pattern, user_input)
            if match:
                response = random.choice(responses)
                break
        if response:
            print("ELIZA: " + response.format(*[reflections.get(word, word) for word in user_input.split()]))
        else:
            print("ELIZA: I'm sorry, I don't understand.")
        user_input = input("You: ")


if __name__ == '__main__':
    psychobabble = read_data("psychobabble.json")
    chat(psychobabble)
