
Summary:	A multi-purpose desktop calculator for GNU/Linux
Name:		qalculate-kde
Version:	0.9.7.10
Release:	28.nmu1%{?dist}

License:	GPLv2+
URL:		http://qalculate.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/qalculate/qalculate-kde4/kqalculate_%{version}+nmu1.tar.gz
Patch0:	qalculate-kde-0.9.7.10-gcc10.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  pkgconfig(libqalculate)

Requires:	gnuplot

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.

This package provides a KDE graphical interface for Qalculate!


%prep
%autosetup -c -p1

%build

%if 0%{?fedora} > 23
export CXXFLAGS="%{optflags} -std=gnu++98"
%endif

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING
%license COPYING
%{_kde4_bindir}/kqalculate
%{_kde4_datadir}/applications/kde4/qalculate_kde.desktop
%{_kde4_appsdir}/kqalculate/
%{_kde4_iconsdir}/hicolor/*/*/*


%changelog
* Tue Mar 10 2020 Than Ngo <than@redhat.com> - 0.9.7.10-28.nmu1
- Fix FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-27.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-26.nmu1
- rebuild for libqalculate

* Tue Aug 27 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-25.nmu1
- rebuild for libqalculate

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-24.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-23.nmu1
- rebuild for libqalculate

* Sat Mar 23 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-22.nmu1
- rebuild for libqalculate

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-21.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-20.nmu1
- rebuild for libqlaculate.so.20

* Tue Aug 21 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-19.nmu1
- rebuild for libqalculate.so.19()

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-18.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-17.nmu1
- rebuild for libqalculate.so.18()

* Fri May 18 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-16.nmu1
- rebuild for libqalculate.so.17()

* Wed Apr 11 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-15.nmu1
- rebuild for libqalculate.so.16()

* Sat Mar 10 2018 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-14.nmu1
- rebuild for libqalculate.so.14()

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-13.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7.10-12.nmu1
- Remove obsolete scriptlets

* Fri Sep 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.7.10-11.nmu1
- rebuild (libqalculate)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-10.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-9.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-8.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9.7.10-7.nmu1
- rebuild for libqalculate.so.6

* Fri Feb 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.7.10-6.nmu1
- qalculate-kde: FTBFS in rawhide (#1307960)
- .spec cosmetics 

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.10-5.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7.10-4.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.7.10-3.nmu1
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7.10-2.nmu1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.7.10-1.nmu1
- kqalculate_0.9.7.10+nmu1 (initial kde4 support)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.7-8
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.9.7-6
- Fix FTBFS with g++ 4.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Deji Akingunola <dakingun@gmail.com> - 0.9.7-2
- BR desktop-file-utils to build on F15

* Fri Jan 29 2010 Deji Akingunola <dakingun@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 Deji Akingunola <dakingun@gmail.com> - 0.9.6-8
- Rebuild for cln-1.3.0

* Thu Feb 26 2009 Deji Akingunola <dakingun@gmail.com> - 0.9.6-7
- Rebuild after the last rebuild failed because of kdelibs4/3 conflicts

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-5
- Rebuild for cln-1.2

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-4
- Rebuild for gcc43

* Thu Jan 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-3
- Now BR kdelibs3 instead of kdelibs

* Sat Aug 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- License tag update

* Sun Jul 01 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-1
- Update to new release

* Sat Jun 09 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-2
- Modify the Name field in the desktop file to distinguish it from that of
  qalculate-gtk (BZ #241024)

* Tue Jan 02 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- New release

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-3
- Rebuild for FC6

* Mon Jul 24 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-2
- Add another BR on autoconf and automake16

* Wed Jun 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-1
- New version 0.9.4

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3.1-2
- Update the icons location

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3.1-1
- Update to newer version

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.2-2
- Rebuild for Fedora Extras 5

* Tue Dec 27 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.2-1
- Upgrade to new version

* Sat Nov 05 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.0-1
- Upgrade to new version

* Thu Oct 13 2005 Paul Howarth <paul@city-fan.org> - 0.8.2-2
- Rationalise buildreqs and runtime dependencies
- Rationalise desktop entries
- Use standard Fedora Extras idioms for QT env setup & file lists
- Add %%clean section
- Don't generate rpaths
- Don't include empty TODO file

* Tue Oct 11 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-1
- Upgraded to new version
- Install the desktop file
- Miscellaneous spec file cleanup

* Wed Oct 05 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.1.1
- Initial package
