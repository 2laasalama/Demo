# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    product_no = fields.Char(string="رقم الصنف")
    oem_no = fields.Char(string="OEM.NO")
    name_english = fields.Char('وصف الصنف باللغه الانجليزيه')
    mo_company_no = fields.Char(string="رقم التصنيع او رقم الشركه المصنعه")
    # -----------------------------------------------------------------------
    product_group_no = fields.Many2one('product.group.no', string="رقم مجموعه الصنف")
    year = fields.Many2one('product.year', 'السنه')
    color = fields.Many2one('product.color', 'اللون')
    direction = fields.Many2one('product.direction', 'الاتجاه')
    size = fields.Many2one('product.size', 'المقاس')
    return_duration = fields.Many2one('product.return.duration', 'فتره ارتجاع الصنف')
    mo_company = fields.Many2one('product.mo.company', 'الشركه المصنعه او الماركه')
    creation_country = fields.Many2one('product.creation.country', 'بلد المنشأ')
    product_description_models = fields.Char(string='وصف الصنف')

    def _select(self):
        return super(PurchaseReport,
                     self)._select() + ", l.product_no as product_no, l.oem_no as oem_no, l.name_english as name_english, l.mo_company_no as mo_company_no,l.product_group_no as product_group_no,l.year as year,l.color as color, l.direction as direction, l.size as size, l.return_duration as return_duration , l.mo_company as mo_company, l.creation_country as creation_country,l.product_description_models as product_description_models"

    def _group_by(self):
        return super(PurchaseReport,
                     self)._group_by() + ", l.product_no, l.oem_no, l.name_english, l.mo_company_no,l.product_group_no,l.year,l.color, l.direction, l.size, l.return_duration , l.mo_company, l.creation_country,l.product_description_models"
