class FileMgr:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # if exc_type is not None:
        #     print('exception had been handled')
        print('exec:', exc_type, exc_val)
        print('exit')
        return True

with FileMgr('a.txt') as file:
    print('do sth')
    file.write('write sth')
    file.aaa()
print('at last')