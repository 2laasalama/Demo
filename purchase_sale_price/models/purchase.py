
from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    sale_price = fields.Float(
        "Sale price", compute="compute_sale_price_unit", store=False
    )
    po_margin = fields.Monetary(string="Margin", compute='_compute_margin')
    po_margin_percent = fields.Float(
        "Margin (%)", compute='_compute_margin', store=True, groups="base.group_user", digits=(16, 4))

    @api.depends('price_unit', 'product_id', 'product_uom')
    def compute_sale_price_unit(self):
        for rec in self:
            pricelist_obj = self.env['product.pricelist'].search([('is_main_pricelist', '=', True)], limit=1)
            if pricelist_obj:
                if rec.product_id:
                    product_context = dict(self.env.context,
                                           partner_id=rec.order_id.partner_id.id,
                                           date=rec.order_id.date_order,
                                           uom=rec.product_uom.id)
                    # Here variable price calculates the price of product after
                    # applying pricelist on it and rule_id is the id of the rule
                    # of pricelist which is applied on product
                    price, rule_id = pricelist_obj.with_context(
                        product_context).get_product_price_rule(
                        rec.product_id, rec.product_qty or 1.0,
                        rec.order_id.partner_id)
                    rec.sale_price = price
                else:
                    rec.sale_price = 0.0

            else:
                if rec.product_id.list_price:
                   rec.sale_price = rec.product_id.list_price
                else:
                    rec.sale_price = 0.0


    @api.depends('sale_price', 'price_unit')
    def _compute_margin(self):
        for line in self:
            if line.price_unit > 0:
                line.po_margin = line.sale_price - line.price_unit
                line.po_margin_percent = line.po_margin / (line.price_unit * 100)
            else:
                line.po_margin = line.sale_price - line.price_unit
                line.po_margin_percent = 0.0


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    is_main_pricelist = fields.Boolean("Main Pricelist", copy=False)