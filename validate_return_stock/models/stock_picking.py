import logging
from odoo import fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_return = fields.Boolean(compute="_compute_is_return")

    def _compute_is_return(self):
        for picking in self:
            if any(x.origin_returned_move_id for x in picking.move_lines):
                picking.is_return = True
            else:
                picking.is_return = False

    def button_validate(self):
        for picking in self:
            if picking.is_return == True and not self.env.user.has_group('stock.group_stock_manager'):
                    raise ValidationError(_('Stock Manager only how can validate returned transfer.'))
        return super(StockPicking, self).button_validate()

