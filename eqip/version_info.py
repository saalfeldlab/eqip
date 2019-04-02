import sys

__major__   = 0
__minor__   = 5
__patch__   = 2
__tag__     = 'dev0'
__version__ = f'{__major__}.{__minor__}.{__patch__}.{__tag__}'.strip('.')

class _Version(object):

    def major(self):
        return __major__

    def minor(self):
        return __minor__

    def patch(self):
        return __patch__

    def tag(self):
        return __tag__

    def version(self):
        return __version__

    def is_release(self):
        return self.tag() == ''

    def __str__(self):
        return self.version()

_version = _Version()

