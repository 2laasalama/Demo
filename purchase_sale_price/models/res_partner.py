# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'
    commercial_register_ids = fields.Many2many('partner.commercial.register','commercial_register1','commercial_register2','commercial_register_rel', string='السجل التجاري')

class PartnerCommercialRegister(models.Model):
    _name = 'partner.commercial.register'
    _rec_name = 'name'

    name = fields.Char(required=1,string='السجل التجاري')


