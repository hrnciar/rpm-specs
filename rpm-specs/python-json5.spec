%global pypi_name json5

Name:           python-%{pypi_name}
Version:        0.9.5
Release:        2%{?dist}
Summary:        Python implementation of the JSON5 data format

License:        ASL 2.0
URL:            https://github.com/dpranke/pyjson5
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JSON5 extends the JSON data interchange format to make it slightly more usable
as a configuration language:

- JavaScript-style comments (both single and multi-line) are legal.
- Object keys may be unquoted if they are legal ECMAScript identifiers
- Objects and arrays may end with trailing commas.
- Strings can be single-quoted, and multi-line string literals are allowed.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-hypothesis
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JSON5 extends the JSON data interchange format to make it slightly more usable
as a configuration language:

- JavaScript-style comments (both single and multi-line) are legal.
- Object keys may be unquoted if they are legal ECMAScript identifiers
- Objects and arrays may end with trailing commas.
- Strings can be single-quoted, and multi-line string literals are allowed.

%package -n pyjson5
Summary:        Tool for working with the JSON5 data format

Requires:       python3-%{pypi_name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n pyjson5
Command-line tool for working with the JSON5 data format.

%prep
%autosetup -n py%{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/README.md

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/tests/

%files -n pyjson5
%doc README.md
%license LICENSE
%{_bindir}/pyjson5

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Update to latest upstream release 0.9.5 (rhbz#1840447)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4 (rhbz#1817785)

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Update to latest upstream release 0.9.3 (rhbz#1815084)

* Sun Feb 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to latest upstream release 0.9.1

* Thu Feb 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.5-2
- Update summary
- Add version (rhbz#1750541)

* Mon Sep 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.5-1
- Initial package for Fedora
