# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from lockdefs.h @ 13-2.1.0-0-gd1d0186
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2021 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:
    # Python < 3.10
    class StrEnum(str, Enum):
        pass



# #define-ed constants

NoLock = 0

AccessShareLock = 1

RowShareLock = 2

RowExclusiveLock = 3

ShareUpdateExclusiveLock = 4

ShareLock = 5

ShareRowExclusiveLock = 6

ExclusiveLock = 7

AccessExclusiveLock = 8

MaxLockMode = 8
