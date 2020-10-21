Name:		python-pysctp 
Version:	0.6
Release:	25%{?dist}
Summary:	Python sctp socket api extensions bindings
License:	LGPLv2
URL:		http://epx.com.br/pysctp/
Source0:	https://github.com/philpraxis/pysctp/archive/%{version}.tar.gz
Source1:	__init__.py
BuildRequires:  gcc python3-setuptools lksctp-tools-devel 
BuildRequires:	python3-devel python3

Patch0: pysctp-buildfix.patch
Patch1: pysctp-python3-update.patch

%global _description\
Python bindings for the SCTP socket api (see draft-ietf-tsvwg-sctpsocket-10.txt)

%description %_description

%package -n python3-pysctp
Summary: %summary
Requires:	python3 lksctp-tools-devel
%{?python_provide:%python_provide python2-pysctp}

%description -n python3-pysctp %_description

%prep
%setup -q -n pysctp-%{version}
mkdir ./pysctp
cp %{SOURCE1} .
%patch1 -p1 

%build
%py3_build

%install
%py3_install
rm -f $RPM_BUILD_ROOT/usr/*.[ch]

%files -n python3-pysctp
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/_sctp.*
%{python3_sitearch}/pysctp-*
%{python3_sitearch}/sctp.*

%doc README 

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.6-18
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6-17
- Rebuild for new binutils

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-16
- Fix broken filelist

* Mon Jul 23 2018 Neil Horman <nhorman@redhat.com> -0.6-15
- Update for python3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6-11
- Python 2 binary package renamed to python2-pysctp
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-3
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Neil Horman <nhorman@redhat.com> - 0.6-1
* Updated to latest upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Nov 20 2009 Neil Horman <nhorman@tuxdriver.com> - 0.3.1-9
- Update BuildRequires (bz 539152)

* Fri Nov 20 2009 Neil Horman <nhorman@tuxdriver.com> - 0.3.1-8
- Update BuildRequires (bz 539152)

* Fri Nov 20 2009 Neil Horman <nhorman@tuxdriver.com> - 0.3.1-7
- Update makefile for latest python release (bz 539152)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3.1-4
- Rebuild for Python 2.6

* Wed Sep 10 2008 Neil Horman <nhorman@tuxdriver.com> 0.3-1-3 
- Fixed files section, last minute pre-import fixes

* Wed Sep 10 2008 Neil Horman <nhorman@tuxdriver.com> 0.3.1-2
- Updated spec file with documentation

* Thu Apr 10 2008 Neil Horman <nhorman@tuxdriver.com> 0.3.1-1
- Initial build
