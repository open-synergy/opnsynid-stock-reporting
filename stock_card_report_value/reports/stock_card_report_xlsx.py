# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import models

from odoo.addons.report_xlsx_helper.report.report_xlsx_format import (
    FORMATS,
    XLS_HEADERS,
)

_logger = logging.getLogger(__name__)


class ReportStockCardReportXlsx(models.AbstractModel):
    _inherit = "report.stock_card_report.report_stock_card_report_xlsx"

    def _get_ws_params(self, wb, data, product):
        filter_template = {
            "1_date_from": {
                "header": {"value": "Date from"},
                "data": {
                    "value": self._render("date_from"),
                    "format": FORMATS["format_tcell_date_center"],
                },
            },
            "2_date_to": {
                "header": {"value": "Date to"},
                "data": {
                    "value": self._render("date_to"),
                    "format": FORMATS["format_tcell_date_center"],
                },
            },
            "3_location": {
                "header": {"value": "Location"},
                "data": {
                    "value": self._render("location"),
                    "format": FORMATS["format_tcell_center"],
                },
            },
        }
        initial_template = {
            "1_ref": {
                "data": {"value": "Initial", "format": FORMATS["format_tcell_center"]},
                "colspan": 3,
            },
            "2_initial_value": {
                "data": {
                    "value": self._render("initial_value"),
                    "format": FORMATS["format_tcell_amount_right"],
                }
            },
            "3_space": {
                "data": {
                    "value": "",
                    "format": FORMATS["format_tcell_center"],
                }
            },
            "4_space": {
                "data": {
                    "value": "",
                    "format": FORMATS["format_tcell_center"],
                }
            },
            "5_space": {
                "data": {
                    "value": "",
                    "format": FORMATS["format_tcell_center"],
                }
            },
            "6_balance": {
                "data": {
                    "value": self._render("balance"),
                    "format": FORMATS["format_tcell_amount_right"],
                }
            },
        }
        stock_card_template = {
            "1_date": {
                "header": {"value": "Date"},
                "data": {
                    "value": self._render("date"),
                    "format": FORMATS["format_tcell_date_left"],
                },
                "width": 25,
            },
            "2_reference": {
                "header": {"value": "Reference"},
                "data": {
                    "value": self._render("reference"),
                    "format": FORMATS["format_tcell_left"],
                },
                "width": 25,
            },
            "3_value": {
                "header": {"value": "Value"},
                "data": {"value": self._render("value")},
                "width": 25,
            },
            "4_cumulative_value": {
                "header": {"value": "Cumulative Value"},
                "data": {"value": self._render("cumulative_value")},
                "width": 25,
            },
            "5_unit_cost": {
                "header": {"value": "Unit Cost"},
                "data": {"value": self._render("unit_cost")},
                "width": 25,
            },
            "6_input": {
                "header": {"value": "In"},
                "data": {"value": self._render("input")},
                "width": 25,
            },
            "7_output": {
                "header": {"value": "Out"},
                "data": {"value": self._render("output")},
                "width": 25,
            },
            "8_balance": {
                "header": {"value": "Balance"},
                "data": {"value": self._render("balance")},
                "width": 25,
            },
        }

        ws_params = {
            "ws_name": product.name,
            "generate_ws_method": "_stock_card_report",
            "title": "Stock Card - {}".format(product.name),
            "wanted_list_filter": [k for k in sorted(filter_template.keys())],
            "col_specs_filter": filter_template,
            "wanted_list_initial": [k for k in sorted(initial_template.keys())],
            "col_specs_initial": initial_template,
            "wanted_list": [k for k in sorted(stock_card_template.keys())],
            "col_specs": stock_card_template,
        }
        return [ws_params]

    def _stock_card_report(self, wb, ws, ws_params, data, objects, product):
        ws.set_portrait()
        ws.fit_to_pages(1, 0)
        ws.set_header(XLS_HEADERS["xls_headers"]["standard"])
        ws.set_footer(XLS_HEADERS["xls_footers"]["standard"])
        self._set_column_width(ws, ws_params)
        # Title
        row_pos = 0
        row_pos = self._write_ws_title(ws, row_pos, ws_params, True)
        # Filter Table
        row_pos = self._write_line(
            ws,
            row_pos,
            ws_params,
            col_specs_section="header",
            default_format=FORMATS["format_theader_blue_center"],
            col_specs="col_specs_filter",
            wanted_list="wanted_list_filter",
        )
        row_pos = self._write_line(
            ws,
            row_pos,
            ws_params,
            col_specs_section="data",
            render_space={
                "date_from": objects.date_from or "",
                "date_to": objects.date_to or "",
                "location": objects.location_id.display_name or "",
            },
            col_specs="col_specs_filter",
            wanted_list="wanted_list_filter",
        )
        row_pos += 1
        # Stock Card Table
        row_pos = self._write_line(
            ws,
            row_pos,
            ws_params,
            col_specs_section="header",
            default_format=FORMATS["format_theader_blue_center"],
        )
        ws.freeze_panes(row_pos, 0)
        balance = objects._get_initial(
            objects.results.filtered(lambda l: l.product_id == product and l.is_initial)
        )
        cumulative_value = objects._get_initial_value(
            objects.results.filtered(lambda l: l.product_id == product and l.is_initial)
        )
        row_pos = self._write_line(
            ws,
            row_pos,
            ws_params,
            col_specs_section="data",
            render_space={
                "balance": balance,
                "initial_value": cumulative_value,
            },
            col_specs="col_specs_initial",
            wanted_list="wanted_list_initial",
        )
        product_lines = objects.results.filtered(
            lambda l: l.product_id == product and not l.is_initial
        )
        for line in product_lines:
            balance += line.product_in - line.product_out
            cumulative_value += line.value
            unit_cost = line.value / abs(line.product_in - line.product_out)
            row_pos = self._write_line(
                ws,
                row_pos,
                ws_params,
                col_specs_section="data",
                render_space={
                    "date": line.date or "",
                    "reference": line.display_name or "",
                    "value": line.value or 0,
                    "cumulative_value": cumulative_value,
                    "unit_cost": unit_cost,
                    "input": line.product_in or 0,
                    "output": line.product_out or 0,
                    "balance": balance,
                },
                default_format=FORMATS["format_tcell_amount_right"],
            )
