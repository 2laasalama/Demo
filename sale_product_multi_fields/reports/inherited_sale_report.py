# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

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

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['product_no'] = ", l.product_no as product_no"
        fields['oem_no'] = ", l.oem_no as oem_no"
        fields['name_english'] = ", l.name_english as name_english"
        fields['mo_company_no'] = ", l.mo_company_no as mo_company_no"
        fields['product_group_no'] = ",l.product_group_no as product_group_no"
        fields['year'] = ",l.year as year"
        fields['color"'] = ",l.color as color"
        fields['direction'] = ", l.direction as direction"
        fields['size'] = ", l.size as size"
        fields['return_duration'] = ", l.return_duration as return_duration"
        fields['mo_company'] = " , l.mo_company as mo_company"
        fields['creation_country'] = ", l.creation_country as creation_country"
        fields['product_description_models'] = ",l.product_description_models as product_description_models"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
    def _group_by_sale(self, groupby=''):
        return super(SaleReport,
                     self)._group_by_sale(groupby) + ", l.product_no, l.OEM_no, l.name_english, l.mo_company_no,l.product_group_no,l.year,l.color, l.direction, l.size, l.return_duration , l.mo_company, l.creation_country,l.product_description_models"
