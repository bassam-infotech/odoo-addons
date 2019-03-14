# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.tools.translate import _

#============================================
#class:BiSaleOrderLineView
#description:It will show the sale order reports
#============================================

class BiSaleOrderLineView(models.Model):

	_name = "bi.sale.order.line.view"
	_auto = False
	_description = "Sales order online view"
	_rec_name = 'id'



	
	name=fields.Char('Name', readonly=True)
	# name=fields.Char(string='Order No', readonly=True)
	company_id = fields.Many2one('res.company', string='Company',readonly=True)
	date_order = fields.Datetime('Order Date',readonly=True)
	partner_id = fields.Many2one('res.partner', string='Customer',readonly=True)
	product_id = fields.Many2one('product.product', string = 'Product' , readonly=True )
	product_uom_qty = fields.Float(string = 'Product Quantity',readonly=True)
	product_uom = fields.Many2one('product.uom',string = 'Unit of Measure', readonly=True)
	price_unit = fields.Float('Unit Price', readonly=True)
	price_tax = fields.Float('Price Tax', readonly=True)
	price_subtotal = fields.Float('Price Subtotal', readonly=True)
	qty_delivered = fields.Float('Delivered' , readonly=True)
	qty_invoiced = fields.Float('Invoiced', readonly=True)
	#============================================
	#class:BiSaleOrderLineView
	#method: init()
	#description:It will show the sale order reports
	#============================================

  
	def init(self):
		tools.drop_view_if_exists(self._cr, 'bi_sale_order_line_view')
		self._cr.execute("""
			CREATE VIEW bi_sale_order_line_view AS (
				select
				
					so.name,
					sol.id,
					so.company_id,
					so.date_order,
					so.partner_id,
					sol.product_id,
					sol.product_uom,
					sol.product_uom_qty,
					sol.price_unit,
					sol.price_tax,
					sol.price_subtotal,
					sol.qty_delivered,
					sol.qty_invoiced

			   
				from
					"sale_order" so
				join
					"sale_order_line" sol
				on
					(sol.order_id = so.id)
				-- where
				-- 	state != 'draft'
			   
			)""")


	
