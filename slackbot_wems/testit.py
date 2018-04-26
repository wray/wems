import unittest
import bot_id
import slackpi
import wray.slacklib
import chris.slacklib
import joe.slacklib
import matthew.slacklib

import wems.bella.slacklib
import wems.clarke.slacklib
import wems.dean.slacklib
import wems.emerson.slacklib
import wems.james.slacklib
import wems.jonathan.slacklib
import wems.kent.slacklib
import wems.meira.slacklib
import wems.morgan.slacklib
import wems.sam.slacklib
import wems.sienna.slacklib
import wems.soumya.slacklib
import wems.viktor.slacklib

import wems.adele.slacklib
import wems.hank.slacklib
import wems.ibby.slacklib
import wems.layla.slacklib
import wems.mardi_belle.slacklib
import wems.naomi.slacklib
import wems.spencer.slacklib

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

    def test_matthew_handler(self):
        self.assertFalse(matthew.slacklib.handle_command('') == None)


    def test_adele_handler(self):
        self.assertFalse(wems.adele.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.adele.slacklib.handle_command(
            wems.adele.slacklib.COMMAND1)) > 1)

    def test_bella_handler(self):
        self.assertFalse(wems.bella.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.bella.slacklib.handle_command(
            wems.bella.slacklib.COMMAND1)) > 1)

    def test_clarke_handler(self):
        self.assertFalse(wems.clarke.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.clarke.slacklib.handle_command(
            wems.clarke.slacklib.COMMAND1)) > 1)

    def test_dean_handler(self):
        self.assertFalse(wems.dean.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.dean.slacklib.handle_command(
            wems.dean.slacklib.COMMAND1)) > 1)

    def test_emerson_handler(self):
        self.assertFalse(wems.emerson.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.emerson.slacklib.handle_command(
            wems.emerson.slacklib.COMMAND1)) > 1)

    def test_hank_handler(self):
        self.assertFalse(wems.hank.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.hank.slacklib.handle_command(
            wems.hank.slacklib.COMMAND1)) > 1)

    def test_ibby_handler(self):
        self.assertFalse(wems.ibby.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.ibby.slacklib.handle_command(
            wems.ibby.slacklib.COMMAND1)) > 1)

    def test_james_handler(self):
        self.assertFalse(wems.james.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.james.slacklib.handle_command(
            wems.james.slacklib.COMMAND1)) > 1)

    def test_jonathan_handler(self):
        self.assertFalse(wems.jonathan.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.jonathan.slacklib.handle_command(
            wems.jonathan.slacklib.COMMAND1)) > 1)

    def test_kent_handler(self):
        self.assertFalse(wems.kent.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.kent.slacklib.handle_command(
            wems.kent.slacklib.COMMAND1)) > 1)

    def test_layla_handler(self):
        self.assertFalse(wems.layla.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.layla.slacklib.handle_command(
            wems.layla.slacklib.COMMAND1)) > 1)

    def test_mardi_belle_handler(self):
        self.assertFalse(wems.mardi_belle.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.mardi_belle.slacklib.handle_command(
            wems.mardi_belle.slacklib.COMMAND1)) > 1)

    def test_meira_handler(self):
        self.assertFalse(wems.meira.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.meira.slacklib.handle_command(
            wems.meira.slacklib.COMMAND1)) > 1)

    def test_morgan_handler(self):
        self.assertFalse(wems.morgan.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.morgan.slacklib.handle_command(
            wems.morgan.slacklib.COMMAND1)) > 1)

    def test_naomi_handler(self):
        self.assertFalse(wems.naomi.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.naomi.slacklib.handle_command(
            wems.naomi.slacklib.COMMAND1)) > 1)

    def test_naomi_handler(self):
        self.assertFalse(wems.naomi.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.naomi.slacklib.handle_command(
            wems.naomi.slacklib.COMMAND1)) > 1)

    def test_sam_handler(self):
        self.assertFalse(wems.sam.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.sam.slacklib.handle_command(
            wems.sam.slacklib.COMMAND1)) > 1)

    def test_sienna_handler(self):
        self.assertFalse(wems.sienna.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.sienna.slacklib.handle_command(
            wems.sienna.slacklib.COMMAND1)) > 1)

    def test_soumya_handler(self):
        self.assertFalse(wems.soumya.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.soumya.slacklib.handle_command(
            wems.soumya.slacklib.COMMAND1)) > 1)

    def test_spencer_handler(self):
        self.assertFalse(wems.spencer.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.spencer.slacklib.handle_command(
            wems.spencer.slacklib.COMMAND1)) > 1)

    def test_viktor_handler(self):
        self.assertFalse(wems.viktor.slacklib.handle_command('') == None)
        self.assertTrue(len(wems.viktor.slacklib.handle_command(
            wems.viktor.slacklib.COMMAND1)) > 1)

if __name__ == '__main__':
    unittest.main()
