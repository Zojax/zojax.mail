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
""" zojax.mail interfaces

$Id$
"""
from zope import schema, interface
from zope.i18nmessageid import MessageFactory
from zope.sendmail.interfaces import IMailDelivery
from z3c.schema.email import RFC822MailAddress

_ = MessageFactory('zojax.mail')


class IMessage(interface.Interface):
    """ email message """

    def __call__():
        """ return message as string """


class IMailAddress(interface.Interface):
    """ mail address adapter """

    address = RFC822MailAddress(
        title = u'Mail Address',
        required = True)


class IFromAddress(interface.Interface):
    """ message 'FROM' email address """

    from_address = RFC822MailAddress(
        title = u'From Address',
        required = True)


class IDestinationAddress(interface.Interface):
    """ message 'TO' email address """

    to_address = schema.Tuple(
        title = u'From Address',
        value_type = RFC822MailAddress(),
        required = True)


class IReturnAddress(interface.Interface):
    """ return address """

    return_address = RFC822MailAddress(
        title = u'Return Address',
        required = True)


class IErrorsAddress(interface.Interface):
    """ mail error handler for message,
    this allow set Errors-To and Return-Path header to handle error replies """

    errors_address = RFC822MailAddress(
        title = u'Erorrs Address',
        required = True)


class IMailer(IMailDelivery):

    hostname = schema.TextLine(
        title = _(u'SMTP server'),
        description = _(u'The address of your local SMTP (outgoing e-mail) '
                        u'server. Usually "localhost", unless you use an '
                        u'external server to send e-mail.'),
        default = u'localhost',
        required = True)

    port = schema.Int(
        title = _(u'SMTP Port'),
        description = _(u'The port of your local SMTP (outgoing e-mail) '
                        u'server. Usually "25".'),
        default = 25,
        required = True)

    username = schema.TextLine(
        title=_(u"Username"),
        description=_(u"Username used for optional SMTP authentication."),
        default=u'',
        required=False)

    password = schema.Password(
        title=_(u"Password"),
        description=_(u"Password used for optional SMTP authentication."),
        default=u'',
        required=False)

    email_from_name = schema.TextLine(
        title = _(u"Site 'From' name"),
        description = _(u'Portal generates e-mail using this name '
                        u'as the e-mail sender.'),
        default = u'Portal administrator',
        required = True)

    email_from_address = RFC822MailAddress(
        title = _(u"Site 'From' address"),
        description = _(u'Portal generates e-mail using this address '
                        u'as the e-mail return address.'),
        default = u'portal@zojax.net',
        required = True)

    errors_address = RFC822MailAddress(
        title = _(u"Site 'Errors' address"),
        description = _(u'Portal generates e-mail using this address '
                        u'as the errors handler address.'),
        required = False)

    def sendmail(context):
        """ send context by emails """


class IMailDebugSettings(interface.Interface):
    """ transport configuration """

    disabled = schema.Bool(
        title = _(u'Disabled'),
        description = _(u'Disable sending message.'),
        default = False)

    log_emails = schema.Bool(
        title = _(u'Log messages'),
        description= _(u'Log email address and message.'),
        default = False)

    no_delivery = schema.Bool(
        title = _(u'No delivery'),
        description = _('Disable final delivery to smtp server.'),
        default = False)


class IPrincipalByEMail(interface.Interface):
    """ email -> principal mapping service """

    def getPrincipal(email):
        """ return principal with email """
