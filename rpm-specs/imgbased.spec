%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_python3 1
%else
%global with_python3 0
%endif

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%global with_python2 0
%else
%global with_python2 1
%endif

%if ! 0%{?rhel}
%{!?with_check:%global with_check 1}
%else
%{!?with_check:%global with_check 0}
%endif
%global _configure ../configure


Name:           imgbased
Version:        1.2.5
Release:        %{?_release}%{?!_release:0.1}%{?dist}.2
Summary:        Tools to work with an image based rootfs

License:        GPLv2+
URL:            https://www.github.com/fabiand/imgbased
Source0:        http://resources.ovirt.org/pub/src/%{name}/%{name}-%{version}.tar.xz

BuildArch:      noarch


BuildRequires:       make
BuildRequires:       automake
BuildRequires:       autoconf
BuildRequires:       rpm-build
BuildRequires:       git
BuildRequires:       asciidoc
BuildRequires:       systemd-units

%if 0%{?with_python3}
Requires:            python%{python3_pkgversion}-imgbased
%else
Requires:            python-imgbased
%endif # with_python3

Requires:            lvm2
Requires:            util-linux
Requires:            augeas
Requires:            rsync
Requires:            tar
Requires:            openscap-scanner
Requires:            grubby

%{!?_licensedir:%global license %%doc}

%description
This tool enforces a special usage pattern for LVM.
Basically this is about having read-only bases and writable
layers atop.


%if 0%{?with_python2}
%package -n python-imgbased
Summary: A python 2 module for imgbased
Requires:       rpm-python
Requires:       systemd-python
Requires:       yum-plugin-versionlock
Requires:       python
BuildRequires:       python-devel
%if 0%{?with_check}
BuildRequires:       python-pep8
BuildRequires:       pyflakes
BuildRequires:       python-nose
BuildRequires:       python-six
BuildRequires:       systemd-python
%endif

%description -n python-imgbased
python-imgbased is a python 2 library to manage lvm layers
%endif # with_python2

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-imgbased
Summary: A python 3 module for imgbased
BuildRequires:       python%{python3_pkgversion}-devel
%if 0%{?with_check}
BuildRequires:       python%{python3_pkgversion}-pycodestyle
BuildRequires:       python%{python3_pkgversion}-pyflakes
BuildRequires:       python%{python3_pkgversion}-nose
BuildRequires:       python%{python3_pkgversion}-six
BuildRequires:       python%{python3_pkgversion}-systemd
%endif
Requires:       python%{python3_pkgversion}-systemd
Requires:       python%{python3_pkgversion}-rpm
Requires:       dnf-plugin-versionlock
Requires:       python%{python3_pkgversion}

%description -n python%{python3_pkgversion}-imgbased
python%{python3_pkgversion}-imgbased is a python 3 library to manage lvm layers
%endif # with_python3

%prep
%setup -q

%build
%if 0%{?with_python2}
mkdir py2 && pushd py2
%configure PYTHON="%{__python2}"
make %{?_smp_mflags}
popd
%endif # with_python2

%if 0%{?with_python3}
mkdir py3 && pushd py3
%configure PYTHON="%{__python3}"
make %{?_smp_mflags}
%endif # with_python3

%install
%if 0%{?fedora} || 0%{?rhel} >= 8
install -Dm 0644 src/plugin-dnf/imgbased-persist.conf \
                 %{buildroot}/%{_sysconfdir}/dnf/plugins/imgbased-persist.conf
install -Dm 0644 src/plugin-dnf/imgbased-persist.py \
                 %{buildroot}/%{python3_sitelib}/dnf-plugins/imgbased-persist.py
%else
install -Dm 0644 src/plugin-yum/imgbased-persist.py \
                 %{buildroot}/%{_prefix}/lib/yum-plugins/imgbased-persist.py
install -Dm 0644 src/plugin-yum/imgbased-persist.conf \
                 %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/imgbased-persist.conf
%endif
install -Dm 0644 data/imgbase-setup.service %{buildroot}%{_unitdir}/imgbase-setup.service
install -Dm 0444 data/imgbased-pool.profile %{buildroot}%{_sysconfdir}/lvm/profile/imgbased-pool.profile

%if 0%{?with_python2}
make -C py2 install DESTDIR="%{buildroot}"
%endif # with_python2

%if 0%{?with_python3}
make -C py3 install DESTDIR="%{buildroot}"
%endif # with_python3


