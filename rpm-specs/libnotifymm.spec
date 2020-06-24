%define apiver 1.0

Name:           libnotifymm
Version:        0.7.0
Release:        15%{?dist}
Summary:        C++ interface for libnotify

License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libnotifymm/0.6/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel >= 2.28.0
BuildRequires:  gtkmm30-devel >= 3.4.1
BuildRequires:  libnotify-devel >= 0.7.5
BuildRequires:  doxygen graphviz


%description
libnotifymm provides a C++ interface to the libnotify
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.


%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtkmm24-devel%{?_isa}
Requires:       libnotify-devel%{?_isa}


%description devel
This package contains the libraries and header files needed for
developing %{name} applications.


%prep
%setup -q


%build
%configure --disable-static --enable-reference --disable-dependency-tracking
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%buildroot INSTALL="install -p"

# move installed documentation for %%doc usage in -devel subpackage
rm -rf __tmp_doc ; mkdir __tmp_doc
mv %{buildroot}%{_datadir}/doc/%{name}-%{apiver}/reference __tmp_doc

find %buildroot -type f -name "*.la" -exec rm -f {} ';'
# Remove code-generation related files
rm -rf %buildroot%{_libdir}/%{name}-%{apiver}


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*


%files devel
%doc __tmp_doc/reference/*
%{_includedir}/%{name}-%{apiver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/devhelp/books/%{name}-1.0

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.0-2
- fix duplicate documentation (#1001237)
- move installed documentation for %%doc usage in -devel subpackage
- use %%?_isa in -devel package deps

* Tue Aug 06 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 0.7.0-1
- upstream 0.7.0
- refresh spec
- fix unversionned docdir (RHBZ #993820)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.6.1-10
- Resolves: rhbz#661037 bodge in removal of old libnotify api

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 11 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.6.1-8
- Rebuilt for F-13

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Denis Leroy <denis@poolshark.org> - 0.6.1-5
- Fixed unowned directory issue (#483467)

* Wed Jan 14 2009 Denis Leroy <denis@poolshark.org> - 0.6.1-4
- Removed closesig patch

* Fri Dec 26 2008 Denis Leroy <denis@poolshark.org> - 0.6.1-3
- Added sed line to quiet rpmlint

* Fri Sep  5 2008 Denis Leroy <denis@poolshark.org> - 0.6.1-2
- Added patch to address libnotify rawhide API breakage

* Thu Sep  4 2008 Denis Leroy <denis@poolshark.org> - 0.6.1-1
- Initial version

