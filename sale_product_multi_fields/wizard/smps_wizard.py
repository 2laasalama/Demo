# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models, _
from odoo.exceptions import UserError


class SmpsAdvWizard(models.TransientModel):
    _name = "smps.adv.wizard"
    _description = "Sale Order Multi Product Selection Advanced Wizard"

    product_ids = fields.One2many(
        "smps.adv.wizard.product.line",
        "smps_adv_wizard_id",
        string="Products"
    )
    product_attr_ids = fields.Many2many(
        "product.attribute.value",
        string="Attributes",
        ondelete="cascade"
    )
    specific_product_ids = fields.One2many(
        "smps.adv.wizard.product.line.specific",
        "smps_adv_wizard_id_specific",
        string="Specific Products"
    )

    def sh_smps_adv_select_btn(self):
        if(
            self and
            self.product_ids and
            self.env.context.get('sh_smps_adv_so_id', False)
        ):
            order_id = self.env.context.get('sh_smps_adv_so_id')
            sale_order_line_obj = self.env['sale.order.line']
            for rec in self.product_ids:
                if rec.uom_id:
                    created_sol = sale_order_line_obj.create(
                        {
                            'product_id': rec.product_id.id,
                            'order_id': order_id,
                            'product_uom': rec.uom_id.id,
                            'product_uom_qty': rec.qty
                        }
                    )
                    if created_sol:
                        created_sol.product_id_change()

    def sh_smps_adv_select_specific_btn(self):
        if(
            self and
            self.specific_product_ids and
            self.env.context.get('sh_smps_adv_so_id', False)
        ):
            order_id = self.env.context.get('sh_smps_adv_so_id')
            sale_order_line_obj = self.env['sale.order.line']
            for rec in self.specific_product_ids:
                if rec.uom_id:
                    created_sol = sale_order_line_obj.create(
                        {
                            'product_id': rec.product_id.id,
                            'order_id': order_id,
                            'product_uom': rec.uom_id.id,
                            'product_uom_qty': rec.qty
                        }
                    )
                    if created_sol:
                        created_sol.product_id_change()

    def reset_filter(self):
        if self:
            rec_dic = self.read()[0]
            if rec_dic:
                reset_vals = {}
                for k, v in rec_dic.items():
                    if "x_" in k and v:
                        reset_vals.update({k: False})
                reset_vals.update({'product_attr_ids': None})
                self.product_attr_ids = None
                self.write(reset_vals)

                return {
                    'name': 'Select Products Advance',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'smps.adv.wizard',
                    'view_id': False,
                    'type': 'ir.actions.act_window',
                    'res_id': self.id,
                    'target': 'new',
                    }

    def reset_list(self):
        if self:
            self.product_ids = None
            return {
                'name': 'Select Products Advance',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'smps.adv.wizard',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'res_id': self.id,
                'target': 'new',
                }

    def reset_specific(self):
        if self:
            self.specific_product_ids = None
            return {
                'name': 'Select Products Advance',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'smps.adv.wizard',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'res_id': self.id,
                'target': 'new',
                }

    def filter_products(self):
        if self:
            rec_dic = self.read()[0]
            domain = []
            if rec_dic:
                for k, v in rec_dic.items():
                    if "x_" in k and "x_opt_" not in k:
                        if v:
                            pro_field_name = k.split("_", 1)[1]
                            smps_field_name = "x_opt_" + pro_field_name
                            if rec_dic.get(smps_field_name, False):
                                opt = rec_dic.get(smps_field_name, False)
                                domain.append((pro_field_name, opt, v))
                            else:
                                # if attribute fields found
                                if "x_attr_" in k:
                                    domain.append((
                                        'product_template_attribute_value_ids', 'in', v[0]
                                    ))
                                # if boolean fields found
                                else:
                                # check whether it's a selection or boolean fields or not
                                    smps_model_id = self.env['ir.model'].sudo().search([
                                                    ('model', '=', 'smps.adv.wizard')
                                                    ], limit=1)
                                    if smps_model_id:
                                        search_field = self.env['ir.model.fields'].sudo().search(
                                            [
                                                ('name', '=', '' + k),
                                                ('model_id', '=', smps_model_id.id),
                                            ], limit=1)
                                        if search_field:
                                            if search_field.ttype in ['selection', 'boolean']:
                                                domain.append(
                                                    (pro_field_name, '=', v)
                                                )
                                            else:
                                                domain.append(
                                                    (pro_field_name, '=', v[0])
                                                )
                                        else:
                                            raise UserError(
                                                _('Field not Found - ' + k)
                                            )

                                    else:
                                        raise UserError(
                                            _('Model not Found - smps.adv.wizard')
                                        )

                    if "product_attr_ids" in k and v:
                        for attr_id in v:
                            domain.append(
                                ('product_template_attribute_value_ids', 'in', attr_id)
                            )

                if domain:
                    domain.append(('sale_ok', '=', True))
                    domain.append(('qty_available', '>', 0))
                    search_products = self.env['product.product'].search(domain)
                    if search_products:
                        result = []
                        smps_adv_wizard_product_line_obj = self.env['smps.adv.wizard.product.line']
                        for product in search_products:
                            line_vals = {
                                    'product_id': product.id,
                                }
                            created_line = smps_adv_wizard_product_line_obj.create(line_vals)
                            if created_line:
                                result.append(created_line.id)

                        self.product_ids = None
                        self.product_ids = [(6, 0, result)]
                    else:
                        self.product_ids = None

                return {
                    'name': 'Select Products Advance',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'smps.adv.wizard',
                    'view_id': False,
                    'type': 'ir.actions.act_window',
                    'res_id': self.id,
                    'target': 'new',
                    }


