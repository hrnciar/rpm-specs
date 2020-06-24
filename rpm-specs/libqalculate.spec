%global srcnm Qalculate
%global libversion 21
%global libsymlink 9.0

Summary:	Multi-purpose calculator library
Name:		libqalculate
Version:	3.11.0
Release:	1%{?dist}
License:	GPLv2+

URL:		https://qalculate.github.io/
Source0:	https://github.com/%{srcnm}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	glib2-devel
BuildRequires:	cln-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	curl-devel
BuildRequires:	libicu-devel
BuildRequires:	mpfr-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	gettext
BuildRequires:	perl(Getopt::Long)

%description
This library underpins the Qalculate! multi-purpose desktop calculator for
GNU/Linux

%package	devel
Summary:	Development tools for the Qalculate calculator library
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel
Requires:	libxml2-devel
Requires:	cln-devel
Requires:	mpfr-devel

%description	devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%package -n	qalculate
Summary:	Multi-purpose calculator, text mode interface
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

Provides:	qalc

%description -n	qalculate
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides the text-mode interface for Qalculate! The GTK and QT
frontends are provided by qalculate-gtk and qalculate-kde packages resp.

%prep
%setup -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING
%{_libdir}/libqalculate.so.%{libversion}
%{_libdir}/libqalculate.so.%{libversion}.%{libsymlink}
%{_datadir}/qalculate/
%{_mandir}/man1/qalc.1.*

%files devel
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc
%{_includedir}/libqalculate/

%files -n qalculate
%{_bindir}/qalc

%changelog
* Mon Jun 22 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.11.0-1
- Update to 3.11.0

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 3.10.0-2
- Rebuild for ICU 67

* Tue May 12 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0

* Tue Apr 21 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.9.0a-1
- Update to 3.9.0

* Sat Mar 07 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.3.0-3
- Rebuild for ICU 65

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 3.3.0-2
- Rebuild for mpfr 4

* Tue Aug 27 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Sat Mar 23 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.2-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 2.8.2-2
- Rebuild for ICU 63

* Mon Jan 21 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.8.2-1
- Update to 2.8.2

* Wed Aug 15 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-1
- Fix spec file issues

* Wed Jul 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.6.0-2
- Rebuild for ICU 62

* Mon Jun 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0
- Drop upstreamed patch

* Fri May 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-2
- Fix segfault on basic operations

* Wed May 16 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.4.0-2
- Rebuild for ICU 61.1

* Wed Apr 11 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Mon Apr 09 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Wed Mar 07 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-6
- .spec cleanup, BR: gcc-c++, use %%ldconfig_scriptlets

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0.0-3
- Rebuild for ICU 60.1

* Thu Sep 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-2
- -devel: Requires: mpfr-devel
- use %%license

* Fri Sep 15 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0
- Drop older patches
- Update buildrequires (curl-devel, libicu-devel and mpfr-devel)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.10-5
- specfile cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.10-3
- rebuilt

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.10-2
- Rebuild for readline 7.x

* Mon Nov 28 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10

* Mon Apr 25 2016 Than Ngo <than@redhat.com> - 0.9.7-18
- bz#953615, fix global variable buffer

* Thu Feb 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.7-17
- Add BR:perl(Getopt::Long)
- Added doc to %%files section

* Tue Feb 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.7-16
- Added patch to fix GCC-6 FTBFS. Thanks Yaakov Selkowitz

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.7-14
- workaround (mostly) needless stderr spam: failed to load external entity .../eurofxref-daily.xml

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.7-12
- rebuild(gcc5), tighten subpkg deps via %%{?_isa}

* Mon Feb 23 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.7-11
- rebuild (gcc5)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Deji Akingunola <dakingun@gmail.com> - 0.9.7-8
- Fix for versioned docdir build error

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Rex Dieter <rdieter@fedorproject.org> - 0.9.7-2
- respin pkgconfig_private patch for implicit linkage (#564920)

* Fri Jan 29 2010 Deji Akingunola <dakingun@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Rex Dieter <rdieter@fedoraproject.org> 0.9.6-7
- move auto*foo to prep stage
- trim pkg-config-related deps (#509840)

* Sun Jul 05 2009 Deji Akingunola <dakingun@gmail.com> - 0.9.6-6
- Rebuild for cln-1.3.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-4
- Rebuild (with patch) for cln-1.2

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-3
- Rebuild for gcc43

* Sat Aug 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- License tag update

* Sun Jul 01 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-1
- Update to new release

* Tue Jan 02 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- New release

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-4
- Rebuild for FC6

* Wed Jun 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-3
- Arbitrarily bump the release field to fix broken update path

* Tue Jun 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-1
- New version 0.9.4

* Sun Apr 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3-2
- More BRs from Paul Howarth (#193481)

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3-1
- Update to newer version

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.2-2
- Rebuild for Fedora Extras 5

* Tue Dec 27 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.2-1
- Upgrade to new version

* Sat Nov 05 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.0-1
- Upgrade to new version

* Mon Oct 17 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-3
- Add patch to allow build with cln-1.1.10

* Mon Oct 17 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-2
- Bump the release tag to make even with FC-4 and FC-3 branches

* Tue Oct 11 2005 Paul Howarth <paul@city-fan.org> - 0.8.2-1
- Split off separate qalculate subpackage
- Update to 0.8.2

* Mon Oct 10 2005 Paul Howarth <paul@city-fan.org> - 0.8.1.2-2
- Don't include static libraries
- Include license text
- Don't include README, which only contains a URL
- Include AUTHORS & TODO
- Remove redundant manual dependencies
- Split off separate devel subpackage
- Be more explicit in %%files list
- Add %%post and %%postun scripts to run ldconfig
- Use DESTDIR with make instead of %%makeinstall
- Add buildreqs readline-devel and ncurses-devel

* Wed Oct 05 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.1.2-1
- Initial package
