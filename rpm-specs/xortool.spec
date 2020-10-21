%global pypi_name xortool

Name:           %{pypi_name}
Version:        0.99
Release:        4%{?dist}
Summary:        Tool for XOR cipher analysis

License:        MIT
URL:            https://github.com/hellman/xortool
Source0:        https://github.com/hellman/xortool/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

%description
A tool to do some XOR analysis to guess the key length (based on count of
equal chars) and to guess the key (base on knowledge of most frequent char).

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' xortool/*.py

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-xor
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.99-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.99-2
- Rebuilt for Python 3.9

* Fri Feb 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.99-1
- Update to latest upstream release 0.99

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.98-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.98-3
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.98-1
- Initial package for Fedora
