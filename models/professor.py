# -*- coding: utf-8 -*-

from openerp import models, fields, api

class UniversityProfessor(models.Model):
     _name = 'university.professor'

     f_name = fields.Char('first name')
     l_name = fields.Char('last name')
     sexe = fields.Selection([('male', 'Male'), ('femal', 'Femal')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Adresse ')
     birthday = fields.Date('Birthday')
     inscription_date = fields.Datetime('Date of inscription')
     email = fields.Char()
     phone = fields.Char()

     #pour activer le mail à travers un bouton dans professor.xml
     active=fields.Boolean()

     departement_id = fields.Many2one(comodel_name='university.departement')
     suject_id = fields.Many2one(comodel_name='university.subject')

     classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                           relation='class_pro_rel',
                                           column1='name',
                                           column2='f_name')

     # @api.multi est un décorateur et self va nous retourner tous les valeurs de ce record  self university.professor

     @api.multi
     def name_get(self):
          result = []
          for prof in self:
               name ='[ '+ prof.departement_id.name +' ] '+ prof.f_name +' '+ prof.l_name
               result.append((prof.id, name))
               return result
@api.multi
def send_email(self):
     self.ensure_one()
     template_id = self.env.ref('university.email_templete_prof').id
     ctx = {
          'default_model':'univesity.professor',
          'default_res_id': self.id,
          'default_use_template':bool(template_id),
          'default_composition_mode':'comment',
          'email_to':self.email,
     }
     return {
          'type':'ir.actions.act_window',
          'view_type':'form',
          'res_model':'mail.compose.message',
          'target':'new',
          'context':ctx
     }


















