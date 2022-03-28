# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_no = fields.Char(string="رقم الصنف", copy=False)
    OEM_no = fields.Char(string="OEM.NO", copy=False)
    name_english = fields.Char('وصف الصنف باللغه الانجليزيه', translate=True)
    mo_company_no = fields.Char(string="رقم التصنيع او رقم الشركه المصنعه")
    # -----------------------------------------------------------------------
    product_group_no = fields.Many2one('product.group.no', string="رقم مجموعه الصنف")
    year = fields.Many2one('product.year', 'السنه')
    alternative_product_ids = fields.Many2many('product.product', 'alt_product_col1', 'alt_product_col1',
                                               'alt_product_rel1', string='الاصناف البديله')
    color = fields.Many2one('product.color', 'اللون')
    direction = fields.Many2one('product.direction', 'الاتجاه')
    size = fields.Many2one('product.size', 'المقاس')
    return_duration = fields.Many2one('product.return.duration', 'فتره ارتجاع الصنف')
    mo_company = fields.Many2one('product.mo.company', 'الشركه المصنعه او الماركه')
    creation_country = fields.Many2one('product.creation.country', 'بلد المنشأ')

    company = fields.Many2one('res.company')

    product_description_model_ids = fields.One2many('product.description.model.year', 'product_id',
                                                    string='وصف الصنف')
    product_description_models = fields.Char(string='وصف الصنف', compute="compute_product_description_models",
                                             store=True)

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     if operator in ('ilike', 'like', '=', '=like', '=ilike'):
    #         args = expression.AND([
    #             args or [],
    #             ['|', '|', '|', '|', '|', '|', '|', '|', '|', ('name', operator, name), ('product_no', operator, name),
    #              ('OEM_no', operator, name), ('name_english', operator, name),
    #              ('mo_company_no', operator, name), ('product_description_models', operator, name),
    #              ('company.name', operator, name), ('creation_country.name', operator, name),
    #              ('mo_company.name', operator, name), ('return_duration.name', operator, name),
    #              ('size.name', operator, name), ('direction.name', operator, name),
    #              ('product_group_no.name', operator, name), ('year.name', operator, name),
    #              ('color.name', operator, name), ('product_description_models', operator, name)]
    #         ])
    #     return super(ProductTemplate, self)._name_search(name, args=args, operator=operator, limit=limit,
    #                                                      name_get_uid=name_get_uid)

    @api.depends('product_description_model_ids')
    def compute_product_description_models(self):
        for rec in self:
            if rec.product_description_model_ids:
                product_description_models = ','.join([p.name + p.year.name for p in rec.product_description_model_ids])
            else:
                product_description_models = ''
            rec.product_description_models = product_description_models

class ProductDescriptionModelYear(models.Model):
    _name = 'product.description.model.year'
    _rec_name = 'name'

    product_id = fields.Many2one('product.product', string='Product')
    name = fields.Char(required=1)
    # year = fields.Char(required=1)
    year = fields.Many2one('product.year', 'السنه', required=1)

    alternative_product_id = fields.Many2one('product.product', string='الصنف البديل')
    alternative_year = fields.Many2one('product.year', 'السنه')

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []
        domain = args + ['|', ('year.name', operator, name), ('name', operator, name)]
        return self._search(domain, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, '%s [%s]' % (field.name, field.year.name)))
        return res


class ProductYear(models.Model):
    _name = 'product.year'
    _rec_name = 'name'

    name = fields.Char(string="السنه", required=1)


class ProductGroupNo(models.Model):
    _name = 'product.group.no'
    _rec_name = 'name'

    name = fields.Char(string="رقم مجموعه الصنف", required=1)


class ProductColor(models.Model):
    _name = 'product.color'
    _rec_name = 'name'

    name = fields.Char(string="اللون", required=1)


class ProductDirection(models.Model):
    _name = 'product.direction'
    _rec_name = 'name'

    name = fields.Char(string="الاتجاه", required=1)


class ProductSize(models.Model):
    _name = 'product.size'
    _rec_name = 'name'

    name = fields.Char(string="المقاس", required=1)


class ProductReturnDuration(models.Model):
    _name = 'product.return.duration'
    _rec_name = 'name'

    name = fields.Char(string="فتره ارتجاع الصنف", required=1)


class ProductMoCompany(models.Model):
    _name = 'product.mo.company'
    _rec_name = 'name'

    name = fields.Char(string="الشركه المصنعه او الماركه", required=1)


class ProductCreationCountry(models.Model):
    _name = 'product.creation.country'
    _rec_name = 'name'

    name = fields.Char(string="بلد المنشأ", required=1)
