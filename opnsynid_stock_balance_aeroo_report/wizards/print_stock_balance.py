# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from openerp import api, fields, models
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class PrintStockBalance(models.TransientModel):
    _name = "stock.print_stock_balance"
    _description = "Print Stock Balance"

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self.env.user.company_id.id,
    )
    date_start = fields.Datetime(
        string="Date Start",
    )
    date_end = fields.Datetime(
        string="Date End",
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    location_ids = fields.Many2many(
        string="Locations",
        comodel_name="stock.location",
        relation="rel_print_stock_balance_2_location",
        column1="wizard_id",
        column2="location_id",
        required=True,
        domain=[
            ("usage", "!=", "view"),
        ],
    )
    product_ids = fields.Many2many(
        string="Products",
        comodel_name="product.product",
        relation="rel_print_stock_balance_2_product",
        column1="wizard_id",
        column2="product_id",
        required=True,
        domain=[
            ("type", "=", "product"),
        ],
    )
    output_format = fields.Selection(
        string="Output Format",
        required=True,
        selection=[("xls", "XLS"), ("ods", "ODS")],
        default="ods",
    )

    @api.constrains("date_start", "date_end")
    def _check_date(self):
        strWarning = _("Date start must be greater than date end")
        if self.date_start and self.date_end:
            if self.date_start > self.date_end:
                raise UserError(strWarning)

    @api.multi
    def action_print(self):
        self.ensure_one()

        datas = {}
        output_format = ""

        datas["form"] = self.read()[0]

        if self.output_format == "xls":
            output_format = "stock_balance_xls"
        elif self.output_format == "ods":
            output_format = "stock_balance_ods"

        return {
            "type": "ir.actions.report.xml",
            "report_name": output_format,
            "datas": datas,
        }
