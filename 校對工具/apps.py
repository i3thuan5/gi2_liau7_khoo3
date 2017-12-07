import Pyro4
from django.apps import AppConfig
from sys import stderr


class 校對工具Config(AppConfig):
    name = '校對工具'

    def ready(self):
        工具 = Pyro4.Proxy("PYRONAME:校對工具")
        try:
            工具.口語標漢字本調('sui1')
        except Pyro4.errors.NamingError:
            print(
                '\n'.join([
                    '請確定有開這兩个指令，無會無法度用「標本調」佮「轉漢字本調」',
                    'python -m Pyro4.naming',
                    'python manage.py 校對工具服務',
                    '',
                ]),
                file=stderr
            )
        except Pyro4.errors.CommunicationError:
            print(
                '\n'.join([
                    '請確定「{}」開好矣'.format('python manage.py 校對工具服務'),
                ]),
                file=stderr
            )
