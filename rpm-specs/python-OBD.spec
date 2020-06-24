%bcond_without check
%global srcname OBD

Name:          python-%{srcname}
Version:       0.7.1
Release:       3%{?dist}
Summary:       OBD-II serial module for reading engine data
License:       GPLv2+
URL:           https://github.com/brendan-w/%{name}
Source0:       https://github.com/brendan-w/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix python dependency generator error
# error: Illegal char '*' (0x2a) in: 0.7.*
# error: Illegal char '*' (0x2a) in: 3.*
Patch0:        %{name}-dep-ver.patch
BuildArch:     noarch

%global desc A python module for handling realtime sensor data from OBD-II vehicle ports.\
Works with ELM327 OBD-II adapters, and is fit for the Raspberry Pi.

%description
%{desc}

%package -n python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3-pint >= 0.7
BuildRequires: python3-pytest
BuildRequires: python3-pyserial >= 3
%endif
%if 0%{fedora} < 30
Requires:      python3-pint >= 0.7
Requires:      python3-pyserial >= 3
%endif

%description -n python3-%{srcname}
%{desc}

Python 3 version.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/obd-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/obd

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.7.1-1
- update to 0.7.1 (#1710329)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 25 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.7.0-1
- initial packaging
- fix dependency version declarations in setup.py
