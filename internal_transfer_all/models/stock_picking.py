import logging
from odoo import fields, models, _, api

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_all_transfer(self):
        for rec in self:
            all_products = []
            rec.move_ids_without_package.unlink()
            if rec.picking_type_code == 'internal':
                quants = self.env['stock.quant'].search(
                    [('quantity', '>', 0), ('location_id', '=', rec.location_id.id)])

                for pro in quants:
                    if pro.product_id:
                        lots_obj = self.env['stock.production.lot'].search(
                            [('product_id', '=', pro.product_id.id)]).ids
                        all_products.append((0, 0, {'product_id': pro.product_id.id,
                                                    'name': pro.product_id.name,
                                                    'description_picking': pro.product_id.name,
                                                    'product_uom_qty': pro.quantity,
                                                    'product_uom': pro.product_id.uom_id.id,
                                                    'location_id': pro.location_id.id,
                                                    'location_dest_id': rec.location_dest_id.id,
                                                    'lot_ids': [(6, 0, lots_obj)]}))
                rec.write({'move_ids_without_package': all_products})
            else:
                rec.write({'move_ids_without_package': all_products})
