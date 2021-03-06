# -*- coding: utf-8 -*-
import openerp
from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp import SUPERUSER_ID

class website_sale(openerp.addons.website_sale.controllers.main.website_sale):

    @http.route(['/shop/payment'], type='http', auth="public", website=True, multilang=True)
    def payment(self, **post):
        cr, uid, context = request.cr, request.uid, request.context
        order = self.get_order()
        carrier_id = post.get('carrier_id')
        if carrier_id:
            carrier_id = int(carrier_id)
        if order:
            request.registry['sale.order']._check_carrier_quotation(cr, uid, order, force_carrier_id=carrier_id, context=context)
            if carrier_id:
                return request.redirect("/shop/payment")

        res = super(website_sale, self).payment(**post)
        return res
