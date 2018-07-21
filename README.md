# Python-Library

APS 7BM Python-Library has been forked by DD to make modifications to setup.py for system-agnostic cython compilation, and create a proper importable python module called "aps7bmlib" that can be used system-wide.

To access a module from anywhere on your system in python, you can then call "from aps7bmlib import <file>".
For example:
>> from aps7mblib import Combine_Scans
>> Combine_Scans.fprocess_files(**kwargs)

-- To install aps7bmlib system wide, do "python setup.py install"

-- To install aps7bmlib for your local user account , do "python setup.py install --user"

-- To install aps7bmlib in the local directory only, do "python setup.py develop"
