from errbot import BotPlugin, botcmd, arg_botcmd


class Students(BotPlugin):
    """'Student' plugin for Errbot"""

    def activate(self):
        self.sid = 0
        super().activate()

    @botcmd
    def sid_get(self, msg, args):
        """ gets a new Student ID
        """
        self.sid += 1
        return format(msg.frm) + ", your Student ID is: " + str(self.sid)

    @arg_botcmd('-n', dest='number', type=int, default=0)
    def sid_reset(self, msg, number=None):
        """ resets the Student ID to a specific value
        """
        self.sid = number
        return "Student ID base reset to: " + str(self.sid)
