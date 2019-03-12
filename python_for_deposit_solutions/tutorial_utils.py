import logging
import subprocess

# analagous to the unix command which but with memoization functions.
try:
    from salt.utils import which as find_executable
except ImportError:
    from distutils.spawn import find_executable

log = logging.getLogger(__name__)


def Property(func):
    return property(**func())


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ExecutableNotFound(Error):
    pass


class memoise_which:
    """
    memoization of the which command
    """
    def __init__(self, exec_name):
        self.name = exec_name
        self._path = None

    @Property
    def path():
        doc = "the path to the exeutable"

        def fget(self):
            if self._path is not None:
                return self._path
            self._path = find_executable(self.name)
            if self._path is None:
                msg = "Could not find executable:{executable}".format(executable=self.name)
                log.error(msg)
                raise ExecutableNotFound(msg)
            return self._path
        return locals()


def execute_local_command(command_attrib_list):
    proc = subprocess.Popen(command_attrib_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    stdout, stderr = proc.communicate()

    retcode = proc.returncode
    return retcode, stdout, stderr


if __name__ == '__main__':
    which_which = memoise_which('which')
    print(execute_local_command(['which', 'which']))
