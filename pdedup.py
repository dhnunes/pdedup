"""
TODO DOCstring.

docstring
"""

from Library.filehasher import FileHasher
from Library.cmdargs import CmdArgs

if __name__ == '__main__':

    args = CmdArgs.cmd_parsed_args()
    file = FileHasher(args["dir_path"])
    result = file.file_walker()
