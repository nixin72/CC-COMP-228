def strlen(string):
    length = 0
    curr = string[length]
    while (curr != "\\"):
        length += 1
        curr = string[length]
    return length

def scanf(y):
    i = 0
    while True:
        string = input()[0]
        y[i] = string
        i+=1
        if (string == "\\"):
            break

    return y

def halt(exitCode):
    print(exitCode)
    exit(exitCode)

def func1(x):
    y = [0,0,0,0,0,0,0,0,0]
    y = scanf(y)
    if strlen(y) != x:
        halt(1)

def main():
    print(list("Enter a passphrase:\n(Use \"\\\" as null terminator)"))
    func1(8)
    return 0

halt(main())
