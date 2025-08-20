import argparse 

class FileTypeWithExtensionCheck(argparse.FileType):
    def __init__(self, mode='r', valid_extensions=None, **kwargs):
        super().__init__(mode, **kwargs)
        self.valid_extensions = valid_extensions

    def __call__(self, string):
        if self.valid_extensions:
            if not string.endswith(self.valid_extensions):
                raise argparse.ArgumentTypeError(
                    'Not a valid filename extension')
        return super().__call__(string)