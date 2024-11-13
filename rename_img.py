import os


def photo():
    os.chdir('images')
    print(os.getcwd())
    firstname = 'cat' 

    for name in os.listdir():
        name_split = name.split('.')
        #if name_split[-1] != 'jpg':
        os.rename(name, firstname + '_' + name_split[0] + '.jpg')


def main():
    photo()


if __name__ == '__main__':
    main()