#!/usr/bin/python

####################
# Module:   AttackBase
# Author:   J. Rieder
# Date:     2015/11/11
# Version:  1.0
#
# Description: Implementation of the base class all attacks use.
#
###############################
# Log:
# 2015/11/11    S.S - Initial
################################

from abc import ABCMeta, abstractmethod

class Attack:
	__metaclass__ = ABCMeta
	
	# Used to start an Attack.
	@abstractmethod
	def start(self): pass

	# Displays short helping text for every Attack.
	@abstractmethod
	def help(self): pass
