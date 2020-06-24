Name:           jrnl
Version:        2.4
Release:        2%{?dist}
Summary:        A command line journal application

License:        MIT
URL:            http://jrnl.sh
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
jrnl is a simple journal application for your command line. Journals are
stored as human readable plain text files and  can be encrypted using 256-bit
AES.

%prep
%autosetup -n %{name}-%{version}
sed -i -e '/^#!\//, 1d' %{name}/*.py

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4-2
- Rebuilt for Python 3.9

* Fri May 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.4-1
- Update to latest upstream release 2.4

* Sat Mar 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3-1
- Remove release pinning (rhbz#1803355)
- Update to latest upstream release 2.3

* Thu Feb 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-1
- Fix build failure (rhbz#1791686)
- Update to latest upstream release 2.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.1-1
- Update to latest upstream release 2.1.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9.8-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.8-1
- Initial package for Fedora
