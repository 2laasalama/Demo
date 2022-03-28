
{
    "name": "Sale Price in purchase order",
    "summary": "Add sale price in purchase order",
    "version": "15",
    "category": "Purchase",
    "author": "Doaa",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "purchase",
        "product"
    ],
    "data": [
        'security/ir.model.access.csv',
        "views/sale_price_purchase.xml",
        'views/res_partner_view.xml',
    ],
}
