# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AutonomousCommunity(models.Model):
    _name = "mkob_spain_topology_community.autonomous.community"
    _description = "Autonomous Community"

    name = fields.Char(string="Name", required=True, )
    slug = fields.Char(string="Slug")
    abbreviation = fields.Char(string="Abbreviation")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", required=False, )
    state_ids = fields.Many2many(comodel_name="res.country.state", relation="mkob_spain_autonomous_comm_state_rel",
                                 column1="ac_id", column2="state_id", string="States", )

    @api.model
    def get_data(self):
        data = {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'abbreviation': self.abbreviation,
            'country_id': self.country_id.id if self.country_id else False,
            'state_ids': [s.id for s in self.state_ids] if self.state_ids else False,
        }
        return data

    @api.onchange('state_ids')
    def onchange_state_ids(self):
        if self.state_ids and not self.country_id:
            self.country_id = self.state_ids[0].country_id.id
