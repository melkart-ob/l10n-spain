# -*- coding: utf-8 -*-

from odoo import fields, models, api


class GroupState(models.Model):
    _name = "res.country.state.group"
    _description = ""

    name = fields.Char(string="Name", required=True, )
    code = fields.Char(string="Code")
    abbreviation = fields.Char(string="Abbreviation")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", required=False, )
    state_ids = fields.Many2many(comodel_name="res.country.state", relation="res_country_state_group_state_rel",
                                 column1="group_id", column2="state_id", string="States", )

    @api.model
    def get_data(self):
        data = {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'abbreviation': self.abbreviation,
            'country_id': self.country_id.id if self.country_id else False,
            'state_ids': [s.id for s in self.state_ids] if self.state_ids else False,
        }
        return data

    @api.onchange('state_ids')
    def onchange_state_ids(self):
        if self.state_ids and not self.country_id:
            self.country_id = self.state_ids[0].country_id.id
