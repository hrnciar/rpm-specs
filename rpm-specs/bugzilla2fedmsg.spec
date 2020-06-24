Name:               bugzilla2fedmsg
Version:            1.0.0
Release:            3%{?dist}
Summary:            Consume BZ messages over STOMP and republish to Fedora Messaging

Group:              Development/Libraries
License:            LGPLv2+
URL:                https://pypi.python.org/pypi/bugzilla2fedmsg
Source0:            https://pypi.python.org/packages/source/b/%{name}/%{name}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-pytest-cov
BuildRequires:      python%{python3_pkgversion}-mock
BuildRequires:      python%{python3_pkgversion}-stompest
BuildRequires:      python%{python3_pkgversion}-pyasn1
BuildRequires:      python%{python3_pkgversion}-dateutil
BuildRequires:      python%{python3_pkgversion}-click
BuildRequires:      python%{python3_pkgversion}-fedora-messaging

%{?python_provide:%python_provide python%{python3_pkgversion}-bugzilla2fedmsg}

%description
A consumer that listens to Bugzilla over STOMP and reproduces messages
on a Fedora Messaging bus.


%prep
%autosetup
# Remove bundled egg-info in case it exists
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# The tests are not yet part of the tarball. They will be starting with 1.0.1.
#%%{__python3} -m pytest --no-cov tests


%files
%doc README.rst LICENSE CHANGELOG.rst fedora-messaging.toml.example
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_schema/
%{python3_sitelib}/%{name}-%{version}*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Aurelien Bompard <abompard@fedoraproject.org> - 1.0.0-1
- version 1.0.0
