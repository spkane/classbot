from errbot.backends.test import testbot
import students

extra_plugin_dir = '.'


def test_sid_get(testbot):
    testbot.push_message('!sid get')
    assert 'gbin@localhost, your Student ID is: 1' in testbot.pop_message()


def test_sid_reset(testbot):
    testbot.push_message('!sid reset -n 0')
    assert 'Student ID base reset to: 0' in testbot.pop_message()
