# the tests requires internet access, with pip install being run
# so they are disabled for now, since koji block outgoing connexion
%global with_tests 0

Name: bandit
Version: 1.6.2
Release: 1%{?dist}
Summary: A framework for performing security analysis of Python source code
License: ASL 2.0
URL: https://github.com/PyCQA/bandit
Source0: https://files.pythonhosted.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: python3-PyYAML
Requires: python3-stevedore
Requires: python3-appdirs
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if 0%{?with_tests}
BuildRequires: python3-pip
%endif
BuildRequires: python3-pbr

%description
Bandit provides a framework for performing security analysis of Python source
code, utilizing the ast module from the Python standard library.

The ast module is used to convert source code into a parsed tree of Python
syntax nodes. Bandit allows users to define custom tests that are performed
against those nodes. At the completion of testing, a report is generated
that lists security issues identified within the target source code.
%prep
%autosetup

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
%if 0%{?with_tests}
tox -epy27
%endif

%files
%doc AUTHORS ChangeLog README.rst
%doc doc
%doc examples
%license LICENSE
%{_bindir}/bandit
%{_bindir}/bandit-baseline
%{_bindir}/bandit-config-generator
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 06 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.6.2-1
- Version bump

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-13
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Marek Cermak <macermak@redhat.com> - 1.4.0-4
- new formatter (custom)

* Mon Nov 27 2017 Marek Cermak <macermak@redhat.com> - 1.4.0-3
- new formatter (yaml)

* Mon Nov 27 2017 Marek Cermak <macermak@redhat.com> - 1.4.0-2
- reformat setup.cfg

* Tue Sep 19 2017 Marek Cermak <macermak@redhat.com> - 1.4.0-1
- new version 1.4.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages


* Thu Apr 21 2016 Michael Scherer <misc@zarb.org> - 1.0.1-1
- update to 1.0.1
- port to python3
- drop the /etc configuration directory, as upstream did remove config file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 Michael Scherer <misc@zarb.org> 0.13.2-1
- new version 0.13.2
- add requires on python-stevedore, fix #1254589

* Sat Jul 11 2015 Michael Scherer <misc@zarb.org> 0.12.0-1
- new version 0.12.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Michael Scherer <misc@zarb.org> 0.11.0-1
- new version 0.11.0

* Fri May 01 2015 Michael Scherer <misc@zarb.org> 0.10.1-1
- Initial package
