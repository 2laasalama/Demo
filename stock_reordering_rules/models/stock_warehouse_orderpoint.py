# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    @api.constrains('product_min_qty', 'product_max_qty')
    def _check_product_qty(self):
        if self.product_min_qty < 0:
            raise ValidationError("Min Quantity should not be less than 0")
        if self.product_max_qty < 0:
            raise ValidationError("Max Quantity should not be less than 0")
