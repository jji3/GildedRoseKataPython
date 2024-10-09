# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_never_negative(self):
        cake = "Conjured Mana Cake"
        items = [Item(cake, 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(-1, items[0].quality)

    def test_quality_should_not_exceed_50(self):
        sul = "Sulfuras, Hand of Ragnaros"
        items = [Item(sul, 5, 55)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(50, items[0].quality)
        
    def test_extra_pass_quality(self):
        passes = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(passes, 5, 45)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(49, items[0].quality)

    # def test_foo(self):
    #     items = [Item("foo", 0, 0)
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)


if __name__ == '__main__':
    unittest.main()
