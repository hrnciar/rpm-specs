%define prever pre1

Name:           mdbtools
Version:        0.7.1
Release:        16%{?dist}
Summary:        Access data stored in Microsoft Access databases
License:        GPLv2+
URL:            https://github.com/brianb/mdbtools/wiki

Source0         https://github.com/brianb/mdbtools/archive/%{version}.tar.gz
Source1:        gmdb2.desktop
BuildRequires:  libxml2-devel libgnomeui-devel 
BuildRequires:  unixODBC-devel readline-devel
BuildRequires:  bison flex desktop-file-utils
BuildRequires:  txt2man gnome-common rarian-compat
BuildRequires:  libtool autoconf automake
Requires:       %{name}-libs = %{version}-%{release}

%description
MDB Tools is a suite of programs for accessing data stored in Microsoft
Access databases.


%package libs
Summary:        Library for accessing data stored in Microsoft Access databases
License:        LGPLv2+

%description libs
This package contains the MDB Tools library, which can be used by applications
to access data stored in Microsoft Access databases.


%package        devel
Summary:        Development files for %{name}
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}, glib2-devel, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package gui
Summary:        Graphical interface for MDB Tools
License:        GPLv2+ 
Requires:       %{name}-libs = %{version}-%{release}

%description gui
The mdbtools-gui package contains the gmdb2 graphical user interface
for MDB Tools


%prep
%setup -q

autoreconf -vif

%build
%configure --disable-static --enable-sql --with-unixodbc="%{_prefix}" --enable-gtk-doc

LANG=C make %{?_smp_mflags} V=1


%install
LANG=C make install DESTDIR="$RPM_BUILD_ROOT"

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

# remove some headers which should not be installed / exported
rm $RPM_BUILD_ROOT%{_includedir}/gmdb.h
rm $RPM_BUILD_ROOT%{_includedir}/mdbver.h

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%ldconfig_scriptlets libs


%files
%doc COPYING
%{_bindir}/mdb-*
%{_mandir}/man1/mdb-*.1.gz

%files libs
%doc AUTHORS COPYING.LIB NEWS README
%{_libdir}/libmdb*.so.*

%files devel
%doc HACKING ChangeLog TODO doc/faq.html
%{_libdir}/libmdb*.so
%{_libdir}/pkgconfig/libmdb*.pc
%{_includedir}/mdb*.h

%files gui
%{_bindir}/gmdb2
%{_datadir}/gmdb
%{_datadir}/gnome/help/gmdb
%{_datadir}/applications/*gmdb2.desktop
%{_datadir}/omf/mdbtools/gmdb-C.omf
%{_mandir}/man1/gmdb2.1.gz

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-13
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.7.1-6
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-1
- Update to 0.7.1
- Update site/source to github urls
- Cleanup spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.14.cvs20051109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-0.13.cvs20051109
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.12.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.11.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.10.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6-0.9.cvs20051109.1
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.8.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.7.cvs20051109.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Karsten Hopp <karsten@redhat.com> 0.6-0.6.cvs20051109.1
- bump and rebuild for current unixODBC libs

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-0.6.cvs20051109
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.5.cvs20051109
- Fix several issues with the odbc interface (rh 472692)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6-0.4.cvs20051109
- Autorebuild for GCC 4.3

* Tue Aug 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.3.cvs20051109
- Stop gmdb from crashing when selecting close without a file being open
  (bz 251419)
- Change release field from 0.x.pre1 to 0.x.cvs20051109, as that more acurately
  reflects our upstream base (bz 251419)

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.2.pre1
- Stop gmdb from crashing when selecting file->properties without having a file
  loaded (bz 251419)
- Don't install headers used to build tools (install only those of libmdb)
- Add glib2-devel to the -devel Requires

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-0.1.pre1
- There were lots of compile warnings, looking for a fix I found that upstream
  is dead, but that Debian has sort of continued as upstream based on the
  0.6pre1 release; Switching to Debian "upstream" release 0.6pre1 (20051109-4)

* Wed Aug  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-1
- Initial Fedora package (based on specfile by Dag Wieers, thanks!)
