%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

Summary:        Python binding for the libssh2 library
Name:           libssh2-python
Version:        0.7.1
Release:        27%{?dist}
License:        LGPLv2+
URL:            https://github.com/wallunit/ssh4py
# The source for the package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://github.com/wallunit/ssh4py.git
#  cd ssh4py ; python setup.py sdist
Source0:        https://github.com/wallunit/ssh4py/zipball/0.7.1/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libssh2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%global _description\
libssh2-python is a python binding for the libssh2 library\


%description %_description

%package -n python3-libssh2
Summary:        %summary
%{?python_provide:%python_provide python3-libssh2}

%description -n python3-libssh2 %_description


%prep
%setup -q


%build
%py3_build


%install
%py3_install


%files -n python3-libssh2
%doc README.txt COPYING
%{python3_sitearch}/libssh2.*.so
%{python3_sitearch}/libssh2*-*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-27
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-25
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-22
- Remove python2 subpackage (#1627364)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-20
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

*Thu Aug 24 2017 Jan Beran <jberan@redhat.com> - 0.7.1-18
- Python 3 subpackage

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.1-17
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.1-16
- Python 2 binary package renamed to python2-libssh2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 08 2011 Chris Lalancette <clalance@redhat.com> - 0.7.1-3
- Fix license to LGPLv2+
- Add the github zipball location

* Mon Mar 14 2011 Chris Lalancette <clalance@redhat.com> - 0.7.1-2
- Update to the spec file for missing BuildRequires
- Update to latest upstream to include missing license files

* Fri Feb 25 2011 Chris Lalancette <clalance@redhat.com> - 0.7.1-1
- Update to latest upstream

* Fri Jan 28 2011 Chris Lalancette <clalance@redhat.com> - 0.6.9-1
- Initial build.
