# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Balance Aeroo Report",
    "version": "8.0.1.0.0",
    "category": "Stock",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "opnsynid_stock_card_aeroo_report",
    ],
    "data": [
        "reports/stock_balance_reports.xml",
        "wizards/print_stock_balance_views.xml",
    ],
}
