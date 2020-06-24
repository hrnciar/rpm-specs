%global srcname branca

Name:           python-%{srcname}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Generate complex HTML+JS pages with Python

License:        MIT
URL:            https://github.com/python-visualization/branca
Source0:        https://github.com/python-visualization/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This library is a spinoff from folium, that would host the non-map-specific \
features. It may become a HTML+JS generation library in the future. It is based \
on Jinja2 only.

%description %{_description}


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(jinja2)

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build


%install
%py3_install


%check
# Skip selenium test as Firefox is no longer available that way.
rm tests/test_iframe.py
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    pytest-3


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version

* Sun Jul 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Initial package.
