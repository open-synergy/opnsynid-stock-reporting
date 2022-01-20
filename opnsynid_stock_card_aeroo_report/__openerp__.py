# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Card Aeroo Report",
    "version": "8.0.2.0.0",
    "category": "Stock",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "report_aeroo",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "reports/stock_card_reports.xml",
        "wizards/print_stock_card_views.xml",
    ],
}
