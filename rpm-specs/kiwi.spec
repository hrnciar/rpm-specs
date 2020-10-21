# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Disable mangling shebangs for dracut module files as it breaks initramfs
%global __brp_mangle_shebangs_exclude_from ^%{_prefix}/lib/dracut/modules.d/.*$

%global desc \
The KIWI Image System provides an operating system image builder \
for Linux supported hardware platforms as well as for virtualization \
and cloud systems like Xen, KVM, VMware, EC2 and more.


Name:           kiwi
Version:        9.21.7
Release:        1%{?dist}
URL:            http://osinside.github.io/kiwi/
Summary:        Flexible operating system image builder
License:        GPLv3+
# We must use the version uploaded to pypi, as it contains all the required files.
Source0:        https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

# Fedora-specific patches
## Use buildah instead of umoci by default for OCI image builds
## TODO: Consider getting umoci into Fedora?
Patch1001:      kiwi-9.18.31-use-buildah.patch

BuildRequires:  bash-completion
BuildRequires:  dracut
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  shadow-utils

# doc build requirements
BuildRequires:  python3dist(docopt) >= 0.6.2
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pyxattr)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(six)

%description %{desc}


%package systemdeps
Summary:        Common system dependencies for KIWI
Provides:       kiwi-image:docker
Provides:       kiwi-image:iso
Provides:       kiwi-image:oem
Provides:       kiwi-image:pxe
Provides:       kiwi-image:tbz
Provides:       kiwi-image:vmx
# tools used by kiwi
# For building Fedora, RHEL/CentOS, and Mageia based images
Requires:       dnf
Provides:       kiwi-packagemanager:dnf
Provides:       kiwi-packagemanager:yum
%if 0%{?fedora}
# For building (open)SUSE based images
Requires:       zypper
Provides:       kiwi-packagemanager:zypper
%endif
# Common tool dependencies
Requires:       device-mapper-multipath
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       xorriso
Requires:       gdisk
Requires:       %{name}-tools = %{version}-%{release}
Requires:       lvm2
Requires:       mtools
Requires:       parted
Requires:       qemu-img
Requires:       rsync
Requires:       squashfs-tools
%ifarch %{ix86} x86_64
# Pull in syslinux when it's x86
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       syslinux-nonlinux
%endif
Requires:       syslinux
%endif
Requires:       tar >= 1.2.7
%if 0%{?fedora} || 0%{?rhel} >= 8
# For building Debian/Ubuntu based images
Recommends:     debootstrap
Recommends:     jing
%endif
%ifnarch ppc64 %{ix86}
# buildah isn't available on ppc64 or x86_32
Requires:       buildah
Requires:       skopeo
%endif
%ifarch %{arm} aarch64
Requires:       uboot-tools
%endif
%ifnarch s390 s390x
# grub isn't available on s390(x) systems
Requires:       grub2-tools
Requires:       grub2-tools-extra
Requires:       grub2-tools-minimal
%endif
%ifarch x86_64 aarch64
Requires:       grub2-tools-efi
%endif
%ifarch x86_64
Requires:       grub2-efi-x64-modules
Requires:       grub2-efi-ia32-modules
%endif
%ifarch %{ix86} x86_64
Requires:       grub2-pc-modules
%endif
%ifarch aarch64
Requires:       grub2-efi-aa64-modules
%endif
%ifarch s390 s390x
Requires:       s390utils
%endif
# Python 2 module is no longer available
Obsoletes:      python2-%{name} < %{version}-%{release}

%description systemdeps
This metapackage installs the necessary system dependencies
to run KIWI.

%package -n python3-%{name}
Summary:        KIWI - Python 3 implementation
Requires:       kiwi-systemdeps = %{version}-%{release}
Requires:       python3-setuptools
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 library of the KIWI Image System. Provides an operating system
image builder for Linux supported hardware platforms as well as for
virtualization and cloud systems like Xen, KVM, VMware, EC2 and more.

%package tools
Summary:        KIWI - Collection of Boot Helper Tools

%description tools
This package contains a small set of helper tools used for the
kiwi created initial ramdisk which is used to control the very
first boot of an appliance. The tools are not meant to be used
outside of the scope of kiwi appliance building.

