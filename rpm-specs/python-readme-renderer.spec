%global pypi_name readme_renderer
%global pkg_name readme-renderer

Name:           python-%{pkg_name}
Version:        27.0
Release:        1%{?dist}
Summary:        Library for rendering "readme" descriptions for Warehouse

License:        ASL 2.0
URL:            https://github.com/pypa/readme_renderer
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(bleach)
BuildRequires:  python3dist(cmarkgfm)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pkg_name}}
 
%description -n python3-%{pkg_name}
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests -k "not test_md_fixtures"

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Oct 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 27.0-1
- Update to latest upstream release 27.0 (#1813626)

* Fri Sep 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 26.0-5
- Enable tests

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 26.0-3
- Rebuilt for Python 3.9

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 26.0-2
- Fix naming (#1834176)

* Thu Apr 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 26.0-1
- Update to latest upstream release 26.0 (#1813626)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 24.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 24.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 24.0-1
- Initial package
