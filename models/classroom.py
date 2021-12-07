# -*- coding: utf-8 -*-

from openerp import models, fields, api

class UniversityClassroom(models.Model):
     _name = 'university.classroom'
     _inherit = ['mail.thread']
     _rec_name = 'classroom_name'

     classroom_name = fields.Char(string='name')
     code = fields.Char()

     student_ids = fields.One2many(comodel_name='university.student1', inverse_name='classroom_id')

     professor_ids = fields.Many2many(comodel_name='university.professor',
                                           relation='pro_class_rel',
                                           column1='name',
                                           column2='f_name')

     subject_ids = fields.Many2many(comodel_name='university.subject',
                                           relation='class_sub_rel',
                                           column1='classroom_name',
                                           column2='name')

     num_prof = fields.Integer(string='Number of professors', compute='comp_prof')
     num_sub = fields.Integer(string='Number of subjects', compute='comp_sub')
     num_etu = fields.Integer(string='Number of students', compute='comp_etu')

     def comp_prof(self):
         self.num_prof = len(self.professor_ids)

     def comp_sub(self):
         self.num_sub = len(self.subject_ids)

     def comp_etu(self):
         self.num_etu = len(self.student_ids)

     #api.onchange est un décorateur et self va nous retourner tous les valeurs bien spécifier(limitées)de ce record  self university.professor
     @api.onchange('subject_ids')
     def _check_number_of_subjects(self):
         if len(self.subject_ids) > 4:
             #print('The number of subject most less than 4')
             return {'warning':{'title': 'warning',
                               'message': 'The number of subject most less than 4',},}



