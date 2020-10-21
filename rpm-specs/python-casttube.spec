# No outside connectivity in koji
%global with_tests 0
%global pypi_name casttube

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        1%{?dist}
Summary:        A python library to interact with the Youtube Chromecast api

License:        MIT
URL:            https://github.com/ur1katz/casttube
Source0:        https://github.com/ur1katz/casttube/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_tests}
BuildRequires:  python3-requests
%endif

%description
Casttube is a python library to interact with the Youtube Chromecast api.

%package -n python3-casttube
Summary:        A python library to interact with the Youtube Chromecast api
%{?python_provide:%python_provide python3-casttube}

Requires: python3-requests

%description -n python3-casttube
Casttube is a python library to interact with the Youtube Chromecast api.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}/usr/LICENSE

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-casttube
%license LICENSE
%{python3_sitelib}/casttube
%{python3_sitelib}/casttube-%{version}-py*.egg-info

%changelog
* Sat Oct 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-2
- Review updates

* Wed Sep 11 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-1
- initial packaging
