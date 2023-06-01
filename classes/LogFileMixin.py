from classes.log import Log
from pathlib import Path

LOG_FILE = Path(__file__).parent.joinpath('../log') / 'log.txt'


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} from {self.__class__.__name__}'
        with open(LOG_FILE, '+a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


if __name__ == '__main__':
    l = LogFileMixin()
    l.log_success('Logando')
    l.log_error('Logando')
