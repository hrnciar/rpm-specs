%global srcname json2table

%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        1.1.5
Release:        9%{?dist}
Summary:        Python module to convert JSON to an HTML table

License:        MIT
URL:            https://github.com/latture/json2table
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This is a simple Python package that allows a JSON object to be converted
to HTML. It provides a convert function that accepts a dict instance and
returns a string of converted HTML.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-beautifulsoup4

%description -n python3-%{srcname}
This is a simple Python package that allows a JSON object to be converted
to HTML. It provides a convert function that accepts a dict instance and
returns a string of converted HTML.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.5-3
- Fix typos (rhbz#1708273)

* Thu Apr 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.5-2
- Add missing license file

* Sun Apr 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.5-1
- Initial package for Fedora
