# Created by pyp2rpm-3.3.2
%global pypi_name collectd_cvmfs

Name:           python-%{pypi_name}
Version:        1.2.2
Release:        7%{?dist}
Summary:        Collectd plugin to monitor CvmFS Clients

License:        ASL 2.0
URL:            https://github.com/cvmfs/collectd-cvmfs
Source0:        https://files.pythonhosted.org/packages/source/c/collectd_cvmfs/collectd_cvmfs-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# pyxattr autoprovides are I think wrong so we must ingor
# https://bugzilla.redhat.com/show_bug.cgi?id=1817425
%global __requires_exclude ^python%{python3_version}dist\\(xattr\\)$

%description
Collectd module for CvmFS clients

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(psutil)
# Should be reviewed/removed if
# https://bugzilla.redhat.com/show_bug.cgi?id=1817425
# is resolved
Requires:       python3dist(pyxattr)
Requires:       collectd-python
%description -n python3-%{pypi_name}
Collectd module for CvmFS clients


%prep
%autosetup -n collectd_cvmfs-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst NEWS.txt
# https://github.com/cvmfs/collectd-cvmfs/issues/13
#%%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_prefix}/share/collectd/%{pypi_name}.db

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-7
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Steve Traylen <steve.traylen@cern.ch> - 1.2.2-6
- Filter out auto generated xattr requirement

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 26 2019 Steve Traylen <steve.traylen@cern.ch> - 1.2.2-1
- New 1.2.2 release
- Change source to pypi from github.

* Mon May 13 2019 Steve Traylen <steve.traylen@cern.ch> - 1.1.0-1
- New 1.1.0 release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Steve Traylen <steve.traylen@cern.ch> - 1.0.3-1
- New 1.0.3 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Steve Traylen <steve.traylen@cern.ch> - 1.0.1-1
- Initial package.
