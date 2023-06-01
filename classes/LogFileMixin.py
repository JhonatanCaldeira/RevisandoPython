from classes.log import Log


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)


if __name__ == '__main__':
    l = LogFileMixin()
    l.log('teste')
