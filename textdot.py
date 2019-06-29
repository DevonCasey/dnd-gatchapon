def text(text_to_print,num_of_dots,num_of_loops):
    from time import sleep
    import keyboard
    import sys
    shell = sys.stdout
    shell.write(text_to_print)
    dotes = int(num_of_dots) * '.'
    for last in range(0,num_of_loops):
        for dot in dotes:
            keyboard.write('.')
            sleep(0.1)
        for dot in dotes:
            keyboard.write('\x08')
            sleep(0.1)