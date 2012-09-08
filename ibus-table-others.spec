Name:       ibus-table-others
Version:    1.3.0.20100907
Release:    2%{?dist}
Summary:    The Cyrillic tables for IBus-Table
License:    GPLv3
Group:      System Environment/Libraries
URL:        http://code.google.com/p/ibus/
Source0:    http://cloud.github.com/downloads/kaio/ibus-table-cyrillic/%{name}-%{version}.tar.gz

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

Requires:         ibus >= 1.2, ibus-table >= 1.2.0.20090912-3
Requires(post):   ibus >= 1.2, ibus-table >= 1.2.0.20090912-3
BuildRequires:    ibus >= 1.2, ibus-table >= 1.2.0.20090912-3

%description
The Cyrillic tables for IBus Table.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} \
  --disable-static \
  --enable-translit \
  --enable-translitua \
  --enable-rustrad \
  --enable-yawerty 
  --enable-mathwriter 
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install

# %find_lang %{name}

%post
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/translit.db
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/translit-ua.db
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/rustrad.db
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/yawerty.db
ibus-table-createdb -i -n %{_datadir}/ibus-table/tables/mathwriter-ibus.db

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_datadir}/ibus-table/icons/translit.svg
%{_datadir}/ibus-table/icons/translit-ua.svg
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/yawerty.png
%{_datadir}/ibus-table/tables/translit.db
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/yawerty.db
%{_datadir}/ibus-table/tables/mathwriter-ibus-table.db

%changelog
* Thu Jun 24 2010 Naveen Kumar <nav007@gmail.com> - 1.3.0.20100907-2
- Changes specific to Mathwriter

* Thu Jan 07 2010 Caius 'kaio' Chance <k at kaio.me> - 1.3.0.20100907-1
- The first version.
- Combine Translit, Translit-ua, Russian Traditional, Yawerty.
