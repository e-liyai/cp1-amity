"""
File      : amity.py
Date      : February, 2017
Author    : eugene liyai
Desc      : Amity is a controller class that runs the application

"""

# ============================================================================
# necessary imports
# ============================================================================

from accounts.fellow import Fellow
from accounts.staff import Staff
from rooms.room import Room
from rooms.livingroom import Livingroom

class Amity(object):
    '''
		Amity class is the controller class for the amity project
		It initiates instances of Person and Room parent classes and controlles
		the views of the project.  
	'''

    # ============================================================================
    # create room from amity
    # ============================================================================
    @staticmethod
    def create_room(name, roomtype):
        pass

    # ============================================================================
    # add new person to random room 
    # ============================================================================
    @staticmethod
    def add_person(staff=None, fellow=None, accomodation=False):

    	pass

    # ============================================================================
    # get person details
    # ============================================================================
    @staticmethod
    def get_person_details(user_id):

    	pass

    # ============================================================================
    # print un allocated rooms
    # ============================================================================
    @staticmethod
    def print_unallocated(file = None):

    	pass

    # ============================================================================
    # print allocated rooms and the persons allocated
    # ============================================================================
    @staticmethod
    def print_allocated(file = None):

    	pass

    # ============================================================================
    # print room details
    # ============================================================================
    @staticmethod
    def print_room(roomname):

    	pass

    # ============================================================================
    # create unique room name constaraint
    # ============================================================================
    def is_room_name_unique(self, roomname):
        pass

    # ============================================================================
    # reallocate person
    # ============================================================================
    def reallocate_person_by_username(self, staffname, roomname):
        pass

    def reallocate_person_by_userid(self, persinid, roomname):
        pass

    # ============================================================================
    # reallocate person
    # ============================================================================
    def save_state(self, save_data):
        pass

    # ============================================================================
    # loads a previously saved state
    # ============================================================================
    def load_state(self, load_data):
        pass