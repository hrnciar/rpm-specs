Name:           gconfmm26
Version:        2.28.3
Release:        20%{?dist}

Summary:        C++ wrapper for GConf2

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gconfmm/2.28/gconfmm-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= 2.6.4
BuildRequires:  gtkmm24-devel >= 2.4.0
BuildRequires:  GConf2-devel >= 2.4.0

%description
This package provides a C++ interface for GConf2. It is a sub-package
of the GTKmm project.  The interface provides a convenient interface
for C++ programmers to create Gnome GUIs with GTK+'s flexible
object-oriented framework.

%package devel
Summary:        Headers for developing programs that will use gconfmm
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-devel
Requires:       gtkmm24-devel
Requires:       GConf2-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use gconfmm, part of GTKmm, the C++
interface to the GTK+.


%prep
%setup -q -n gconfmm-%{version}
# convert README file to UTF-8 
iconv --from=ISO-8859-1 --to=UTF-8  README > README.new && \
touch -r README README.new && \
mv README.new README


%build
%configure --disable-static --enable-shared
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/gconfmm-2.6
%{_libdir}/gconfmm-2.6
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/devhelp/books/gconfmm-2.6/gconfmm-2.6.devhelp2
%{_datadir}/doc/gconfmm-2.6/reference/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.28.3-9
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.3-2
- Rebuilt for glibc bug#747377

* Sat Oct 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.28.3-1
- upstream 2.28.3
- fix documentation build with glibmm 2.28+

* Tue Oct 18 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.28.2-3
- fix FTBFS (patch from kalev)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 2.28.2-1
- Update to upstream 2.28.2
- Rename spec file according guidelines
- Rpmlint fixes

* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.28.0-1
- Update to upstream 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0

* Wed Mar 12 2008 Denis Leroy <denis@poolshark.org> - 2.22.0-1
- Update to upstream 2.22.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.20.0-2
- Autorebuild for GCC 4.3

* Mon Sep 17 2007 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to new stable 2.20.0

* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to Gnome 2.18, to follow GConf2 version

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-2
- FE6 Rebuild

* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to 2.16.0

* Sun Jun 25 2006 Denis Leroy <denis@poolshark.org> - 2.14.2
- Update to 2.14.2
- Added dist postfix to release field

* Mon Mar 20 2006 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to 2.14.0

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-3
- Rebuild

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-2
- Removed static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-1
- Update to 2.12.0

* Sat May  7 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-2
- Added patch to fix x86_64 compile

* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Upgrade to 2.10.0
- Added patch to fix gcc4 warning

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.6.1-0.fdr.1
- Upgrade to 2.6.1

* Fri Oct 31 2003 Michael Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.2
- Fix BuildRequires
- Add specific version numbers to GConf dependency.

* Sat Oct 18 2003 Michael Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.1
- Initial RPM creation
