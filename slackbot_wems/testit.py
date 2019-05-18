import unittest
import slackbot_wems.bot_id as bot_id
import slackbot_wems.slackpi as slackpi
import slackbot_wems.wray.slacklib as wray
#import chris.slacklib

class TestSlackBotFunctions(unittest.TestCase):

    def test_ci(self):
        self.assertTrue(True)

    def test_slack_client(self):
        self.assertTrue(bot_id.get_id() == None)

    def test_slack_pi(self):
        self.assertTrue(slackpi.handle_command("","") == None)

    def test_wray_handler(self):
        self.assertFalse(wray.handle_command('') == None)
        self.assertTrue(len(wray.handle_command(
            wray.COMMAND1)) > 1)
        resp = wray.handle_command(wray.COMMAND4)
        print(resp)
        self.assertTrue(len(resp) > 1)

    def test_exc_handler(self):
        self.assertTrue(slackpi.handle_command('version','channel') == None)
        
    # def test_chris_handler(self):
    #     self.assertFalse(chris.slacklib.handle_command('') == None)
    #     self.assertTrue(len(chris.slacklib.handle_command(
    #         chris.slacklib.COMMAND1)) > 1)
    
    # def test_joe_handler(self):
    #     self.assertFalse(joe.slacklib.handle_command('') == None)
    #     self.assertTrue(len(joe.slacklib.handle_command(
    #         joe.slacklib.COMMAND1)) > 1)
    #    # self.assertTrue(slackpi.handle_command(
    #        # joe.slacklib.COMMAND1,"") == None)
    #     #self.assertFalse(joe.slacklib.handle_command('green led on') == None)

    # def test_matthew_handler(self):
    #     self.assertFalse(matthew.slacklib.handle_command('') == None)

    #def test_hank_handler(self):
       #self.assertFalse(wems.hank.slacklib.handle_command('') == None)
        #self.assertTrue(len(wems.hank.slacklib.handle_command(
            #wems.hank.slacklib.COMMAND1)) > 1)

    #def test_ibby_handler(self):
        #self.assertFalse(wems.ibby.slacklib.handle_command('') == None)
        #self.assertTrue(len(wems.ibby.slacklib.handle_command(
            #wems.ibby.slacklib.COMMAND1)) > 1)

    # def test_james_handler(self):
    #     self.assertFalse(wems.james.slacklib.handle_command('') == None)
    #     self.assertTrue(len(wems.james.slacklib.handle_command(
    #         wems.james.slacklib.COMMAND1)) > 1)

    # def test_layla_handler(self):
    #     self.assertFalse(wems.layla.slacklib.handle_command('') == None)
    #     self.assertTrue(len(wems.layla.slacklib.handle_command(
    #         wems.layla.slacklib.COMMAND1)) > 1)

    # def test_caroline_handler(self):
    #     self.assertFalse(wems.caroline.slacklib.handle_command('') == None)
    #     self.assertTrue(len(wems.caroline.slacklib.handle_command(
    #         wems.caroline.slacklib.COMMAND1)) > 1)

    # def test_rhyder_handler(self):
    #     self.assertFalse(wems.rhyder.slacklib.handle_command('') == None)
    #     self.assertTrue(len(wems.rhyder.slacklib.handle_command(
    #         wems.rhyder.slacklib.COMMAND1)) > 1)


if __name__ == '__main__':
    unittest.main()
