# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import except_orm, Warning, RedirectWarning


class UniversityStudent(models.Model):
     _name='university.student1'
     # = 'f_name'

     f_name = fields.Char('firts name')
     l_name = fields.Char('last name')
     sexe = fields.Selection([('male', 'Male'), ('femal', 'Femal')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Adresse ')
     birthday = fields.Date('Birthday')
     registration_date = fields.Datetime('Registration Date')
     email = fields.Char()
     phone = fields.Char()

     state = fields.Selection([('l1', 'leven1'),('l2', 'leven2'),('l3', 'leven3'),('finish', 'Finished'),])

     departement_id = fields.Many2one(comodel_name='university.departement')
     classroom_id = fields.Many2one(comodel_name='university.classroom')

     #champs relier pour obtenir les matière de la classe
     subject_ids = fields.Many2many(related='classroom_id.subject_ids')
     #fin champs rilier

     # @api.multi est un décorateur et self va nous retourner tous les valeurs de ce record self university.student1
     @api.multi
     def name_get(self):
          result = []
          for student in self:
               name ='[ '+ student.classroom_id.classroom_name +' ] ' + student.f_name +' '+ student.l_name
               result.append((student.id, name))
               return result

     #@api.multi est un décorateur et self vifier les valeur de ce record  self (la date naissance doit etre au dessus de la date d'enregistrement) university.student
     @api.constrains('registration_date', 'birthday')
     # pour appliquer aux enregistrement one par one
     @api.one
     def chek_dates(self):
          if self.birthday > self.registration_date:
               raise ValueError('The birthday mus be inferior of than registraition date')


     @api.multi
     def next_level(self):
          self.ensure_one()# va s'assurer que le traitement va s'exécutersur un seul éléments
          if self.state == 'l1':
               return self.write({'state': 'l2'})

          elif self.state == 'l2':
               return self.write({'state': 'l3'})

          elif self.state == 'l3':
               return self.write({'state': 'finished'})

          else :
               raise Warning('The student has already finished is courses !')






