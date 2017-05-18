"""This module exports the Gcc plugin class."""

from cuda_lint import Linter, util
from cudatext import *

class Gcc(Linter):

    """Provides an interface to gcc.exe."""
    cmd = None
    executable = 'gcc'
    multiline = False
    syntax = ('C', 'C improved', 'C++', 'C++11')
    regex = (
        r'<stdin>:(?P<line>\d+):(?P<col>\d+):\s*'
        r'.*?((?P<error>error)|(?P<warning>warning|note)):\s*'
        r'(?P<message>.+)'
    )
    base_cmd = (
        '-c '
        '-fsyntax-only '
        '-Wall '
        '-O0 '
    )


    def split_match(self, match):
   
        """Return the components of the error."""
        split_match = super(Gcc, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        
        return match, line, col, error, warning, message, ''


    def cmd(self):
    
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        if ed.get_prop(PROP_LEXER_FILE) in ['C', 'C improved']:
            code_type = 'c'
        else:
            code_type = 'c++'

        result += ' -x {0} -'.format(code_type)

        return result
