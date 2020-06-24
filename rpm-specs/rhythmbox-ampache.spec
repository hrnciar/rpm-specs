%global commit ca46005b9e492ecf2d6f14226c8b4b1e1e36957e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200105
%global debug_package %{nil}
%global py_install_args --no-glib-compile-schemas

Name:           rhythmbox-ampache
Version:        0
Release:        24.%{date}git%{shortcommit}%{?dist}
Summary:        Ampache plugin for Rhythmbox
License:        GPLv2+
URL:            https://github.com/lotan/rhythmbox-ampache
Source0:        https://github.com/lotan/rhythmbox-ampache/archive/%{commit}/%{name}-%{commit}.tar.gz
ExcludeArch:    s390 s390x
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       rhythmbox%{?_isa}

%description
The Rhythmbox Ampache Plugin is a plugin for the music player
Rhythmbox that enables browsing the metadata and streaming music
from an Ampache media server.

%prep
%autosetup -n %{name}-%{commit}

%build
%py3_build

%install
%py3_install -- %py_install_args

%files
%doc README
%license LICENSE
%{_libdir}/rhythmbox/plugins/ampache
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.plugins.ampache.gschema.xml
%{_datadir}/rhythmbox/plugins/ampache
%{python3_sitelib}/rhythmbox_ampache-*-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-24.20200105gitca46005
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20200105gitca46005
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-22.20200105gitca46005
- New git version ca46005

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-21.20170825git3946080
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20170825git3946080
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20170825git3946080
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20170825git3946080
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0-17.20170825git3946080
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20170825git3946080
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-15.20170825git3946080
- Fix py3_install macro call
- New git version 3946080

* Thu Aug 24 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-14.20170807git0d233e3
- Enquote py_install_args

* Wed Aug 23 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-13.20170807git0d233e3
- Drop support for s390 and s390x as rhythmbox does not support them (there is no gnome-media there)

* Tue Aug 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-12.20170807git0d233e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Aug 07 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-11.20170807git0d233e3
- New git version 0d233e3
- Add patch to use lib64 dir in s390x arch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20150518git7415a69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20150518git7415a69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20150518git7415a69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20150518git7415a69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20150518git7415a69
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 15 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-0.5.20150518git7415a69
- Disable debug package

* Mon Sep 14 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-0.4.20150518git7415a69
- Make the package arched
- Use python macros

* Mon Sep 14 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-0.3.20150518git7415a69
- Switch to python3

* Mon May 18 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-0.2.20150518git7415a69
- Upstream made glib-compile-schemas optional

* Thu May 14 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0-0.1.20150518git7c1d978
- Initial RPM release
