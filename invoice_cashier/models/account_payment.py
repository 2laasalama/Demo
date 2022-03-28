# -*- coding: utf-8 -*-
from odoo import models, fields, api,_

class AccountPayment(models.Model):
    _inherit='account.payment'

    mail_sent =fields.Boolean(copy=False)

    @api.model
    def create(self,vals):
        res=super(AccountPayment, self).create(vals)
        for rec in res:
           if rec.mail_sent != True and rec.payment_type == 'outbound':
               users=self.env['res.users'].search([])
               for user in users:
                   if user.has_group('account.group_account_manager'):
                       rec.activity_schedule('invoice_cashier.schedule_activity_of_send_payment_id', rec.date,
                                             user_id=user.id,
                                             summary=self.env.user.name +' '+'This Send Payment' + ' '+ rec.name + 'Is Created')
               rec.mail_sent = True
        return res
