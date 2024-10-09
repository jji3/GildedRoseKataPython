# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_Aged_Brie_should_increase(self):
        ab = "Aged Brie"
        items = [Item(ab, 3, 2)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_Sulfuras_should_not_change(self):
        sul = "Sulfuras, Hand of Ragnaros"
        items = [Item(sul, 5, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(45, items[0].quality)

    def test_quality_never_negative(self):
        cake = "Conjured Mana Cake"
        items = [Item(cake, 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(-1, items[0].quality)

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)


if __name__ == '__main__':
    unittest.main()