%files
%doc README.md
%license LICENSE
%{_sbindir}/imgbase
%{_datadir}/%{name}/hooks.d/
%{_mandir}/man8/imgbase.8*
/%{_docdir}/%{name}/*.asc
%{_unitdir}/imgbase-setup.service
%{_sysconfdir}/lvm/profile/imgbased-pool.profile
%if 0%{?fedora} || 0%{?rhel} >= 8
%{_sysconfdir}/dnf/plugins/imgbased-persist.conf
%{python3_sitelib}/dnf-plugins/imgbased-persist.py*
%{python3_sitelib}/dnf-plugins/__pycache__/imgbased*
%else
%{_sysconfdir}/yum/pluginconf.d/imgbased-persist.conf
%{_prefix}/lib/yum-plugins/imgbased-persist.py*
%endif

%if 0%{?with_python2}
%files -n python-imgbased
%doc README.md
%license LICENSE
%{python2_sitelib}/%{name}/
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-imgbased
%doc README.md
%license LICENSE
%{python3_sitelib}/%{name}/
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-0.1.2
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-0.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Yuval Turgeman <yturgema@redhat.com> - 1.2.5-1
- Rebase on upstream 1.2.5

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.10-0.1.1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Yuval Turgeman <yturgema@redhat.com> - 1.1.10-1
- Rebase on upstream 1.1.10

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2.3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Drop python2 subpackage

* Sun Oct 14 2018 Yuval Turgeman <yturgema@redhat.com> - 1.1.0-1
- Initial build for 4.3

* Mon Aug 21 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.999-0
- Development for 4.3

* Mon Mar 06 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 0.9.999-0
- Development for 4.2

* Mon Mar 06 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 0.9.16-0
- Added systemd unit for running vdsm-tool configure
- Resolves: BZ#1429288

* Fri Mar 03 2017 Ryan Barry <rbarry@redhat.com> - 0.9.15-0
- Add unmount to imgbased.utils

* Thu Feb 23 2017 Ryan Barry <rbarry@redhat.com> - 0.9.14-0
- Rescan all LVs on update

* Wed Feb 22 2017 Ryan Barry <rbarry@redhat.com> - 0.9.12-0
- Fix an error with imgbase --init

* Mon Feb 20 2017 Ryan Barry <rbarry@redhat.com> - 0.9.11-0
- Fix some logic problems in imgbased's handling of bases

* Mon Feb 20 2017 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.9.10-0
- Keep unmodified configuration files
- Switch to a NIST partition layout on upgrades

* Thu Feb 02 2017 Douglas Schilling Landgraf <dougsland@redhat.com> - 0.9.7-0
- split the imgbase in two packages for python3 support

* Fri Jan 20 2017 Ryan Barry <rbarry@redhat.com> - 0.9.6-1
- Copy kernel FIPS signatures into /boot

* Wed Jan 18 2017 Ryan Barry <rbarry@redhat.com> - 0.9.5-1
- Revert selinux relabeling on upgrades

* Wed Jan 04 2017 Ryan Barry <rbarry@redhat.com> - 0.9.4-1
- Also keep depinstalled and depupdated for persistence

* Wed Jan 04 2017 Ryan Barry <rbarry@redhat.com> - 0.9.3-1
- Ensure new layers have enough space for hosted engine
- Copy the kernel and initrd to /boot so grub2-mkconfig and virt-v2v work

* Wed Jan 04 2017 Ryan Barry <rbarry@redhat.com> - 0.9.2-1
- Use GB instead of GiB in osupdater /boot validation

* Tue Jan 03 2017 Ryan Barry <rbarry@redhat.com> - 0.9.1-1
- Fix a typo in utils.SystemRelease which blocks installs

* Tue Dec 20 2016 Ryan Barry <rbarry@redhat.com> - 0.9.0-1
- Add a yum plugin to persist RPMs through upgrades
- Remove existing yum/dnf plugins

* Mon Nov 14 2016 Ryan Barry <rbarry@redhat.com> - 0.8.10-1
- Enable IQN randomization

* Fri Nov 11 2016 Ryan Barry <rbarry@redhat.com> - 0.8.9-1
- Also relocate on updates

* Thu Nov 10 2016 Ryan Barry <rbarry@redhat.com> - 0.8.8-1
- Relocate /var/lib/yum to /usr

* Fri Nov 4 2016 Ryan Barry <rbarry@redhat.com> - 0.8.7-1
- Fix a regression with the last patch in interactive installs

* Wed Oct 19 2016 Ryan Barry <rbarry@redhat.com> - 0.8.6-1
- Ensure disabled services stay disabled after upgrade

* Thu Sep 15 2016 Ryan Barry <rbarry@fedoraproject.org> - 0.8.5-1
- Remove non-imgbased entries at boot

* Wed Apr 02 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.1
- Initial package
