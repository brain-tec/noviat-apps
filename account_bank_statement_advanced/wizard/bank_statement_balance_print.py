# -*- coding: utf-8 -*-
# Copyright 2009-2018 Noviat.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import time
from odoo import api, fields, models


class BankStatementBalancePrint(models.TransientModel):
    _name = 'bank.statement.balance.print'
    _description = 'Bank Statement Balances Report'

    @api.model
    def _get_journals(self):
        return self.env['account.journal'].search([('type', '=', 'bank')])

    journal_ids = fields.Many2many(
        comodel_name='account.journal', string='Financial Journal(s)',
        domain=[('type', '=', 'bank')], default=_get_journals,
        help="Select here the Financial Journal(s) you want to include "
             "in your Bank Statement Balances Report.")
    date_balance = fields.Date(
        string='Date', required=True, default=time.strftime('%Y-%m-%d'))

    @api.multi
    def balance_print(self):
        return self.env['report'].get_action(
            self, 'account.report_statement_balances')
