# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    cashier_id = fields.Many2one('hr.employee', string='Cashier', tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

