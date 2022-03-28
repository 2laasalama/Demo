# -*- coding: utf-8 -*-
{
    "name": "Sales Products Multi fields",
    "author": "Doaa khaled",
    "category": "Sales",
    "version": "14",
    "depends": ["sale_management", "account", "purchase", "stock", "stock_account"],
    "data": [
        "security/ir.model.access.csv",
        "views/settings_view.xml",
        "wizard/smps_wizard.xml",
        "views/sale_view.xml",
        "views/product_views.xml",
        "views/view.xml",
        "reports/analysis_reports.xml",
        "reports/inherited_stock_views.xml",
    ],
    "auto_install": False,
    "installable": True,

}
