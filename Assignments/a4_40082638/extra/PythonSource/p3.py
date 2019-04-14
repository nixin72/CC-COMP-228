def main():
    x = 10
    for i in range(0, 100):
        x += i
        if (x > 102):
            break
    print(x)

main()
