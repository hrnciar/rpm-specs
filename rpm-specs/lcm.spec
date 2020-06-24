# vim: set ts=4 sw=4 et: coding=UTF-8

Name:           lcm
Version:        1.4.0
Release:        1%{?dist}
License:        LGPLv2+
Summary:        Utilities for lightweight communications and marshaling
URL:            https://lcm-proj.github.io/
Source:         https://github.com/lcm-proj/lcm/releases/download/v%{version}/%{name}-%{version}.zip

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  python3-devel

%description
LCM is a library for message passing and data marshaling targeted at real time
systems where high-bandwidth and low latency are critical.
It provides a publish/subscribe message passing model and a XDR-style message
specification language with bindings for applications in C, Java and Python.


%package java
Summary:        Lightweight communications and marshaling java artifacts
BuildArch:      noarch
BuildRequires:  java-devel >= 1:1.6.0
Requires:       java-headless >= 1:1.6.0
Requires:       javapackages-filesystem

%description java
LCM is a library for message passing and data marshaling targeted at real time
systems where high-bandwidth and low latency are critical.

This package provides the java stuff...


%package javadoc
Summary:        Lightweight communications and marshaling java artifacts documentation
BuildArch:      noarch

%description javadoc
LCM is a library for message passing and data marshaling targeted at real time
systems where high-bandwidth and low latency are critical.

This package provides the java documentation.


%package -n python3-%{name}
Summary:        Lightweight communications and marshaling Python 3 bindings
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
LCM is a library for message passing and data marshaling targeted at real time
systems where high-bandwidth and low latency are critical.


%package devel
Summary:        Lightweight communications and marshaling development files
Requires:       %{name}%{?_isa}        = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-java           = %{version}-%{release}

%description devel
LCM is a library for message passing and data marshaling targeted at real time
systems where high-bandwidth and low latency are critical.

This package provides the development files for the various lcm packages.


%prep
%setup -q

%build
%cmake . -DLCM_JAVA_TARGET_VERSION=
%make_build
( cd lcm-java && ./make-javadocs.sh )

%install
%make_install
# install javadocs
install -d %{buildroot}%{_javadocdir}
cp -pr lcm-java/javadocs %{buildroot}%{_javadocdir}/%{name}
# remove static library
rm %{buildroot}%{_libdir}/liblcm.a
# remove bundled jars
rm %{buildroot}%{_datadir}/java/{jchart2d,jide-oss,xmlgraphics-commons}*.jar

%check
# Tests are still written assuming Python 2, fail on Python 3 :-(
ctest -V %{?_smp_mflags} || :


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/lcm-example
%{_bindir}/lcm-gen
%{_bindir}/lcm-logfilter
%{_bindir}/lcm-logger
%{_bindir}/lcm-logplayer
%{_bindir}/lcm-sink
%{_bindir}/lcm-source
%{_bindir}/lcm-tester
%{_mandir}/man1/*.1.gz
%{_libdir}/liblcm.so.*
# man pages which go on java sub-package
%exclude %{_mandir}/man1/lcm-logplayer-gui.1.gz
%exclude %{_mandir}/man1/lcm-spy.1.gz


%files java
%license COPYING
%doc AUTHORS COPYING
%{_bindir}/lcm-logplayer-gui
%{_bindir}/lcm-spy
%{_datadir}/java/lcm.jar
%{_mandir}/man1/lcm-logplayer-gui.1.gz
%{_mandir}/man1/lcm-spy.1.gz


%files javadoc
%license COPYING
%doc AUTHORS COPYING
%{_javadocdir}/%{name}/


%files -n python3-%{name}
%{python3_sitearch}/lcm/


%files devel
%{_includedir}/%{name}/
%{_libdir}/liblcm.so
# cmake helpers live in /usr/lib64/lcm/cmake/
%{_libdir}/%{name}
%{_libdir}/pkgconfig/lcm.pc
%{_libdir}/pkgconfig/lcm-java.pc
%{_datadir}/aclocal/lcm.m4


%changelog
* Sat Jun 13 2020 Dan Callaghan <djc@djc.id.au> - 1.4.0-1
- update to upstream release 1.4.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-17
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-14
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-12
- Package python2-lcm was removed (#1629812)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-9
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Dan Callaghan <dcallagh@redhat.com> - 1.3.1-8
- remove superfluous Obsoletes for lcm-python (RHBZ#1537212)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuild for Python 3.6

* Fri Aug 26 2016 Dan Callaghan <dcallagh@redhat.com> - 1.3.1-3
- clean up spec as per latest Fedora guidelines

* Wed Aug 24 2016 Tomas Orsava <torsava@redhat.com> - 1.3.1-2
- Added support for Python 3 — new subpackage python3-lcm
- The package is now being built two times, once with Python 2 bindings and
  the second time with Python 3 bindings
- Renamed subpackage lcm-python to python2-lcm, added Provides and Obsoletes
  for the name lcm-python

* Mon Aug 15 2016 Dan Callaghan <dcallagh@redhat.com> - 1.3.1-1
- new upstream release 1.3.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Dan Callaghan <dcallagh@redhat.com> - 1.3.0-1
- new upstream release 1.3.0

* Fri Jun 19 2015 Dan Callaghan <dcallagh@redhat.com> - 1.2.1-1
- new upstream release 1.2.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Dan Callaghan <dcallagh@redhat.com> - 0.9.2-4
- BZ#1022129, remove versioned .jar symlink as per new Java packaging guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Nelson Marques <nmarques@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2
- Upstream doesn't create the .jar versioned link, we do it on install

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Nelson Marques <nmo.marques@gmail.com> - 0.9.0-5
- Add "ExcludeArch: ppc ppc64" for el5 and el6, no java dependencies
- Update release to match the changelog

* Fri Jul 06 2012 Nelson Marques <nelson-m-marques@ext.ptinovacao.pt> - 0.9.0-1
- Update to version 0.9.0
- BZ#767649, moved java man pages to java sub-package

* Thu Jul 05 2012 Nelson Marques <nelson-m-marques@ext.ptinovacao.pt> - 0.7.1-3
- BZ#767649, updated buildroot and other improvements

* Tue Jul 03 2012 Nelson Marques <nelson-m-marques@ext.ptinovacao.pt> - 0.7.1-2
- BZ#767649, introduced recommended changes

* Mon Jul 02 2012 Nelson Marques <nelson-m-marques@ext.ptinovacao.pt> - 0.7.1-1
- BZ#767649, initial package from upstream release 0.7.1
