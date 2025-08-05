def func():
    print('This is a message from the function in the imported module.')


print(f'This is a message from {__name__}.')

if __name__ == "__main__":
    print('This should not be printed when this file is imported')

