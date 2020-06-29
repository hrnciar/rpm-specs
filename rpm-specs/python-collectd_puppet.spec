# Created by pyp2rpm-3.3.2
%global pypi_name collectd-puppet
%global module_name collectd_puppet

Name:           python-%{module_name}
Version:        2.0.0
Release:        7%{?dist}
Summary:        Collectd plugin to monitor puppet agents

License:        ASL 2.0
URL:            https://github.com/cernops/collectd-puppet
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{module_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       collectd-python

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemd-rpm-macros


%description
Collectd plugin for puppet run status.

%package -n     python3-%{module_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{module_name}}

Requires:       python3dist(pyyaml)
%description -n python3-%{module_name}
Collectd plugin for puppet run status.

%prep
%autosetup -n %{module_name}-%{version}
# Remove bundled egg_info
rm -r src/%{module_name}.egg-info

%build
%py3_build

%install
%py3_install

%postun
%systemd_postun_with_restart collectd.service

%files -n python3-%{module_name}
%license LICENSE
%doc README.rst NEWS.rst
%{_datadir}/collectd/puppet_types.db
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-7
- Rebuilt for Python 3.9

* Fri Feb 14 2020 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-7
- condrestart collectd on upgrade

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Steve Traylen <steve.traylen@cern.ch> - 2.0.0-1
- Update to 2.0.0

* Wed Feb 06 2019 Steve Traylen <steve.traylen@cern.ch> - 1.5.1-1
- Initial package.
