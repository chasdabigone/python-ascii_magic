import sys, os
sys.path.append(os.path.abspath(".."))

try:
  import google.colab  # so I only do it when I'm on google colab
  sys.path.insert(0, "/content/ascii_magic")
except:
  pass

from ascii_magic.ascii_magic._ascii_magic import AsciiArt, Front, Back  # noqa
from ascii_magic.ascii_magic.constants import PALETTE, CHARS_BY_DENSITY  # noqa
from ascii_magic.ascii_magic.functions import *  # noqa
