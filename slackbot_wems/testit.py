import unittest
import bot_id
import slackpi
import wray.slacklib
import chris.slacklib
import joe.slacklib

class TestSlackBotFunctions(unittest.TestCase):

    def test_ci(self):
        self.assertTrue(True)

    def test_slack_client(self):
        self.assertTrue(bot_id.get_id() == None)

    def test_slack_pi(self):
        self.assertTrue(slackpi.handle_command("","") == None)

    def test_wray_handler(self):
        self.assertFalse(wray.slacklib.handle_command('') == None)
        self.assertTrue(len(wray.slacklib.handle_command(
            wray.slacklib.COMMAND1)) > 1)
        resp = wray.slacklib.handle_command(wray.slacklib.COMMAND4)
        print(resp)
        self.assertTrue(len(resp) > 1)

    def test_exc_handler(self):
        self.assertTrue(slackpi.handle_command('version','channel') == None)
        
    def test_chris_handler(self):
        self.assertFalse(chris.slacklib.handle_command('') == None)
        self.assertTrue(len(chris.slacklib.handle_command(
            chris.slacklib.COMMAND1)) > 1)
    
    def test_joe_handler(self):
        self.assertFalse(joe.slacklib.handle_command('') == None)
        self.assertTrue(len(joe.slacklib.handle_command(
            joe.slacklib.COMMAND1)) > 1)
       # self.assertTrue(slackpi.handle_command(
           # joe.slacklib.COMMAND1,"") == None)
        #self.assertFalse(joe.slacklib.handle_command('green led on') == None)


if __name__ == '__main__':
    unittest.main()
