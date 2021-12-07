# -*- coding: utf-8 -*-

from openerp import models, fields, api


class UniversitySubject(models.Model):
     _name = 'university.subject'
     name = fields.Char()
     code = fields.Char()

     departement_id = fields.Many2one(comodel_name='university.departement')
     classroom_id = fields.Many2one(comodel_name='university.classroom')

     professor_ids = fields.Many2many(comodel_name='university.professor',
                                           relation='sub_pro_rel',
                                           column1='name',
                                           column2='f_name')
