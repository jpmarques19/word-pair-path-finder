import os

def main():
    """main function"""
    with open('tree.txt', 'w') as file:
        for root, dirs, files in os.walk('.'):
            level = root.replace('.', '').count(os.sep)
            indent = ' ' * 4 * (level)
            file.write('{}{}/\n'.format(indent, os.path.basename(root)))  # Use single-line string
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                file.write('{}{}\n'.format(subindent, f))  # Use single-line string

if __name__ == '__main__':
    main()
