# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Services used for GCE
%global gce_services google-accounts-daemon.service google-clock-skew-daemon.service google-instance-setup.service google-network-daemon.service google-shutdown-scripts.service google-startup-scripts.service

# Google does not properly version the sources, this commit is the "tag-release" of this package
%global base_name google-compute-engine
%global srcname compute-image-packages
%global commit 3178e68b004eea38dada580de4193994f45dfc50
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: google-compute-engine-tools
Version: 2.8.12
Release: 7%{?dist}
Summary: Google Compute Engine guest environment tools
License: ASL 2.0
URL: https://github.com/GoogleCloudPlatform/%{srcname}
Source0: %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

# Ensure cloud-init runs after network configuration
# From: https://github.com/GoogleCloudPlatform/compute-image-packages/pull/682
Patch0001: 0001-google-network-daemon-Start-before-cloud-init-runs.patch

BuildArch: noarch

BuildRequires: python3-boto
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: systemd

Requires: curl
Requires: %{base_name}-oslogin
Requires: python3-%{base_name} = %{version}-%{release}
Requires: rsyslog
Requires: systemd

# Provide the upstream name of this package...
Provides: %{base_name} = %{version}-%{release}

%description
This package contains scripts, configuration, and init files
for features specific to the Google Compute Engine cloud environment.

%files
%attr(0755,root,root) %{_sysconfdir}/dhcp/dhclient.d/google_hostname.sh
%{_unitdir}/*.service
%{_presetdir}/90-google-compute-engine.preset
# These should generally be replaced on upgrade as they are reflections of GCP required configuration
%config %{_sysconfdir}/modprobe.d/gce-blacklist.conf
%config %{_sysconfdir}/rsyslog.d/90-google.conf
%{_sysctldir}/11-gce-network-security.conf
%{_udevrulesdir}/*.rules
%attr(0755,root,root) %{_bindir}/*

%preun
%systemd_preun %{gce_services}

%post
%systemd_post %{gce_services}

%postun
# On upgrade run instance setup again to handle any new configs and restart daemons.
if [ $1 -eq 1 ]; then
  %{_bindir}/google_instance_setup
fi
%systemd_postun_with_restart %{gce_services}


# -------------------------------------------------------------------

%package -n python3-%{base_name}
Summary: Google Compute Engine Python 3 library
%{?python_provide:%python_provide python3-%{base_name}}

%description -n python3-%{base_name}
Google Compute Engine python library for Python 3.x.

%files -n python3-%{base_name}
%{python3_sitelib}/google_compute_engine/
%{python3_sitelib}/google_compute_engine-*

# -------------------------------------------------------------------

%prep
%autosetup -n %{srcname}-%{commit} -p1

# Purge unneeded shebangs
find google_compute_engine/ -name "*.py" -exec sed -e "\|#!/usr/bin/python|d" -i "{}" +;

%build
%py3_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/dhcp
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d
mkdir -p %{buildroot}%{_sysctldir}
mkdir -p %{buildroot}%{_udevrulesdir}

cp google_config/modprobe/gce-blacklist.conf %{buildroot}%{_sysconfdir}/modprobe.d/
cp google_config/rsyslog/90-google.conf %{buildroot}%{_sysconfdir}/rsyslog.d/
cp google_config/sysctl/11-gce-network-security.conf  %{buildroot}%{_sysctldir}
cp google_config/udev/*.rules %{buildroot}%{_udevrulesdir}

%py3_install

mkdir -p %{buildroot}%{_sysconfdir}/dhcp/dhclient.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_presetdir}
cp google_compute_engine_init/systemd/*.service %{buildroot}%{_unitdir}
cp google_compute_engine_init/systemd/90-google-compute-engine.preset %{buildroot}%{_presetdir}/90-google-compute-engine.preset
cp google_config/bin/google_set_hostname %{buildroot}%{_bindir}
cp google_config/dhcp/google_hostname.sh %{buildroot}%{_sysconfdir}/dhcp/dhclient.d/google_hostname.sh


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.12-7
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.12-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8.12-4
- Rebuilt for Python 3.8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Neal Gompa <ngompa13@gmail.com> - 2.8.12-2
- Fix postun script to run instance setup on upgrades

* Wed Dec 12 2018 Neal Gompa <ngompa13@gmail.com> - 2.8.12-1
- Rebase to 2.8.12

* Tue Oct 30 2018 Neal Gompa <ngompa13@gmail.com> - 2.8.8-1
- Initial packaging for Fedora