%ifarch %{ix86} x86_64
%package pxeboot
Summary:        KIWI - PXE boot structure
Requires:       syslinux
Requires:       tftp-server

%description pxeboot
This package contains the basic PXE directory structure which is
needed to serve kiwi built images via PXE.
%endif

%package -n dracut-kiwi-lib
Summary:        KIWI - Dracut kiwi Library
Requires:       bc
# btrfs-progs is not available on RHEL 8+
%if ! (0%{?rhel} >= 8)
Requires:       btrfs-progs
%endif
Requires:       coreutils
Requires:       cryptsetup
Requires:       curl
Requires:       device-mapper
Requires:       dialog
Requires:       dracut
Requires:       e2fsprogs
Requires:       gdisk
Requires:       grep
Requires:       kpartx
Requires:       lvm2
Requires:       mdadm
Requires:       parted
Requires:       pv
Requires:       util-linux
Requires:       xfsprogs
Requires:       xz
BuildArch:      noarch

%description -n dracut-kiwi-lib
This package contains a collection of methods to provide a library
for tasks done in other kiwi dracut modules

%package -n dracut-kiwi-oem-repart
Summary:        KIWI - Dracut module for oem(repart) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
BuildArch:      noarch

%description -n dracut-kiwi-oem-repart
This package contains the kiwi-repart dracut module which is
used to repartition the oem disk image to the current disk
geometry according to the setup in the kiwi image configuration

%package -n dracut-kiwi-oem-dump
Summary:        KIWI - Dracut module for oem(install) image type
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       gawk
Requires:       kexec-tools
BuildArch:      noarch

%description -n dracut-kiwi-oem-dump
This package contains the kiwi-dump and kiwi-dump-reboot dracut
modules which is used to install an oem image onto a target disk.
It implements a simple installer which allows for user selected
target disk or unattended installation to target. The source of
the image to install could be either from media(CD/DVD/USB) or
from remote

%package -n dracut-kiwi-live
Summary:        KIWI - Dracut module for iso(live) image type
Requires:       device-mapper
Requires:       dialog
Requires:       dracut
Requires:       e2fsprogs
Requires:       xorriso
Requires:       util-linux
Requires:       xfsprogs
Requires:       parted
BuildArch:      noarch

%description -n dracut-kiwi-live
This package contains the kiwi-live dracut module which is used
for booting iso(live) images built with KIWI

%package -n dracut-kiwi-overlay
Summary:        KIWI - Dracut module for vmx(+overlay) image type
Requires:       dracut
Requires:       util-linux
BuildArch:      noarch

%description -n dracut-kiwi-overlay
This package contains the kiwi-overlay dracut module which is used
for booting vmx images built with KIWI and configured to use an
overlay root filesystem

%package cli
Summary:        Flexible operating system appliance image builder
Provides:       kiwi-schema = 7.2
# So we can reference it by the source package name while permitting this to be noarch
Provides:       %{name} = %{version}-%{release}
Requires:       python3-%{name} = %{version}-%{release}
Requires:       bash-completion
BuildArch:      noarch

%description cli %{desc}


%prep
%autosetup -p1

# Drop shebang for kiwi/xml_parse.py, as we don't intend to use it as an independent script
sed -e "s|#!/usr/bin/env python||" -i kiwi/xml_parse.py

%build
# Because there are some compiled stuff
%set_build_flags

%py3_build

# Build C-Tools
make CFLAGS="%{build_cflags}" tools

%install
%py3_install

# Install C-Tools, man-pages, completion and kiwi default configuration (yes, the slash is needed!)
make buildroot=%{buildroot}/ install

# Install dracut modules (yes, the slash is needed!)
make buildroot=%{buildroot}/ install_dracut

# Erase redundant bash completion file
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d

# Get rid of unnecessary doc files
rm -rf %{buildroot}%{_docdir}/packages

# Rename unversioned binaries
mv %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi-ng-3
mv %{buildroot}%{_bindir}/kiwicompat %{buildroot}%{_bindir}/kiwicompat-3

