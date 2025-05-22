# vim:set ts=4
#
# ibus-table-others - Other tables for IBus-Table
#
# Copyright (c) 2009-2010 Caius 'kaio' Chance <k at kaio.me>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

createdb = \
	$(IBUS_TABLE_CREATEDB) 

tables_DATA =

if IBUS_TABLE_BUILD_COMPOSE
tables_DATA += compose.db
endif

if IBUS_TABLE_BUILD_IPAXSAMPA
tables_DATA += ipa-x-sampa.db
endif

if IBUS_TABLE_BUILD_TRANSLIT
tables_DATA += translit.db
endif

if IBUS_TABLE_BUILD_TRANSLITUA
tables_DATA += translit-ua.db
endif

if IBUS_TABLE_BUILD_RUSTRAD
tables_DATA += rustrad.db
endif

if IBUS_TABLE_BUILD_RUSLE
tables_DATA += rusle.db
endif

if IBUS_TABLE_BUILD_YAWERTY
tables_DATA += yawerty.db
endif

if IBUS_TABLE_BUILD_THAI
tables_DATA += thai.db
endif

if IBUS_TABLE_BUILD_TELEX
tables_DATA += telex.db
endif

if IBUS_TABLE_BUILD_VIQR
tables_DATA += viqr.db
endif

if IBUS_TABLE_BUILD_VNI
tables_DATA += vni.db
endif

if IBUS_TABLE_BUILD_LATEX
tables_DATA += latex.db
endif

if IBUS_TABLE_BUILD_LEAN
tables_DATA += lean.db
endif

if IBUS_TABLE_BUILD_CNS11643
tables_DATA += cns11643.db
endif

if IBUS_TABLE_BUILD_EMOTICON
tables_DATA += emoticon-table.db
endif

if IBUS_TABLE_BUILD_MATHWRITER
tables_DATA += mathwriter-ibus.db
endif

if IBUS_TABLE_BUILD_ROVAS
tables_DATA += hu-old-hungarian-rovas.db
endif

if IBUS_TABLE_BUILD_HUHUNGTRADITIONAL
tables_DATA += hu_Hung_HU_traditional.db
endif

if IBUS_TABLE_BUILD_MONGOLBICHIG
tables_DATA += mongol_bichig.db
endif

tables_DATA += $(NULL)

tablesdir = $(datadir)/ibus-table/tables

EXTRA_DIST = \
	compose.txt \
	hu-old-hungarian-rovas.txt \
	hu_Hung_HU_traditional.txt \
	ipa-x-sampa.txt \
	translit.txt \
	translit-ua.txt \
	rustrad.txt \
	rusle.txt \
	yawerty.txt \
	thai.txt \
	telex.txt \
	viqr.txt \
	vni.txt \
	latex.txt \
	lean.txt \
	cns11643.txt \
	emoticon-table.txt \
	mathwriter-ibus.txt \
	mongol_bichig.txt \
	$(NULL)

DISTCLEANFILES = \
	*.db \
	$(NULL)

.txt.db:
	$(createdb) -n $@ -s $<

