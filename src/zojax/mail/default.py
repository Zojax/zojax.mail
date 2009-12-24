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
from email.Utils import formataddr

from zope import interface, component
from zope.component import getUtility

from interfaces import IMailer, IFromAddress, IErrorsAddress


class DefaultFromAddress(object):
    component.adapts(interface.Interface)
    interface.implements(IFromAddress)

    def __init__(self, template):
        configlet = getUtility(IMailer)

        self.from_address = formataddr(
            (configlet.email_from_name,
             configlet.email_from_address))


class DefaultErrorsAddress(object):
    component.adapts(interface.Interface)
    interface.implements(IErrorsAddress)

    def __init__(self, address):
        self.errors_address = getUtility(IMailer).errors_address