# Create symlinks for correct binaries
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi
ln -sr %{buildroot}%{_bindir}/kiwi-ng-3 %{buildroot}%{_bindir}/kiwi-ng
ln -sr %{buildroot}%{_bindir}/kiwicompat-3 %{buildroot}%{_bindir}/kiwicompat

# kiwi pxeboot directory structure to be packed in kiwi-pxeboot
%ifarch %{ix86} x86_64
for i in KIWI pxelinux.cfg image upload boot; do \
    mkdir -p %{buildroot}%{_sharedstatedir}/tftpboot/$i ;\
done
%fdupes %{buildroot}%{_sharedstatedir}/tftpboot
%endif

%files -n python3-%{name}
%license LICENSE
%{_bindir}/kiwi-ng-3*
%{_bindir}/kiwicompat-3*
%{python3_sitelib}/kiwi*/

%files tools
%license LICENSE
%{_bindir}/dcounter
%{_bindir}/isconsole
%{_bindir}/utimer

%files cli
%{_bindir}/kiwi
%{_bindir}/kiwi-ng
%{_bindir}/kiwicompat
%{_datadir}/bash-completion/completions/kiwi-ng.sh
%{_mandir}/man8/kiwi*
%config(noreplace) %{_sysconfdir}/kiwi.yml

