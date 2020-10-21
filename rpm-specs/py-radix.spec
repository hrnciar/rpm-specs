Name: py-radix
Summary: Radix tree data structure for Python
Version: 0.9.3
Release: 19%{?dist}

URL: https://github.com/mjschultz/py-radix
Source0: https://github.com/mjschultz/py-radix/archive/v%{version}.tar.gz

License: BSD with advertising
BuildRequires: gcc

%description
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%package -n python3-%{name}
Summary: Radix tree data structure for Python

BuildRequires: python3-devel
BuildRequires: python3-setuptools
# Needed for tests
BuildRequires: python3-coverage
BuildRequires: python3-nose

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%prep
%setup -q
rm -f inet_ntop.c strlcpy.c
touch inet_ntop.c strlcpy.c

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{name}
%doc README.rst
%license LICENSE
%{python3_sitearch}/py_radix*
%{python3_sitearch}/radix*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-12
- Subpackage python2-py-radix has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-5
- Rebuild for Python 3.6

* Thu Jul 21 2016 Charalampos Stratakis <cstratak@redhat.com> 0.9.3-4
- Provide python 3 subpackage
- Renamed python 2 (sub)package
- Modernize SPEC

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Kevin Fenzi <kevin@scrye.com> 0.9.3-1
- Update to 0.9.3
- Enable tests in check
- Point to new upstream site/repo

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Oct 23 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-6
- Add patch by Alexander Sabourenkov to fix memory leak (Debian #512830)

* Mon Oct 12 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-5
- remove inet_ntop.c and strlcpy.c for safety.  They're only used on
  Windows.

* Thu Oct  1 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-4
- more package cleanups during review
  - quiet setup, clean buildroot at install, drop python Requires,
    add dist tag.

* Thu Oct  1 2009 Matt Domsch <mdomsch@fedoraproject.org> - 0.5-2
- update for Fedora packaging guidelines

* Wed Jun 28 2006 Damien Miller <djm@mindrot.org>
- Build RPM
