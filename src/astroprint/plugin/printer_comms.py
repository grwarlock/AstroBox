# coding=utf-8
__author__ = "AstroPrint Product Team <product@astroprint.com>"
__license__ = "GNU Affero General Public License http://www.gnu.org/licenses/agpl.html"
__copyright__ = "Copyright (C) 2017 3DaGoGo, Inc - Released under terms of the AGPLv3 License"

class PrinterCommsService(object):

	## Implement these functions

	#
	# Returns a tuple representing the driver name: (id, name).
	# This will be used in the driver selection box
	#

	@property
	def driverName(self):
		raise NotImplementedError()