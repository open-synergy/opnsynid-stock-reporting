# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields
from openerp.tools import drop_view_if_exists


class StockMoveHistory(models.Model):
    _name = "stock.stock_move_history"
    _description = "Stock Move History"
    _auto = False

    name = fields.Char(
        string="Description",
    )
    date = fields.Datetime(
        string="Date",
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
    )
    product_id = fields.Many2one(
        string="Product",
        comodel_name="product.product",
    )
    location_id = fields.Many2one(
        string="Location",
        comodel_name="stock.location",
    )
    picking_id = fields.Many2one(
        string="Picking",
        comodel_name="stock.picking",
    )
    picking_type_id = fields.Many2one(
        string="Picking Type",
        comodel_name="stock.picking.type",
    )
    product_qty = fields.Float(
        string="Product Qty",
    )
    product_uom_id = fields.Many2one(
        string="Product UoM",
        comodel_name="product.uom",
    )
    move_qty = fields.Float(
        string="Move Qty",
    )
    move_uom_id = fields.Many2one(
        string="Move UoM",
        comodel_name="product.uom",
    )

    def init(self, cr):
        drop_view_if_exists(cr, "stock_stock_move_history")
        strSQL = """
                    CREATE OR REPLACE VIEW stock_stock_move_history AS (
                        SELECT  *
                        FROM    stock_stock_move_in AS a
                        UNION
                        SELECT  *
                        FROM    stock_stock_move_out AS b
                    )
                    """
        cr.execute(strSQL)
