"""
test_gsf.py:

File to test the GuitarScaleFinder class.

* Author:       Mitchell Bowden <mitchellbowden AT gmail DOT com>
* License:      MIT License: http://creativecommons.org/licenses/MIT/
"""

# wordstrument classes & methods
from lib.sequence import Sequence
from lib.note import Note
import lib.tablature as tablature
from lib.scale import is_valid_scale

from guitar_scale_finder import GuitarScaleFinder

###############################
# testing

def test_scale_finder():
  toTest = "c"

  raw_notes = Sequence(toTest)
  raw_notes.set_scale('major')
  raw_notes.fill_sequence(Note("c2"), Note("b7"))

  gt = tablature.GuitarFretboard(tablature.six_string_std)
  tab = tablature.GuitarTabSequence(gt,None)
  tab_seq = {}
  for n in raw_notes.notes[1:]:
    gti = gt.index(n)
    for g in gti:
      if g[0] in tab_seq:
        tab_seq[g[0]].append((g[1], n.to_str_normal()))
      else:
        tab_seq[g[0]] = [(g[1], n.to_str_normal())]

  for t in sorted(tab_seq.keys()):
    for s in sorted(tab_seq[t]):
      tab.add((t, s[0]), s[1], None)

  reg = tab.to_str()

  gsf = GuitarScaleFinder('c', 'major', tablature.six_string_std, Note("c2"), Note("b7"))
  gsf_str = gsf.to_str()
  print reg
  print "----------------------------"
  print gsf_str
  print "======="
  if gsf_str == reg:
    print "Matches - ok"
  else:
    print "No match - fail"

  print gsf.split_str(12)

if __name__ == '__main__':
  test_scale_finder()
