import os, random, time

if __name__ == '__main__':
    ts = os.get_terminal_size()
    width = ts.columns
    running = True
    counter = 1
    while running:
        symbol = "/" if random.choice([True, False]) else "\\"
        if counter == width:
            print(symbol, flush=True)
        else:
            print(symbol, flush=True, end='')
        time.sleep(0.05)
