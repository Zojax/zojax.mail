##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope.component import getUtilitiesFor
from zope.app.security.interfaces import PrincipalLookupError

from interfaces import IPrincipalByEMail


def getPrincipalByEMail(email):
    for name, utility in getUtilitiesFor(IPrincipalByEMail):
        principal = utility.getPrincipal(email)
        if principal is not None:
            return principal

    raise PrincipalLookupError

getPrincipalByEmail = getPrincipalByEMail
