# 1. Example
import unittest
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size/2 - 1] + copy[size/2]) / 2
class TestMedian(unittest.TestCase):
    def testMedian(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
if __name__ == '__main__':
    unittest.main()


# 2. Example
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

printme()
printme("Again second call to the same function")



def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #self
    self.error = MDText()
    self.add_widget(self.error, canvas='after')

    def on_focus(self, _, value):
        pass

class FloatingAction(Factory.IconButton):
    action = ObjectProperty(allownone=True)

    def show(self, *args):
        Clock.schedule_once(self._show, 0)

    def _show(self, *args):
        Animation.cancel_all(self)
        Animation(font_size=self.target_font_size),
                  d=0.1,
                  t='linear').start(self)

    def hide(self, *args):
        Animation.cancel_all(self)
        Animation(font_size=0, d=0.2, t='linear').start(self)