%ifarch %{ix86} x86_64
%files pxeboot
%license LICENSE
%{_sharedstatedir}/tftpboot/*
%endif

%files -n dracut-kiwi-lib
%license LICENSE
%{_prefix}/lib/dracut/modules.d/99kiwi-lib/

%files -n dracut-kiwi-oem-repart
%license LICENSE
%{_prefix}/lib/dracut/modules.d/90kiwi-repart/

%files -n dracut-kiwi-oem-dump
%license LICENSE
%{_prefix}/lib/dracut/modules.d/90kiwi-dump/
%{_prefix}/lib/dracut/modules.d/99kiwi-dump-reboot/

%files -n dracut-kiwi-live
%license LICENSE
%{_prefix}/lib/dracut/modules.d/90kiwi-live/

%files -n dracut-kiwi-overlay
%license LICENSE
%{_prefix}/lib/dracut/modules.d/90kiwi-overlay/

%files systemdeps
# Empty metapackage

%changelog
* Sat Aug 15 2020 Neal Gompa <ngompa13@gmail.com> - 9.21.7-1
- Upgrade to 9.21.7 (RH#1820679)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.21.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Neal Gompa <ngompa13@gmail.com> - 9.21.5-1
- Upgrade to 9.21.5 (RH#1820679)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 9.20.5-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Neal Gompa <ngompa13@gmail.com> - 9.20.5-1
- Upgrade to 9.20.5 (RH#1798896)
- Fix installation of dracut modules on RHEL 8

* Wed Feb 05 2020 Neal Gompa <ngompa13@gmail.com> - 9.19.15-1
- Upgrade to 9.19.15 (RH#1779818)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.19.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Neal Gompa <ngompa13@gmail.com> - 9.19.5-1
- Upgrade to 9.19.5 (RH#1772452)

* Mon Nov 11 2019 Neal Gompa <ngompa13@gmail.com> - 9.18.31-1
- Upgrade to 9.18.31 (RH#1755472)
- Rebase patch to use buildah by default for OCI image builds

* Sat Sep 21 2019 Neal Gompa <ngompa13@gmail.com> - 9.18.17-1
- Upgrade to 9.18.17 (RH#1742734)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 9.18.9-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Neal Gompa <ngompa13@gmail.com> - 9.18.9-1
- Upgrade to 9.18.9

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.18.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Neal Gompa <ngompa13@gmail.com> - 9.18.6-1
- Upgrade to 9.18.6
- Add skopeo as a requirement for container builds

* Thu Jul 04 2019 Neal Gompa <ngompa13@gmail.com> - 9.17.41-1
- Upgrade to 9.17.41 (RH#1713612)
- Switch to requiring grub2 tools and modules instead of grub2-efi
- Do not require grub2 on s390x
- Drop spec cruft for pre Fedora 29

* Mon Apr 22 2019 Neal Gompa <ngompa13@gmail.com> - 9.17.38-1
- Upgrade to 9.17.38 (RH#1698619)

* Sun Mar 31 2019 Neal Gompa <ngompa13@gmail.com> - 9.17.34-2
- Do not require buildah on x86_32 and ppc64

* Sun Mar 31 2019 Neal Gompa <ngompa13@gmail.com> - 9.17.34-1
- Upgrade to 9.17.34 (RH#1688338)
- Patch to use buildah by default instead of umoci for OCI image builds

* Sun Mar 10 2019 Neal Gompa <ngompa13@gmail.com> - 9.17.27-1
- Upgrade to 9.17.27 (RH#1680084)

* Sun Feb 17 2019 Neal Gompa <ngompa13@gmail.com> - 9.17.19-1
- Upgrade to 9.17.19

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.16.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 26 2018 Neal Gompa <ngompa13@gmail.com> - 9.16.12-1
- Upgrade to 9.16.12 (RH#1591056)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 9.16.0-2
- Rebuilt for Python 3.7

* Wed Jun 06 2018 Neal Gompa <ngompa13@gmail.com> - 9.16.0-1
- Upgrade to 9.16.0 (RH#1578808)
- Drop Python 2 subpackage for F29+

* Wed May 09 2018 Neal Gompa <ngompa13@gmail.com> - 9.15.1-1
- Upgrade to 9.15.1 (RH#1570222)

* Thu Apr 12 2018 Neal Gompa <ngompa13@gmail.com> - 9.14.2-1
- Upgrade to 9.14.2 (RH#1565110)

* Sat Mar 24 2018 Neal Gompa <ngompa13@gmail.com> - 9.14.0-1
- Upgrade to 9.14.0 (RH#1560120)

* Sat Mar 17 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.7-2
- Add Conflicts for flumotion < 0.11.0.1-9 on python2-kiwi

* Sat Mar 17 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.7-1
- Initial import into Fedora (RH#1483339)

* Fri Mar 16 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.7-0.4
- Drop useless python shebang in a source file
- Swap python BRs for python2 ones

* Fri Mar 16 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.7-0.3
- Fix invocations of python_provide macro to work with noarch subpackages
- Add BuildRequires for kiwi-tools

* Fri Mar 16 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.7-0.2
- More small cleanups
- Reorder Req/Prov declarations

* Fri Mar 16 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.7-0.1
- Update to 9.13.7
- Cleanups to packaging per review
- Adapt kiwi-pxeboot to match how tftp-server is packaged

* Sun Feb 25 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.0-0.3
- Rename source package from python-kiwi to kiwi
- Rename kiwi subpackage to kiwi-cli
- Merge kiwi-man-pages into kiwi-cli

* Wed Feb 21 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.0-0.2
- Update proposed change based on PR changes

* Tue Feb 20 2018 Neal Gompa <ngompa13@gmail.com> - 9.13.0-0.1
- Update to 9.13.0
- Add proposed change to fix yum vs yum-deprecated lookup in chroot

* Mon Feb 12 2018 Neal Gompa <ngompa13@gmail.com> - 9.12.8-0.4
- Switch to autosetup to actually apply patch

* Mon Feb 12 2018 Neal Gompa <ngompa13@gmail.com> - 9.12.8-0.3
- Patch to use pyxattr in setuptools data

* Fri Feb 09 2018 Neal Gompa <ngompa13@gmail.com> - 9.12.8-0.2
- Fix broken dependency on pyxattr

* Thu Feb 08 2018 Neal Gompa <ngompa13@gmail.com> - 9.12.8-0.1
- Update to 9.12.8

* Mon Jan 15 2018 Neal Gompa <ngompa13@gmail.com> - 9.11.30-0.1
- Update to 9.11.30

* Thu Dec 21 2017 Neal Gompa <ngompa13@gmail.com> - 9.11.19-0.1
- Update to 9.11.19

* Wed Sep 06 2017 Neal Gompa <ngompa13@gmail.com> - 9.10.7-0.1
- Update to 9.10.7

* Wed Aug 23 2017 Neal Gompa <ngompa13@gmail.com> - 9.10.6-0.1
- Update to 9.10.6
- Address review feedback

* Sun Aug 20 2017 Neal Gompa <ngompa13@gmail.com> - 9.10.4-0.1
- Initial packaging

