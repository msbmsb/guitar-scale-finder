"""
guitar-scale-finder.py:

Defines the GuitarScaleFinder class. Requires constructor parameters:
* root - the root note [a-g]
* scale - as defined in lib.scale.get_scale_names()
* tuning - see lib.tablature.six_string_std for example
* start_note - a Note object specifying beginning of range
* end_note - a Note object specifying end of range

* Author:       Mitchell Bowden <mitchellbowden AT gmail DOT com>
* License:      MIT License: http://creativecommons.org/licenses/MIT/
"""

# wordstrument classes & methods
from lib.sequence import Sequence
from lib.note import Note
import lib.tablature as tablature
from lib.scale import is_valid_scale

class GuitarScaleFinder(object):
  def __init__(self, root='c', scale='major', tuning=tablature.six_string_std, start_note=Note("c2"), end_note=Note("b7")):
    self.root = root
    self.scale = scale
    self.tuning = tuning
    self._start = start_note
    self._end = end_note
    self._tab = self._build_tab_sequence()

  def _build_tab_sequence(self):
    if not is_valid_scale(self.scale):
      print "Error: %s is not a valid scale" % self.scale
      return None

    seq = self._get_sequence()
    tab = self._get_tab(seq)
    return tab

  def _get_sequence(self):
    raw_notes = Sequence(self.root)
    raw_notes.set_scale(self.scale)
    raw_notes.fill_sequence(self._start, self._end)
    return raw_notes

  def _get_tab(self, notes_):
    gt = tablature.GuitarFretboard(self.tuning)
    tab = tablature.GuitarTabSequence(gt,None)
    tab_seq = {}
    for n in notes_.notes[1:]:
      gti = gt.index(n)
      for g in gti:
        if g[0] in tab_seq:
          tab_seq[g[0]].append((g[1], n.to_str_normal()))
        else:
          tab_seq[g[0]] = [(g[1], n.to_str_normal())]

    for t in sorted(tab_seq.keys()):
      for s in sorted(tab_seq[t]):
        tab.add((t, s[0]), s[1], None)

    return tab

  def to_str(self):
    if self._tab:
      return self._tab.to_str()
    return ''

  def split_str(self, num=None):
    return self._tab.split_str_by_notes(num)
