from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_no = fields.Char(string="رقم الصنف", store=True, related="product_id.product_no")
    oem_no = fields.Char(string="OEM.NO", store=True, related="product_id.OEM_no")
    name_english = fields.Char('وصف الصنف باللغه الانجليزيه', translate=True, store=True,
                               related="product_id.name_english")
    mo_company_no = fields.Char(string="رقم التصنيع او رقم الشركه المصنعه", store=True,
                                related="product_id.mo_company_no")
    # -----------------------------------------------------------------------
    product_group_no = fields.Many2one('product.group.no', string="رقم مجموعه الصنف", store=True,
                                       related="product_id.product_group_no")
    year = fields.Many2one('product.year', string='السنه', store=True, related="product_id.year")
    color = fields.Many2one('product.color', 'اللون', store=True, related="product_id.color")
    direction = fields.Many2one('product.direction', 'الاتجاه', store=True, related="product_id.direction")
    size = fields.Many2one('product.size', 'المقاس', store=True, related="product_id.size")
    return_duration = fields.Many2one('product.return.duration', string='فتره ارتجاع الصنف', store=True,
                                      related="product_id.return_duration")
    mo_company = fields.Many2one('product.mo.company', 'الشركه المصنعه او الماركه', store=True,
                                 related="product_id.mo_company")
    creation_country = fields.Many2one('product.creation.country', string='بلد المنشأ', store=True,
                                       related="product_id.creation_country")
    product_description_models = fields.Char(string='وصف الصنف', store=True,
                                             related="product_id.product_description_models")


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    product_no = fields.Char(string="رقم الصنف", store=True, related="product_id.product_no")
    oem_no = fields.Char(string="OEM.NO", store=True, related="product_id.OEM_no")
    name_english = fields.Char('وصف الصنف باللغه الانجليزيه', translate=True, store=True,
                               related="product_id.name_english")
    mo_company_no = fields.Char(string="رقم التصنيع او رقم الشركه المصنعه", store=True,
                                related="product_id.mo_company_no")
    # -----------------------------------------------------------------------
    product_group_no = fields.Many2one('product.group.no', string="رقم مجموعه الصنف", store=True,
                                       related="product_id.product_group_no")
    year = fields.Many2one('product.year', string='السنه', store=True, related="product_id.year")
    color = fields.Many2one('product.color', 'اللون', store=True, related="product_id.color")
    direction = fields.Many2one('product.direction', 'الاتجاه', store=True, related="product_id.direction")
    size = fields.Many2one('product.size', 'المقاس', store=True, related="product_id.size")
    return_duration = fields.Many2one('product.return.duration', string='فتره ارتجاع الصنف', store=True,
                                      related="product_id.return_duration")
    mo_company = fields.Many2one('product.mo.company', 'الشركه المصنعه او الماركه', store=True,
                                 related="product_id.mo_company")
    creation_country = fields.Many2one('product.creation.country', string='بلد المنشأ', store=True,
                                       related="product_id.creation_country")
    product_description_models = fields.Char(string='وصف الصنف', store=True,
                                             related="product_id.product_description_models")


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_no = fields.Char(string="رقم الصنف", store=True, related="product_id.product_no")
    oem_no = fields.Char(string="OEM.NO", store=True, related="product_id.OEM_no")
    name_english = fields.Char('وصف الصنف باللغه الانجليزيه', translate=True, store=True,
                               related="product_id.name_english")
    mo_company_no = fields.Char(string="رقم التصنيع او رقم الشركه المصنعه", store=True,
                                related="product_id.mo_company_no")
    # -----------------------------------------------------------------------
    product_group_no = fields.Many2one('product.group.no', string="رقم مجموعه الصنف", store=True,
                                       related="product_id.product_group_no")
    year = fields.Many2one('product.year', string='السنه', store=True, related="product_id.year")
    color = fields.Many2one('product.color', 'اللون', store=True, related="product_id.color")
    direction = fields.Many2one('product.direction', 'الاتجاه', store=True, related="product_id.direction")
    size = fields.Many2one('product.size', 'المقاس', store=True, related="product_id.size")
    return_duration = fields.Many2one('product.return.duration', string='فتره ارتجاع الصنف', store=True,
                                      related="product_id.return_duration")
    mo_company = fields.Many2one('product.mo.company', 'الشركه المصنعه او الماركه', store=True,
                                 related="product_id.mo_company")
    creation_country = fields.Many2one('product.creation.country', string='بلد المنشأ', store=True,
                                       related="product_id.creation_country")
    product_description_models = fields.Char(string='وصف الصنف', store=True,
                                             related="product_id.product_description_models")


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    product_no = fields.Char(string="رقم الصنف", store=True, related="product_id.product_no")
    oem_no = fields.Char(string="OEM.NO", store=True, related="product_id.OEM_no")
    name_english = fields.Char('وصف الصنف باللغه الانجليزيه', translate=True, store=True,
                               related="product_id.name_english")
    mo_company_no = fields.Char(string="رقم التصنيع او رقم الشركه المصنعه", store=True,
                                related="product_id.mo_company_no")
    # -----------------------------------------------------------------------
    product_group_no = fields.Many2one('product.group.no', string="رقم مجموعه الصنف", store=True,
                                       related="product_id.product_group_no")
    year = fields.Many2one('product.year', string='السنه', store=True, related="product_id.year")
    color = fields.Many2one('product.color', 'اللون', store=True, related="product_id.color")
    direction = fields.Many2one('product.direction', 'الاتجاه', store=True, related="product_id.direction")
    size = fields.Many2one('product.size', 'المقاس', store=True, related="product_id.size")
    return_duration = fields.Many2one('product.return.duration', string='فتره ارتجاع الصنف', store=True,
                                      related="product_id.return_duration")
    mo_company = fields.Many2one('product.mo.company', 'الشركه المصنعه او الماركه', store=True,
                                 related="product_id.mo_company")
    creation_country = fields.Many2one('product.creation.country', string='بلد المنشأ', store=True,
                                       related="product_id.creation_country")
    product_description_models = fields.Char(string='وصف الصنف', store=True,
                                             related="product_id.product_description_models")