class SmpsAdvWizardProductLine(models.TransientModel):
    _name = 'smps.adv.wizard.product.line'
    _description = "SO Multi Product Selection Advanced Wizard Product Line"

    smps_adv_wizard_id = fields.Many2one(
        'smps.adv.wizard',
        string='Searched Product'
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product'
    )
    default_code = fields.Char(
        related="product_id.default_code",
        string='Internal Reference'
    )
    sale_price = fields.Float(
        related="product_id.list_price",
        string="Sale Price"
    )
    uom_id = fields.Many2one(
        "uom.uom",
        related="product_id.uom_id",
        string="Unit of Measure"
    )
    qty = fields.Float(string="Qty", default=1.0)

    def add_to_specific(self):
        if self and self.product_id:
            smps_adv_wizard_product_line_specific_obj = self.env['smps.adv.wizard.product.line.specific']
            line_vals = {
                    'product_id': self.product_id.id,
                    'qty': self.qty,
                    'smps_adv_wizard_id_specific': self.smps_adv_wizard_id.id
                }
            smps_adv_wizard_product_line_specific_obj.create(line_vals)
            res_id = self.smps_adv_wizard_id.id
            self.unlink()
            return {
                'name': 'Select Products Advance',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'smps.adv.wizard',
                'view_id': False,
                'type': 'ir.actions.act_window',
                'res_id': res_id,
                'target': 'new',
                }


class SmpsAdvWizardProductLineSpecific(models.TransientModel):
    _name = 'smps.adv.wizard.product.line.specific'
    _description = "SO Multi Product Selection Advanced Wizard Product Line Specific"

    smps_adv_wizard_id_specific = fields.Many2one(
        'smps.adv.wizard', string='Searched Product')
    product_id = fields.Many2one(
        'product.product',
        string='Product'
    )
    default_code = fields.Char(
        related="product_id.default_code",
        string='Internal Reference'
    )
    sale_price = fields.Float(
        related="product_id.list_price",
        string="Sale Price"
    )
    uom_id = fields.Many2one(
        "uom.uom",
        related="product_id.uom_id",
        string="Unit of Measure"
    )
    qty = fields.Float(string="Qty", default=1.0)
