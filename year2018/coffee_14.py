from configparser import ConfigParser

if __name__ == '__main__':
    config = ConfigParser()
    config.read('./conf/settings.ini')

    reg_stickers_count = config.get('sbux', 'reg_stickers')
