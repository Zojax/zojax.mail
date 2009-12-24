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
import logging
from zope import interface
from zope.component import getUtility
from zope.sendmail.mailer import SMTPMailer

from interfaces import IMailer
from interfaces import IMailDebugSettings
from interfaces import IMessage, IFromAddress, IDestinationAddress


class Mailer(object):
    interface.implements(IMailer)

    def send(self, fromaddr, toaddrs, message):
        if self.username and self.password:
            mailer = SMTPMailer(self.hostname, self.port,
                                self.username, self.password)
        else:
            mailer = SMTPMailer(self.hostname, self.port)

        try:
            mailer.send(fromaddr, toaddrs, message)
        except Exception, err:
            logging.getLogger('zojax.mail').exception(str(err))

    def sendmail(self, context):
        debug_config = getUtility(IMailDebugSettings)
        if debug_config.disabled:
            return

        # generate message
        message = IMessage(context)()

        # log message
        if debug_config.log_emails:
            logger = logging.getLogger('zojax.mail')
            logger.log(
                logging.INFO, str(IDestinationAddress(context).to_address))
            logger.log(logging.INFO, message)

        # delivery
        if debug_config.no_delivery:
            return

        self.send(IFromAddress(context).from_address,
                  IDestinationAddress(context).to_address, message)
