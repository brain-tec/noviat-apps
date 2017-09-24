# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Upload Payment Order via EBICS',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Noviat',
    'category': 'Accounting & Finance',
    'depends': [
        'account_ebics',
        'account_banking_sepa_credit_transfer'],
    'data': [
        'wizard/banking_export_sepa_wizard.xml',
    ],
    'installable': True,
}
