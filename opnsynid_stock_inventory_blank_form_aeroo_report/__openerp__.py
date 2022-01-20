# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock Inventory Blank Form Aeroo Report",
    "version": "8.0.1.0.0",
    "summary": "Adds Stock Inventory Blank Form Report",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "category": "Stock",
    "depends": ["stock", "report_aeroo"],
    "data": [
        "reports/stock_inventory_blank_form.xml",
        "views/stock_inventory_view.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
