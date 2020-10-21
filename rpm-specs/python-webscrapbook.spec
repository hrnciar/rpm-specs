# Initially created by pyp2rpm-3.3.2
%global pypi_name webscrapbook

Name:           python-%{pypi_name}
Version:        0.15.4
Release:        2%{?dist}
Summary:        A backend toolkit for management of WebScrapBook collection

License:        MIT
URL:            https://github.com/danny0838/PyWebScrapBook
Source0:        https://github.com/danny0838/PyWebScrapBook/archive/%{version}.tar.gz#/PyWebScrapBook-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(setuptools)

%global _description\
PyWebScrapBook is a command line toolkit and backend server for the\
WebScrapBook browser extension.\
\
Features: Host any directory as a website; HTZ or MAFF archive file viewing;\
Markdown file rendering; Directory listing; Create, view, edit, and/or delete\
files via the web page or API; HTTP(S) authorization.

%description %_description

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
Requires:       python%{python3_pkgversion}dist(bottle) >= 0.12
Requires:       python%{python3_pkgversion}dist(commonmark) >= 0.8
Requires:       python%{python3_pkgversion}dist(lxml) >= 4.0
Requires:       python%{python3_pkgversion}dist(setuptools)
%description -n python%{python3_pkgversion}-%{pypi_name} %_description

%prep
%autosetup -n PyWebScrapBook-%{version}

# Remove shebangs on non-executable package contents
find webscrapbook/ -type f -exec sed -i -e '/^#!/,1d' {} \+

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/webscrapbook
%{_bindir}/wsb
%{_bindir}/wsbview
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 04 2020 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.15.4-1
- New upstream release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.6.2-1
- Initial Fedora package.
