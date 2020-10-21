%global _description\
Nyx is a command-line monitor for Tor. With this you can get detailed\
real-time information about your relay such as bandwidth usage,\
connections, logs, and much more.

Name:           nyx
Version:        2.1.0
Release:        6%{?dist}
Summary:        Command-line monitor for Tor
License:        GPLv3
URL:            https://nyx.torproject.org
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
# Tests
BuildRequires:  python3-stem
BuildRequires:  python3-pyflakes
Suggests:       %{name}-doc = %{version}-%{release}
Provides:       tor-arm = %{version}-%{release}
Obsoletes:      tor-arm <= 1.4.5.0-17
Obsoletes:      tor-arm-gui <= 1.4.5.0-17
Obsoletes:      tor-arm-devel <= 1.4.5.0-17

%description %_description

%package doc
Summary:        %summary

%description doc %_description

%prep
%autosetup

%build
%py3_build

%install
%py3_install
install -D -m 0644 nyx.1 %{buildroot}%{_mandir}/man1/nyx.1

%check
%{__python3} run_tests.py

%files
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}*-py*.egg-info

%files doc
%license LICENSE
%doc web
%{_mandir}/man1/nyx.1*

%changelog
* Mon Aug 03 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-6
- Enable tests

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.0-1
- Version 2.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-2
- Add Obsoletes for all tor-arm subpackages

* Wed Nov 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.4-1
- Version 2.0.4

* Wed Jul 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.6-2.20170712git08eec6f
- Use Python3
- Doc subpackage

* Wed Jul 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.6-1.20170712git08eec6f
- First release of nyx
