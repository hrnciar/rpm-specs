Name:		surf-geometry
Version:	1.0.6
Summary:	Tool to visualize some real algebraic geometry
Release:	28%{?dist}
Source0:	http://downloads.sourceforge.net/surf/surf-%{version}.tar.gz
Source1:	%{name}.module.in
Patch0:		%{name}-min-max.patch
URL:		http://surf.sourceforge.net/
License:	GPLv2+
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	flex-static
BuildRequires:	cups-devel
BuildRequires:	gmp-devel
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libXmu-devel
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
Requires:	environment(modules)

%description
surf is a tool to visualize some real algebraic geometry:
plane algebraic curves, algebraic surfaces and hyperplane sections of surfaces.
surf is script driven and has (optionally) a nifty GUI using the Gtk widget set.

%prep
%setup -q -n surf-%{version}
%patch0 -p1

# Avoid extra directory and install binary and xpm file in same directory
sed -i 's|^\(pkgdatadir = $(datadir)\)/@PACKAGE@|\1|' Makefile.in
sed -i 's|/surf\(/surf\.xpm\)|\1|' gtkgui/showAbout.cc
chmod -x gtkgui/PrintImageDialog.{cc,h}

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="-std=c++14 $CFLAGS"

%configure \
    --bindir=%{_libdir}/%{name} \
    --datadir=%{_libdir}/%{name} \
    --with-gmp=%{_prefix} \
    --with-gtk=%{_prefix} \
    --with-x
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Based on 4ti2.spec
mkdir -p $RPM_BUILD_ROOT%{_datadir}/modulefiles
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    $RPM_BUILD_ROOT%{_datadir}/modulefiles/%{name}-%{_arch} 

mv $RPM_BUILD_ROOT%{_mandir}/man1/surf.1 \
    $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc AUTHORS
%doc ChangeLog
%license COPYING
%doc NEWS
%doc README
%doc TODO
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/modulefiles/%{name}-%{_arch}

%changelog
* Tue Aug 14 2020 Jeff Law <law@redhat.com> - 1.0.6-28
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.6-23
- Add BuildRequires: gcc-c++, fixes FTBFS (#1606453)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.6-20
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.6-16
- Correct FTBFS in rawhide (#1308163)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.6-14
- Require environment(modules), install into generic modulefiles location
- Use %%license

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.6-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.0.6-7
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.0.6-6
- rebuild against new libjpeg

* Thu Dec 20 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.6-5
- Adhere to Static Library Packaging Guidelines (#889176)

* Wed Aug 29 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.6-4
- Correct download link (#840244)
- Do not mix rpmbuild macros and environment variables (#840244)
- Consistently use %%{name} (#840244)
- Remove executable bit from some sources (#840244)

* Sun Aug 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.6-3
- Rename from Singular-surf to surf-geometry (#840244)
- Use enviroment-modules to avoid conflicts with surf package (#840244)

* Thu Jul 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.6-2
- Correct %%{?dist} tag.
- List base directory instead of directory and a single file.

* Sat Jul 14 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.0.6-1
- Initial Singular-surf spec.
