#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2004-2008 Tiny SPRL (http://tiny.be) All Rights Reserved.
#
# $Id$
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
###############################################################################

name = 'openerp-server'
version = '4.3.0'
description = 'OpenERP Server'
long_desc = '''\
OpenERP is a complete ERP and CRM. The main features are accounting (analytic
and financial), stock management, sales and purchases management, tasks
automation, marketing campaigns, help desk, POS, etc. Technical features include
a distributed server, flexible workflows, an object database, a dynamic GUI,
customizable reports, and SOAP and XML-RPC interfaces.
'''
classifiers = """\
Development Status :: 5 - Production/Stable
License :: OSI Approved :: GNU General Public License Version 2 (GPL-2)
Programming Language :: Python
"""
url = 'http://www.openerp.com'
author = 'Tiny.be'
author_email = 'info@tiny.be'
support_email = 'support@openerp.com'
license = 'GPL-2'

try:
    # if the sources are taken from the bzr repository, 
    # append the revision number and the date of the bzr branch
    from bzrlib.branch import Branch
    from bzrlib.osutils import format_date
    try:
        from os.path import dirname
        _branch = Branch.open(dirname(dirname(__file__)))
        _lastrev = _branch.repository.get_revision(_branch.last_revision())
        _date = format_date(_lastrev.timestamp, _lastrev.timezone)
        version = "%s~bzr-%s (%s)" % (version, _branch.revno(), _date)
    except:
        # This is not because bzr is installed that openerp is under revision.
        pass
except ImportError:
    pass

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

