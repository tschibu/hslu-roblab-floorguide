#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alusersessionproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALUserSession(object):
    def __init__(self, session):
        self.proxy = None 
        self.session = session

    def force_connect(self):
        self.proxy = self.session.service("ALUserSession")

    def areUserSessionsOpen(self, user_list):
        """Check if users have an open session.

        :param std::vector<int> user_list: A list of int IDs of each user to check.
        :returns bool: A bool, true if all users have open sessions.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.areUserSessionsOpen(user_list)

    def doUsersExist(self, user_list):
        """Check if users exist in db.

        :param std::vector<int> user_list: A list of int ID of the users to check.
        :returns bool: A bool, true if all users exist.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.doUsersExist(user_list)

    def doesBindingSourceExist(self, binding_name):
        """Query if a particular has been applied to UserSession

        :param str binding_name: The string name of the binding source.
        :returns bool: A bool, true if a binding source exists.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.doesBindingSourceExist(binding_name)

    def doesUserDataSourceExist(self, source_name):
        """Check if a data source has been registered.

        :param str source_name: The string name of the data source.
        :returns bool: A bool, true if the source has been registered
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.doesUserDataSourceExist(source_name)

    def findUsersWithBinding(self, binding_name, binding_value):
        """Get the sources a user is bound to.

        :param str binding_name: The string name of the binding source.
        :param str binding_value: The string ID of the user at the binding source.
        :returns std::vector<int>: The int IDs of the users with the passed binding_value.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.findUsersWithBinding(binding_name, binding_value)

    def getBindingSources(self):
        """The list of binding sources  that have been applied to UserSession

        :returns std::vector<std::string>: A list of strings, one for each binding source.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getBindingSources()

    def getFocusedUser(self):
        """Get which user has the robot's focus.

        :returns int: The int ID of the focused user. -1 if no focused user.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getFocusedUser()

    def getNumUsers(self):
        """Get the count of users in db.

        :returns int: An int of how many users exist
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getNumUsers()

    def getOpenUserSessions(self):
        """Get which users have an open session.

        :returns std::vector<int>: A list of int IDs of each user with an open session.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getOpenUserSessions()

    def getUserBinding(self, uid, binding_name):
        """Get the a specific source a user is bound to.

        :param int uid: The int ID of the user.
        :param str binding_name: The string name of the binding source.
        :returns str: The string value of the binding ID for the user.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getUserBinding(uid, binding_name)

    def getUserBindings(self, uid):
        """Get the sources a user is bound to.

        :param int uid: The int ID of the user.
        :returns std::map<std::string , std::string>: A map of string binding names and their string values.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getUserBindings(uid)

    def getUserData(self, uid, data_name):
        """Get some data about a user.  Will throw if it does not exist

        :param int uid: The int ID of the user whose data to get.
        :param str data_name: The key of the data to get.
        :returns std::map<std::string , AL::ALValue>: A map keyed by source_name of ALValues of the data.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getUserData(uid, data_name)

    def getUserData2(self, uid, data_name, source_name):
        """Get some data about a user.  Will throw if it does not exist

        :param int uid: The int ID of the user whose data to get.
        :param str data_name: The key of the data to get.
        :param str source_name: The string name of the data source.
        :returns AL::ALValue: ALValue of the data.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getUserData(uid, data_name, source_name)

    def getUserDataSources(self):
        """Check what data sources have been registered.

        :returns std::vector<std::string>: A list of strings of each registered data source.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getUserDataSources()

    def getUserList(self):
        """Get a full list of the users.

        :returns std::vector<int>: A list of int user IDs.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.getUserList()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.ping()

    def setUserData(self, uid, data_name, source_name, data):
        """Set some data about a user.  Will throw if user does not exist

        :param int uid: The int ID of the user whose data to set.
        :param str data_name: The key of the data to set.
        :param str source_name: The string name of the data source.
        :param AL::ALValue data: ALValue of the data.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.setUserData(uid, data_name, source_name, data)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALUserSession")
        return self.proxy.version()
