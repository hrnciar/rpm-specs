%{?python_enable_dependency_generator}
%global commit 87dd1d8fb60ba6d6524d4ae49586e596d7cda759
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner Yubico

Name:           yubikey-manager
Version:        3.1.1
Release:        2.git%{shortcommit}%{?dist}
Summary:        Python library and command line tool for configuring a YubiKey

License:        BSD
URL:            https://github.com/%{owner}/%{name}/
Source0:        https://github.com/%{owner}/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  python3-devel swig pcsc-lite-devel ykpers
# install_requires from setup.py
BuildRequires:  %{py3_dist six pyscard pyusb click cryptography pyopenssl fido2}
Requires:       python3-%{name} python3-setuptools u2f-hidraw-policy

%description
Command line tool for configuring a YubiKey.

%package -n python3-%{name}
Summary:        Python library for configuring a YubiKey
Requires:       ykpers pcsc-lite

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python library for configuring a YubiKey.

%prep
%autosetup -n %{name}-%{commit}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{name}
%license COPYING
%doc NEWS
%{python3_sitelib}/*

%files
%{_bindir}/ykman

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-2.git87dd1d8
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Gerald Cox <gbcox@fedoraproject.org> - 3.1.1-1.git87dd1d8
- Upstream release rhbz#1796504

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8.git1f22620
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Gerald Cox <gbcox@fedoraproject.org - 3.0.0-7.git1f22620
- PCSC Exceptions - rhbz#1684945

* Thu Oct 24 2019 Gerald Cox <gbcox@fedoraproject.org - 3.0.0-6.gitcfa1907
- PCSC Exceptions - rhbz#1684945 rhbz#1737264

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-5.gitcfa1907
- Require python3-setuptools explicitly

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-4.gitcfa1907
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-3.gitcfa1907
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.0.0-2.gitcfa1907
- Upstream release - rhbz#1737243

* Sun Aug 04 2019 Gerald Cox <gbcox@fedoraproject.org> - 3.0.0-1.gitcfa1907
- Upstream release - rhbz#1737243

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3.gitb44d719
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.0-2.gitb44d719
- Upstream release - rhbz#1703827

* Sun Apr 28 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.1.0-1.gitb44d719
- Upstream release - rhbz#1703827

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4.gite17b3de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Gerald Cox <gbcox@fedoraproject.org> - 2.0.0-3.gite17b3de
- Upstream release - rhbz#1655888

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-2.git1c707b2
- Enable python dependency generator

* Mon Dec 31 2018 Gerald Cox <gbcox@fedoraproject.org> - 2.0.0-1.git1c707b2
- Upstream release - rhbz#1655888

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.7

* Mon May 7 2018 Seth Jennings <sethdjennings@gmail.com> - 0.6.0-2
- add u2f-host as dependency

* Wed May 2 2018 Seth Jennings <sethdjennings@gmail.com> - 0.6.0-1
- Upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 9 2017 Seth Jennings <sethdjennings@gmail.com> - 0.4.0-1
- New package
- Upstream release
