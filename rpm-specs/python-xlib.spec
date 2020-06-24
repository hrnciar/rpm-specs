%if 0%{?fedora} >= 32 || 0%{?rhel} >= 8
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-xlib
Version:        0.26
Release:        3%{?dist}
Summary:        X client library for Python

License:        LGPLv2+
URL:            https://github.com/python-xlib/python-xlib
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xorg.conf
# tests need to import tohex
# https://github.com/python-xlib/python-xlib/pull/75
Patch1:         python-xlib-tohex.patch
Patch2:         fix-ssh-tunnel-auth 
# Remove failing test
# https://github.com/python-xlib/python-xlib/issues/1
Patch4:         python-xlib-test.patch

BuildArch:      noarch
BuildRequires:  texinfo-tex
BuildRequires:  tex(dvips)
# For tests
BuildRequires:  xorg-x11-drv-dummy

%description
The Python X Library is a complete X11R6 client-side implementation, 
written in pure Python. It can be used to write low-levelish X Windows 
client applications in Python.

%if %{with python2}
%package -n python2-xlib
Summary:        X client library for Python 2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-six >= 1.10.0
# For tests
BuildRequires:  python2-mock
Requires:       python2-six >= 1.10.0
%{?python_provide:%python_provide python2-xlib}

%description -n python2-xlib
The Python X Library is a complete X11R6 client-side implementation, 
written in pure Python. It can be used to write low-levelish X Windows 
client applications in Python 2.
%endif

%package -n python%{python3_pkgversion}-xlib
Summary:        X client library for Python 3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-six >= 1.10.0
# For tests
BuildRequires:  python%{python3_pkgversion}-mock
Requires:       python%{python3_pkgversion}-six >= 1.10.0
%{?python_provide:%python_provide python%{python3_pkgversion}-xlib}

%description -n python%{python3_pkgversion}-xlib
The Python X Library is a complete X11R6 client-side implementation, 
written in pure Python. It can be used to write low-levelish X Windows 
client applications in Python 3.

%package doc
Summary:        Documentation and examples for python-xlib
BuildRequires:  texi2html

%description doc
Install this package if you want the developers' documentation and examples
that tell you how to program with python-xlib.

%prep
%autosetup -p1

%build
%if %{with python2}
%py2_build
%endif
%py3_build
cd doc
make html ps
cd html
rm Makefile

%install
%if %{with python2}
%py2_install
%endif
%py3_install
chmod a-x examples/*.py

%check
# Note - tests fail on big-endian, see https://github.com/python-xlib/python-xlib/issues/76
cp %SOURCE1 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
elif [ -x /usr/libexec/Xorg.bin ]; then
   Xorg=/usr/libexec/Xorg.bin
else
   Xorg=/usr/bin/Xorg
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99
%if %{with python2}
%__python2 setup.py test
%endif
%__python3 setup.py test
kill %1 || :
cat xorg.log
 
%if %{with python2}
%files -n python2-xlib
%license LICENSE
%doc CHANGELOG.md README.rst TODO
%{python2_sitelib}/*
%endif

%files -n python%{python3_pkgversion}-xlib
%license LICENSE
%doc CHANGELOG.md README.rst TODO
%{python3_sitelib}/*

%files doc
%license LICENSE
%doc examples doc/html doc/ps/python-xlib.ps


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.26-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26-1
- Update to 0.26

* Tue Nov 26 2019 Orion Poplawski <orion@cora.nwra.com> - 0.25-1
- Update to 0.25

* Tue Oct 29 2019 Orion Poplawski <orion@cora.nwra.com> - 0.23-8
- Drop python2 for Fedora 32+ (bz#1764881)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.23-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.23-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Orion Poplawski <orion@cora.nwra.com> - 0.23-1
- Update to 0.23

* Fri Apr 13 2018 Orion Poplawski <orion@cora.nwra.com> - 0.20-4
- Use Xdummy for tests, remove failing one.

* Thu Apr 12 2018 Orion Poplawski <orion@cora.nwra.com> - 0.20-3
- Fix dvips BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Orion Poplawski <orion@cora.nwra.com> - 0.20-1
- Update to 0.20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 1 2017 Orion Poplawski <orion@cora.nwra.com> - 0.19-2
- Add patch to fix test error

* Tue Feb 28 2017 Orion Poplawski <orion@cora.nwra.com> - 0.19-1
- Update to 0.19
- Drop upstreamed patches

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.17-2
- Rebuild for Python 3.6

* Fri Sep 30 2016 Orion Poplawski <orion@cora.nwra.com> - 0.17-1
- Update to 0.17
- License changed to LGPLv2+
- Ship python3-xlib (bug #1360713)
- Modernize spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-0.12.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> - 0.15-0.11.rc1
- Add patch to fix perl usage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.11.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.10.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.9.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.7.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jun 04 2011 Luke Macken <lmacken@redhat.com> - 0.15-0.5.rc1
- Apply a couple of patches from upstream:
    * r139 - Accept IPv6 addresses in Xlib.display.Display
    * r138 - Remove a stray print statement

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep  3 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.15-0.3.rc1
- try a workaround proposed by upstream for #552491

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.15-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Dec 14  2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.15-0.1.rc1
- New upstream pre-release and some cherry picked patches from Debian from Fedora bug 537264 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.14-3
- Rebuild for Python 2.6

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.14-2
- fix license tag

* Tue Jul 1 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.14-1
- Latest upstream release

* Tue Apr 10 2007 Jef Spaleta <jspaleta@gmail.com> - 0.13-3
- Created doc subpackage per suggestion in review

* Mon Mar 26 2007 Jef Spaleta <jspaleta@gmail.com> - 0.13-2
- Review Cleanup

* Sat Mar 24 2007 Jef Spaleta <jspaleta@gmail.com> - 0.13-1
- Initial packaging

