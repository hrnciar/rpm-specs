# Python2 macros for EPEL
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global pypi_name gerrit-view


Name:           python-gerrit-view 
Version:        0.4.6
Release:        5%{?dist}
Summary:        A set of tools to query/view Gerrit patch reviews and their Zuul status

License:        ASL 2.0 
URL:            https://pypi.org/project/gerrit-view/
Source0:        https://pypi.python.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-urwid
BuildRequires:  python3-requests

%global _description\
A set of tools to query/view Gerrit patch reviews and their status.\
Current set of tools: (1) qgerrit -- to query different projects' Gerrit\
reviews based on a set of criteria/filters; (2) cgerrit -- to view (in\
real time) Gerrit reviews on CLI; (3) czuul -- to view Gerrit reviews'\
Zuul (a pipeline oriented project gating and automation system) status\
on CLI.

%description %_description

%package -n python3-gerrit-view
Summary: %summary
Requires: python3-gerritlib
Requires: python3-requests
Requires: python3-six
Requires: python3-prettytable
Requires: python3-urwid
Requires: python3-paramiko
Requires: python3-GitPython
%{?python_provide:%python_provide python3-gerrit-view}

%description -n python3-gerrit-view %_description

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf gerrit_view.egg-info

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

%files -n python3-gerrit-view
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/gerrit_view-%{version}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Kashyap Chamarthy <kchamart@redhat.com>
- Update the URL to correct location (rhbz#1374659)

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.2-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.2-7
- Python 2 binary package renamed to python2-gerrit-view
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.2-1
- New upstream release - 0.3.2

* Wed Feb 26 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.0-3
- Remove duplicate entry of python-urwid from Requires

* Tue Feb 25 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.0-2
- Address "File listed twice" warnings

* Tue Feb 25 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.0-1
- Initial package

