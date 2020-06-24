%global pypi_name spake2

%global common_description %{expand:
This library implements the SPAKE2 password-authenticated key exchange
("PAKE") algorithm. This allows two parties, who share a weak password,
to safely derive a strong shared secret (and therefore build an
encrypted + authenticated channel).}

Name:           python-%{pypi_name}
Summary:        SPAKE2 password-authenticated key exchange
Version:        0.8
Release:        7%{?dist}
License:        MIT

URL:            https://github.com/warner/python-spake2
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(hkdf)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(hkdf)

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest src/spake2


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.8-1
- Initial package.

