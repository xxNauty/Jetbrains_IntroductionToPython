import some_module

print(f'This is a message from {__name__}.')
some_module.func()

if __name__ == "__main__":
    print('This should be printed ONLY when task.py is called directly.')

