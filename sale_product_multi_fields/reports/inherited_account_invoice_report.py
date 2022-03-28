# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

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
        return super(AccountInvoiceReport,
                     self)._select() + ", line.product_no, line.oem_no, line.name_english, line.mo_company_no,line.product_group_no,line.year,line.color, line.direction, line.size, line.return_duration , line.mo_company, line.creation_country,line.product_description_models"
