Summary:       The gerrit client tools
Name:          gerrymander
Version:       1.5
Release:       19%{?dist}
Source0:       https://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
URL:           https://pypi.python.org/pypi/gerrymander
License:       ASL 2.0

BuildArch:     noarch

BuildRequires: python3-nose
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-gerrymander

%package -n python3-gerrymander
Summary: The gerrit python3 client
License: GPLv2+
%{?python_provide:%python_provide python3-gerrymander}


%description
The gerrymander package provides a set of command line tools
for interacting with Gerrit

%description -n python3-gerrymander
The python3-gerrymander package provides a set of python3
modules for interacting with Gerrit.

%prep
%setup -q
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

# Remove any egg info (as of submitting this review, there's no bundled
# egg info)
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
# setup.py's integration does 'python3 /usr/bin/nosetests', which isn't
# going to work. So we'll just call nosetests ourselves.
nosetests-%{python3_version}

%files
%doc conf/gerrymander.conf-example
%{_bindir}/gerrymander

%files -n python3-gerrymander
%doc README LICENSE
%{python3_sitelib}/gerrymander/
%{python3_sitelib}/%{name}-%{version}-py3.*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5-19
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-16
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5-13
- Remove python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.5-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5-8
- Python 2 binary package renamed to python2-gerrymander
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.5-6
- Fix Python 2 dependency in gerrymander (RHBZ#1422897)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 1.5.4
- fix test invocation for Python 3

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 29 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.5.2
- Add the Python PrettyTable dependency to relevant sub-packages
  (Thanks, Daniel Berrange, Matthew Booth)

* Mon Feb 22 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.5.1
- New upstream release 1.5

* Tue Feb 16 2016 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.4.5
- Add 'python-prettytable' to 'Requires'; fixes rhbz# 1307167

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.4.1
- Update to new upstream release 1.4
- Change the official source to pypi (from github generated tarballs)
- Change the URL to pypi

* Wed Aug 20 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.4
- Remove with_python3 conditional, as current Fedora releases have it

* Tue Aug 19 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.3
- Update %%files section correctly

* Mon Aug 18 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3.2
- Address review comments from rhbz# 1128253

* Tue Aug 05 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.3-1
- Initial package
