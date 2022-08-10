# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ebay_logs_added(models.Model):
    _inherit = 'product.template'

    def push_product_ebay(self):
        for product in self:
            if product.ebay_listing_status != 'Active':
                item_dict = product._get_item_dict()
                _logger.warning(item_dict)

        res = super(ebay_logs_added, self).push_product_ebay()
        return res


    @api.model
    def ebay_execute(self, verb, data=None, list_nodes=[], verb_attrs=None, files=None):
        _logger.warning("verb")
        _logger.warning(verb)
        _logger.warning("data")
        _logger.warning(data)
        _logger.warning("list nodes")
        _logger.warning(list_nodes)
        _logger.warning("verb_attrs")
        _logger.warning(verb_attrs)

        res = super(ebay_logs_added, self).ebay_execute()
        return res

    @api.model
    def _process_order(self, order):
        for transaction in order['TransactionArray']['Transaction']:
            _logger.warning(transaction)

        res = super(ebay_logs_added, self)._process_order()
        return res

    def _synchronize_orders_ranged(self, date_from, date_to, page=1):
        call_data = {
            'ModTimeFrom': str(date_from),
            'ModTimeTo': str(date_to),
            'Pagination': {'EntriesPerPage': 100,  # max allowed by ebay
                           'PageNumber': page,
                           }
        }
        try:
            response = self.ebay_execute('GetOrders', call_data)
            _logger.warning("I am in sync_order_ranged")
            _logger.warning(response)
            _logger.warning(response.dict())
        except:
            _logger.warning("custo _synchronize_orders_ranged didn't work")

        res = super(ebay_logs_added, self)._synchronize_orders_ranged()
        return res
