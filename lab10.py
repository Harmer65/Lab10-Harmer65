# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.

class ArrayStack:
    def __init__(self):
        self._items = []
    
    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('cannot pop top element of an empty stack')

        return self._items.pop() # removes and returns the last element

def eval_rpn(tokens):
    op = {"+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y)} # to be completely honest I got this above part from a stack overflow thread. I understand how it works, and it wasnt really the purpose, so eeehhhh.
    while True:
        if len(tokens) < 3: 
            return tokens
        try:
            int(tokens[1])
            try:
                int(tokens[2])
                tokensTemp = tokens[1:len(tokens)]
                tokensTemp = eval_rpn(tokensTemp)
                tokens = tokens[0:1]
                toklen = len(tokensTemp)
                for i in range(toklen):
                    tokens.append(tokensTemp.pop(0))
            except:
                int(tokens[1])
                tokens[0] = str(op[tokens[2]](int(tokens.pop(0)),int(tokens.pop(0)))) #hated this line. the first pop takes the 0th value, then the second one takes the 0th one again since value 0 is now what value 1 was. its tokens[0] too since the original 0 and 1 are gone
        except:
            return tokens
    return tokens
    
    # Outline (write your plan here first):
    #   My first instict is to use a bunch of for and if operators, and im sure I could, but I will attempt to do it with stacks and such. I will take the first two digits, no matter what section of the operation we're on, it will be the two numbers we'd be working with. then Id take the operator which is the third. then after Im done the operation, I remove the first two and replace the operator with the result.
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9

def decode_string(s):
    stack1 = []
    stringer1 = ""
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)

        elif char == "[":
            stack1.append((stringer1, num))
            stringer1 = ""
            num = 0

        elif char == "]":
            stringer0, repeat_count = stack1.pop()
            stringer1 = stringer0 + stringer1 * repeat_count

        else:
            stringer1 += char

    return stringer1

    # Outline:
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"


def daily_temperatures(temps):
    result = [0] * len(temps)
    stack1 = []

    for i in range(len(temps)):
        while stack1 and temps[stack1[-1]]<temps[i]:
            prev = stack1.pop()
            result[prev] = i - prev
        stack1.append(i)

    return result    
    
    # Outline:
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]

def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(eval_rpn(["2", "1", "+", "3", "*"]))# == 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))# == 6
    print(eval_rpn(["3", "4", "+"]))# == 7
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))#22

    print(decode_string("3[a]2[bc]"))# == "aaabcbc"
    print(decode_string("3[a2[c]]"))# == "accaccacc"
    print(decode_string("2[abc]3[cd]ef"))# == "abcabccdcdcdef"
    print(decode_string("abc"))# == "abc"

    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))# == [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))# == [1, 1, 1, 0]
    print(daily_temperatures([30, 60, 90]))# == [1, 1, 0]
    print(daily_temperatures([50]))# == [0]
    pass


if __name__ == "__main__":
    main()
