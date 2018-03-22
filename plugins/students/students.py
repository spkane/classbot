from errbot import BotPlugin, botcmd, arg_botcmd


class Students(BotPlugin):
    """'Student' plugin for Errbot"""

    def activate(self):
        super().activate()
        try:
            self.log.info("Retrieved Initial Student ID: " + str(self['sid']))
        except:
            self['sid'] = 0
            self.log.info("Initial Student ID set to: " + str(self['sid']))

    def get_configuration_template(self):
        return {'DC1_GIST_S1': '',
                'DC1_GIST_D1': '',
                'DC1_GIST_D2': '',
                'DC2_GIST_S1': '',
                'DC2_GIST_D1': '',
                'DC2_GIST_D2': '',
                'DW1_GIST_S1': '',
                'DW1_GIST_D1': '',
                'DW1_GIST_D2': '',
                'TOKEN': ''}

    def strip_channel(self, user):
        list = str(user).split("/")
        return "@" + list[1]

    def check_config(self):
        if self.config is None or self.config == {}:
            return False
        else:
            return True

    @botcmd(template='get')
    def sid_get(self, msg, args):
        """ gets a new Student ID
        """
        num = self['sid']
        num += 1
        self.log.info("Student ID for " + format(msg.frm) + " set to: " + str(num))
        self['sid'] = num
        if msg.is_group:
            user = self.strip_channel(msg.frm)
        else:
            user = msg.frm
        return {'user': format(user), 'sid': str(self['sid'])}

    @arg_botcmd('-n', dest='num', type=int, default=0, template='reset')
    def sid_reset(self, msg, num=None):
        """ resets the Student ID to a specific value
        """
        self['sid'] = num
        self.log.info(format(msg.frm) + " reset Student ID to: " + str(num))
        if msg.is_group:
            user = self.strip_channel(msg.frm)
        else:
            user = msg.frm
        return {'user': format(user), 'sid': str(self['sid'])}

    @arg_botcmd('-c', dest='classid', type=str, default="0", template='prep')
    def class_prep(self, msg, classid):
        """ posts the preperation directions to the channel
        """
        if self.check_config() == False:
            return str(msg.frm) + "You must configure this plugin. Try `!plugin config Students`"
        if classid == "dc1":
            gist = self.config['DC1_GIST_S1']
        elif classid == "dc2":
            gist = self.config['DC2_GIST_S1']
        elif classid == "dw1":
            gist = self.config['DW1_GIST_S1']
        else:
            return str(msg.frm) + ", this class ID is unknown: " + str(classid)
        return {'setup': gist}

    @arg_botcmd('-c', dest='classid', type=str, default="0", template='intro')
    def class_intro(self, msg, classid):
        """ posts the daily intro to the channel
        """
        if self.check_config() == False:
            return str(msg.frm) + "You must configure this plugin. Try `!plugin config Students`"
        token = self.config['TOKEN']
        if classid == "dc1-1":
            gist1 = self.config['DC1_GIST_S1']
            gist2 = self.config['DC1_GIST_D1']
            day="One"
        elif classid == "dc2-1":
            gist1 = self.config['DC2_GIST_S1']
            gist2 = self.config['DC2_GIST_D1']
            day = "One"
        elif classid == "dw1-1":
            gist1 = self.config['DW1_GIST_S1']
            gist2 = self.config['DW1_GIST_D1']
            day = "One"
        elif classid == "dc1-2":
            gist1 = self.config['DC1_GIST_S1']
            gist2 = self.config['DC1_GIST_D2']
            day = "Two"
        elif classid == "dc2-2":
            gist1 = self.config['DC2_GIST_S1']
            gist2 = self.config['DC2_GIST_D2']
            day = "Two"
        elif classid == "dw1-2":
            gist1 = self.config['DW1_GIST_S1']
            gist2 = self.config['DW1_GIST_D2']
            day = "Two"
        else:
            return str(msg.frm) + ", this class ID is unknown: " + classid
        return {'classid': classid, 'setup': gist1, 'follow': gist2, 'day': day, 'token': token}
