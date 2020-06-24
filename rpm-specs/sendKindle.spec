Name:           sendKindle
Version:        3
Release:        7%{?dist}
Summary:        CLI tool for sending files via email to your Amazon Kindle device
BuildArch:      noarch
License:        AGPLv3+
URL:            https://github.com/kparal/sendKindle
Source0:        https://github.com/kparal/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       python3-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Send files as email attachments to your Amazon Kindle device. IMAP access
to your email account is required.

%prep
%setup -q
# Installation removed the executable bit, rpmlint then complains,
# let's remove the hashbang
# https://fedoraproject.org/wiki/Packaging_tricks#Remove_shebang_from_Python_libraries
sed '1{\@^#!/usr/bin/python3@d}' sendKindle.py > sendKindle.py.new
touch -r sendKindle.py{,.new}
mv sendKindle.py{.new,}

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/sendKindle
%{python3_sitelib}/*
%doc README.rst
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Kamil Páral <kparal@redhat.com> - 3-1
- new upstream version 3 (python3-only)

* Mon Jul 16 2018 Kamil Páral <kparal@redhat.com> - 2.1-14
- fix building on Rawhide (explicitly use python2)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Kamil Páral <kparal@redhat.com> - 2.1-4
- Change BR: python-setuptools-devel to python-setuptools
  https://lists.fedoraproject.org/pipermail/devel/2013-November/191344.html

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Kamil Páral <kparal@redhat.com> - 2.1-2
- Add python-setuptools dependency (#982243)

* Thu Nov 15 2012 Kamil Páral <kparal@redhat.com> - 2.1-1
- New package for Fedora
