import textwrap

def wrap(string, max_width):
    res = []
    line = []
    
    for letter in string:
        
        if len(line) == max_width:
            res.append("".join(line))
            res.append("\n")
            line.clear()
            
        line.append(letter)
            
    return "".join(res)+"".join(line)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
