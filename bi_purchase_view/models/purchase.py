# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.tools.translate import _

#============================================
#class:PurchaseOrderLineView
#description:it will show the purchase order line details
#============================================

class BiPurchaseOrderLineView(models.Model):
	_name = "bi.purchase.order.line.view"
	_description = "it will show the purchase order line details"
	_auto = False

	name = fields.Char('Name',readonly=True)
	date_order = fields.Datetime('Order Date', readonly=True)
	partner_id = fields.Many2one('res.partner', 'Supplier', readonly=True)
	product_uom = fields.Many2one('product.uom', 'UOM', readonly=True)
	company_id = fields.Many2one('res.company',string='Company',readonly=True)
	qty_received = fields.Float( 'Recieved Qty', readonly=True)
	qty_invoiced = fields.Float('Invoice Qty', readonly=True)
	product_id = fields.Many2one('product.product', 'Product', readonly=True)
	product_qty = fields.Float('Quantity', readonly=True)
	price_unit = fields.Float('Unit Price', readonly=True)
	price_subtotal = fields.Float('Price Subtotal', readonly=True)
	#============================================
	#class:BiPurchaseOrderLineView
	#method:init
	#description:"it will show the purchase order line details"
	#============================================
	def init(self):
		tools.drop_view_if_exists(self._cr, 'bi_purchase_order_line_view')
		self._cr.execute("""
			CREATE VIEW bi_purchase_order_line_view AS (
				select
					po.name,
					po.date_order,
					po.partner_id,
					pol.id,
					po.company_id,
					pol.product_uom,
					pol.price_unit,
					pol.product_qty,
					pol.product_id,
					pol.price_subtotal,
					pol.qty_received,
					pol.qty_invoiced
		from
					"purchase_order" po
				join
					"purchase_order_line" pol
				on
					(pol.order_id = po.id)
			)""")
   