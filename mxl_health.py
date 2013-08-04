# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2013  Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011  Adrián Bernardi, Mario Puntin (health_invoice)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from trytond.model import ModelView, ModelSQL, fields, ModelSingleton
from trytond.pyson import Eval, Equal
from trytond.pool import Pool


__all__ = ['Patient', 'Visit', 'Encounter', 'Case']


class Patient(ModelSQL, ModelView):
    "Patient"
    __name__ = "gnuhealth.patient"
    last_visit = fields.Char('Last Visit')
    telephone_contact = fields.Char('Telephone Contact')
    visits = fields.One2Many('gnuhealth.mxl.visit', 'name', 'Visits')
    encounters = fields.One2Many('gnuhealth.mxl.encounter', 'name', 'Encounters')
    cases = fields.One2Many('gnuhealth.mxl.clinicalcase', 'name', 'Visits')



class Visit(ModelSQL, ModelView):
    'Patient Visit'
    __name__ = 'gnuhealth.mxl.visit'

    name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
    visit_type = fields.Selection([
    	('scheduled', 'Scheduled'),
    	('ad_hoc', 'Ad-Hoc')], 'Visit Type', select=True)
    visit_date = fields.Date('Date of Appointment')
    appointment_with = fields.Many2One('gnuhealth.physician', 'Clinician')
    assigned_to = fields.Many2One('gnuhealth.physician', 'Assigned To')
    assignment_date = fields.Date('Date Appointment Set')


class Encounter(ModelSQL, ModelView):
	'Clinical Encounter'
	__name__ = 'gnuhealth.mxl.encounter'

	name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
	clinician = fields.Many2One('gnuhealth.physician', 'Clinician')
	secondary_clinician = fields.Many2One('gnuhealth.physician', 'Secondary Clinician')
	#case = fields.Many2One('gnuhealth.mxl.clinicalcase', 'Case')
	encounter_date = fields.Date('Date of Encounter')
	encounter_type = fields.Selection([
    	('doctor_visit', 'Doctor Visit'),
    	('immunisation', 'Immunisation'),
    	('drug_pick_up', 'Drug Pick Up')], 'Type', select=True)

class Case(ModelSQL, ModelView):
	'Clinical Encounter'
	__name__ = 'gnuhealth.mxl.clinicalcase'

	name = fields.Many2One('gnuhealth.patient', 'Patient', readonly=True)
	diagnosis = fields.Char('Diagnosis')
	case_date = fields.Date('Date of Case')




