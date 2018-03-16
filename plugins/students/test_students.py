import os
import students
from errbot.backends.test import testbot

class TestStudents(object):
    extra_plugin_dir = '.'

    def test_sid(self, testbot):
        testbot.push_message('!sid get')
        assert 'gbin@localhost, your Student ID is: 1' in testbot.pop_message()
        testbot.push_message('!sid reset -n 0')
        assert 'Student ID base reset to: 0' in testbot.pop_message()
