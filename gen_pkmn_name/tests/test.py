from unittest import TestCase
import gen_pkmn_name as pkmn
from gen_pkmn_name.command_line import main

class TestConsole(TestCase):
  def test_basic(self):
    main()