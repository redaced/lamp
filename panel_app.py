#!/usr/bin/env python

import gobject
import gtk
import appindicator
import os


def menuitem_response(w, buf):
  print buf

if __name__ == "__main__":
  ind = appindicator.Indicator ("example-simple-client","indicator-messages",appindicator.CATEGORY_APPLICATION_STATUS)
  ind.set_status (appindicator.STATUS_ACTIVE)
  ind.set_attention_icon ("indicator-messages-new")

  # create a menu
  menu = gtk.Menu()

  p = os.popen('',"r")
  while 1:
    line = p.readline()
    if not line: break
    print line
  # create some 
  # for i in range(3):
  #   buf = "Test-undermenu - %d" % i
  buf = "MySql"

  menu_items = gtk.MenuItem(buf)

  menu.append(menu_items)

  menu_items.show()

  ind.set_menu(menu)

  gtk.main()