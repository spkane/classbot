from errbot import BotPlugin, botcmd, arg_botcmd


class Students(BotPlugin):
    """'Student' plugin for Errbot"""

    def activate(self):
        super().activate()
        if self['sid'] is None:
            self['sid'] = 0

    @botcmd
    def sid_get(self, msg, args):
        """ gets a new Student ID
        """
        num = self['sid']
        num += 1
        self.log.info("Student ID for " + format(msg.frm) + " set to: " + str(num))
        self['sid'] = num
        return format(msg.frm) + ", your Student ID is: " + str(self['sid'])

    @arg_botcmd('-n', dest='num', type=int, default=0)
    def sid_reset(self, msg, num=None):
        """ resets the Student ID to a specific value
        """
        self['sid'] = num
        self.log.info(format(msg.frm) + " reset Student ID to: " + str(num))
        return "Student ID base reset to: " + str(self['sid'])
