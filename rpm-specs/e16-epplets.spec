Summary:          Epplets for Enlightenment, DR16
Name:             e16-epplets
Version:          0.15
Release:          8%{?dist}
License:          MIT with advertising and GPL+ and GPLv2+
URL:              http://www.enlightenment.org/
Source0:          http://downloads.sourceforge.net/enlightenment/e16-epplets-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:    freeglut-devel
BuildRequires:    imlib2-devel
BuildRequires:    mesa-libGLU-devel
Requires:         e16 >= 0.16.8
%description
Epplets are small, handy Enlightenment applets, similar to dockapps or
applets for other packages.  The epplets package contains the base
epplet API library and header files, as well as the core set of
epplets, including CPU monitors, clocks, a mail checker, mixers, a
slideshow, a URL grabber, a panel-like toolbar, and more.

%package          devel
Summary:          Development tools for epplets
Requires:         %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains the header files and libs
for developing epplets for Enlightenment, DR16

%prep
%autosetup

%build
%{__sed} -i -e 's/-rpath $(libdir)//' epplets/Makefile.in
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libepplet{,_glx}.{a,la}

%ldconfig_scriptlets

%files
%doc ChangeLog 
%{_libdir}/libepplet.so.*
%{_libdir}/libepplet_glx.so.*
%{_bindir}/E*.epplet
%{_datadir}/e16/epplet_icons
%{_datadir}/e16/epplet_data

%files devel
%{_includedir}/epplet.h
%{_libdir}/libepplet.so
%{_libdir}/libepplet_glx.so

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Terje Rosten <terje.rosten@ntnu.no> - 0.15-1
- 0.15

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Terje Rosten <terjeros@phys.ntnu.no> - 0.14-1
- 0.14

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Terje Rosten <terjeros@phys.ntnu.no> - 0.12-4
- Add DSO patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan  8 2009 Terje Rosten <terjeros@phys.ntnu.no> - 0.12-1
- 0.12

* Sat Dec 27 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.10-4
- Use Dejavu fonts

* Tue Apr 15 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.10-3
- Remove .{a,la} files
- Remove post requires
- Add mesa-libGLU-devel and freeglut-devel to build req

* Thu Mar 27 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.10-2
- Fix license

* Mon Aug 20 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.10-1
- Initial build (based on upstream spec, thanks!)
