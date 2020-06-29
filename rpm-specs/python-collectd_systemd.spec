# Created by pyp2rpm-3.3.0
%global pypi_name collectd_systemd

%global commit 212cb7918fa6925213082d11a0fe0fb44fe84852
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20181018git%{shortcommit}

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        0.17.%{snapinfo}%{?dist}
Summary:        Collectd plugin to monitor systemd services

License:        MIT
URL:            https://github.com/mbachry/collectd-systemd/
Source0:        https://github.com/mbachry/collectd-systemd/archive/%{commit}/collectd-system-%{shortcommit}.tar.gz
Source1:        collectd_systemd.te
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(mock)

BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros

%description
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-dbus
Requires:       collectd-python
Requires:       %{name}-selinux = %{version}-%{release}

%description -n python3-%{pypi_name}
collectd-systemd A collectd plugin which checks if given systemd services
are in "running" state and sends metrics with 1.0 or 0.0.

%package selinux
Summary:        selinux policy for collectd systemd plugin
Requires:       selinux-policy
Requires:       policycoreutils

%description selinux
This package contains selinux rules to allow the collectd
systemd plugin to access service status via dbus.

%prep
%autosetup -n collectd-systemd-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -p %{SOURCE1} .

%build
%py3_build
make -f /usr/share/selinux/devel/Makefile collectd_systemd.pp

%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 644 -p collectd_systemd.pp \
    %{buildroot}%{_datadir}/selinux/packages/%{name}/collectd_systemd.pp

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/collectd_systemd.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r collectd_systemd >/dev/null 2>&1 || :
fi
%systemd_postun_with_restart collectd.service


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files selinux
%{_datadir}/selinux/packages/%{name}/collectd_systemd.pp

%check
PYTHONPATH=. pytest-3

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.17.20181018git212cb79
- Rebuilt for Python 3.9

* Fri Feb 14 2020 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.16.20181018git212cb79
- condrestart collectd on upgrade in particular

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.15.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.14.20181018git212cb79
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.13.20181018git212cb79
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.12.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.11.20181018git212cb79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.10.20181018git212cb79
- Subpackage python2-collectd_systemd has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 18 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.9.20181018git212cb79
- New HEAD from upstream.

* Tue Sep 18 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.8.20180604gitbe9c647
- Policy file updated for init.d services.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-0.7.20180604gitbe9c647
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.1-0.6.20180604gitbe9c647
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.5.20180604gitbe9c647
- New HEAD from upstream.

* Thu May 24 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.4.20180516gita7018ec
- Corect path to selinux module.

* Tue May 22 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.3.20180516gita7018ec
- Add selinux sub package

* Thu May 17 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.2.20180516gita7018ec
- Correct snapshot in string.

* Wed May 16 2018 Steve Traylen <steve.traylen@cern.ch> - 0.0.1-0.1.20180516gita7018ec
- Initial package.
