# vim:set ts=4
#
# ibus-table-other - Other tables for IBus-Table
#
# Copyright (c) 2009-2010 Caius 'kaio' Chance < k at kaio.me >
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

# if not 1, append datestamp to the version number.
m4_define([package_name], [ibus-table-others])
m4_define([ibus_released], [1])
m4_define([ibus_major_version], [1])
m4_define([ibus_minor_version], [3])
m4_define([ibus_micro_version], [19])
# commented out as datestamp doesn't suit dist date.
m4_define(ibus_maybe_datestamp,
    m4_esyscmd([if test x]ibus_released[ != x1; then date +.%Y%m%d | tr -d '\n\r'; fi]))
#m4_define([ibus_maybe_datestamp], [.20090907])

m4_define([ibus_version],
    ibus_major_version.ibus_minor_version.ibus_micro_version[]ibus_maybe_datestamp)

AC_INIT([package_name],[ibus_version],[http://code.google.com/p/ibus/issues/entry],[package_name])
AM_INIT_AUTOMAKE([1.10])
AM_MAINTAINER_MODE

# AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])

# check python
AM_PATH_PYTHON([3.3])

# check for ibus-table-createdb
PKG_CHECK_MODULES([IBUS_TABLE], [ibus-table >= 1.2.0])
AC_ARG_VAR([IBUS_TABLE_CREATEDB],[[ibus-table-createdb, which generate db]])

AC_PATH_PROG([IBUS_TABLE_CREATEDB],[ibus-table-createdb],
        [AC_MSG_ERROR([ibus-table-createdb not found.])])

# choose table
AC_ARG_ENABLE([ipaxsampa],
    [AS_HELP_STRING([--enable-ipaxsampa],[Generate ipx-a-sampa Engine])], ,
    [enable_ipaxsampa=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_IPAXSAMPA],[test x"$enable_ipaxsampa" != x"no"])

AC_ARG_ENABLE([compose],
    [AS_HELP_STRING([--enable-compose],[Generate Compose Engine])], ,
    [enable_compose=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_COMPOSE],[test x"$enable_compose" != x"no"])

AC_ARG_ENABLE([translit],
    [AS_HELP_STRING([--enable-translit],[Generate Translit Engine])], ,
    [enable_translit=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_TRANSLIT],[test x"$enable_translit" != x"no"])

AC_ARG_ENABLE([translitua],
    [AS_HELP_STRING([--enable-translitua],[Generate Ukrainian Translit Engine])], ,
    [enable_translitua=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_TRANSLITUA],[test x"$enable_translitua" != x"no"])

AC_ARG_ENABLE([rustrad],
    [AS_HELP_STRING([--enable-rustrad],[Generate Russian Traditional Engine])], ,
    [enable_rustrad=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_RUSTRAD],[test x"$enable_rustrad" != x"no"])

AC_ARG_ENABLE([rusle],
    [AS_HELP_STRING([--enable-rusle],[Generate Russian Legacy Engine])], ,
    [enable_rusle=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_RUSLE],[test x"$enable_rusle" != x"no"])

AC_ARG_ENABLE([yawerty],
    [AS_HELP_STRING([--enable-yawerty],[Generate Yawerty Engine])], ,
    [enable_yawerty=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_YAWERTY],[test x"$enable_yawerty" != x"no"])

AC_ARG_ENABLE([thai],
    [AS_HELP_STRING([--enable-thai],[Generate Thai Engine])], ,
    [enable_thai=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_THAI],[test x"$enable_thai" != x"no"])

AC_ARG_ENABLE([telex],
    [AS_HELP_STRING([--enable-telex],[Generate Telex Engine])], ,
    [enable_telex=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_TELEX],[test x"$enable_telex" != x"no"])

AC_ARG_ENABLE([viqr],
    [AS_HELP_STRING([--enable-viqr],[Generate Viqr Engine])], ,
    [enable_viqr=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_VIQR],[test x"$enable_viqr" != x"no"])

AC_ARG_ENABLE([vni],
    [AS_HELP_STRING([--enable-vni],[Generate VNI Engine])], ,
    [enable_vni=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_VNI],[test x"$enable_vni" != x"no"])

AC_ARG_ENABLE([latex],
    [AS_HELP_STRING([--enable-latex],[Generate Latex Engine])], ,
    [enable_latex=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_LATEX],[test x"$enable_latex" != x"no"])

AC_ARG_ENABLE([cns11643],
    [AS_HELP_STRING([--enable-cns11643],[Generate CNS11643 Engine])], ,
    [enable_cns11643=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_CNS11643],[test x"$enable_cns11643" != x"no"])

AC_ARG_ENABLE([emoticon],
    [AS_HELP_STRING([--enable-emoticon],[Generate Emoticon Engine])], ,
    [enable_emoticon=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_EMOTICON],[test x"$enable_emoticon" != x"no"])

AC_ARG_ENABLE([mathwriter],
    [AS_HELP_STRING([--enable-mathwriter],[Generate Mathwriter Engine])], ,
    [enable_mathwriter=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_MATHWRITER],[test x"$enable_mathwriter" != x"no"])

AC_ARG_ENABLE([rovas],
    [AS_HELP_STRING([--enable-rovas],[Generate Rovas (Old Hungarian) Engine])], ,
    [enable_rovas=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_ROVAS],[test x"$enable_rovas" != x"no"])

AC_ARG_ENABLE([mongolbichig],
    [AS_HELP_STRING([--enable-mongolbichig],[Generate Mongol Bichig Engine (Transliteration to Mongol Script)])], ,
    [enable_mongolbichig=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_MONGOLBICHIG],[test x"$enable_mongolbichig" != x"no"])

# OUTPUT files
AC_CONFIG_FILES(Makefile
icons/Makefile
tables/Makefile
emoticon-src/Makefile
ibus-table-others.spec
)

AC_OUTPUT

AC_MSG_RESULT([
Build options:
  Version                   $VERSION
  Install prefix            $prefix
  Build compose             $enable_compose
  Build ipx-a-sampa         $enable_ipaxsampa
  Build Translit            $enable_translit
  Build Ukrainian Translit  $enable_translitua
  Build Russian Traditional $enable_rustrad
  Build Russian Legacy      $enable_rusle
  Build Yawerty             $enable_yawerty
  Build Thai                $enable_thai
  Build Telex               $enable_telex
  Build Viqr                $enable_viqr
  Build VNI                 $enable_vni
  Build Latex               $enable_latex
  Build CNS11643            $enable_cns11643
  Build Emoticon            $enable_emoticon
  Build Mathwriter          $enable_mathwriter
  Build Rovas               $enable_rovas
  Build Mongol Bichig       $enable_mongolbichig
])

