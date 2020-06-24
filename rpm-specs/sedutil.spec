%global gittag0 1.15.1

%global _hardened_build 1

Name:		sedutil
Version:	%{gittag0}
Release:	5%{?dist}
Summary:	Tools to manage the activation and use of self encrypting drives

# Everything is GPLv3+ except:
# - Common/pbkdf2/* which is CC0, a bundled copy of Cifra: https://github.com/ctz/cifra
License:	GPLv3+ and CC0
URL:		https://github.com/Drive-Trust-Alliance/sedutil/wiki
Source0:	https://github.com/Drive-Trust-Alliance/%{name}/archive/%{gittag0}/%{name}-%{gittag0}.tar.gz

# Modified version of https://github.com/Drive-Trust-Alliance/sedutil/pull/56.patch
# to use linux/nvme_ioctl.h regardless of kernel version number so we can compile on EL7.
Patch0:		sedutil-1.15.1-nvme_ioctl.patch

# sedutil does not work on big-endian architectures
ExcludeArch:	ppc ppc64 s390 s390x

BuildRequires:	gcc-c++
BuildRequires:	ncurses-devel

# This package uses a bundled copy of Cifra:
# https://github.com/ctz/cifra/commit/319fdb764cd12e12b8296358cfcd640346c4d0dd
Provides:	bundled(cifra)

# Replaces msed, but doesn't provide a compatible CLI command
Obsoletes:	msed <= 0.23-0.20

%description
The Drive Trust Alliance software (sedutil) is an Open Source (GPLv3)
effort to make Self Encrypting Drive technology freely available to
everyone. It is a combination of the two known available Open Source
code bases today: msed and OpalTool.

sedutil is a Self-Encrypting Drive (SED) management program and
Pre-Boot Authorization (PBA) image that will allow the activation and
use of self encrypting drives that comply with the Trusted Computing
Group Opal 2.0 SSC.

This package provides the sedutil-cli and linuxpba binaries, but not
the PBA image itself.

%prep
%setup -q -n sedutil-%{gittag0}
%{?el7:%patch0 -p1 -b .nvme_ioctl}
# Adjust the GitVersion.sh script to just use the git tag from the
# checkout so we don't need a full git tree or the git tool itself.
cd linux
sed -i -e's/tarball/%{gittag0}/' GitVersion.sh
# Remove stray execute permissions from source code
find . -type f -name '*.h' -exec chmod -x {} \;
find . -type f -name '*.cpp' -exec chmod -x {} \;


%build
# Always use the x86_64 build configuration, because we override
# CFLAGS etc. for each arch build anyway and the upstream makefiles
# don't have build configs for every arch we support.
cd linux/CLI
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" CONF=Release_x86_64

cd ../../LinuxPBA
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" CONF=Release

%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -p -m755 linux/CLI/dist/Release_x86_64/GNU-Linux/sedutil-cli $RPM_BUILD_ROOT%{_sbindir}/sedutil-cli

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m644 docs/sedutil-cli.8 $RPM_BUILD_ROOT%{_mandir}/man8/sedutil-cli.8

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
install -p -m755 LinuxPBA/dist/Release/GNU-Linux/linuxpba $RPM_BUILD_ROOT%{_libexecdir}/linuxpba


%files
%doc README.md Common/Copyright.txt Common/ReadMe.txt linux/PSIDRevert_LINUX.txt
%license Common/LICENSE.txt
%{_sbindir}/sedutil-cli
%{_mandir}/man8/sedutil-cli.8*
%{_libexecdir}/linuxpba


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Charles R. Anderson <cra@wpi.edu> - 1.15.1-1
- Update to 1.15.1
- Upstream swapped bundled gnulib GPLv2+ for bundled Cifra CC0

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 1.12-8
- add BR gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-4
- Update patch for epel7 build with older kernel version numbering

* Tue May  9 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-3
- Remove commented out macros
- Clarify multiple licensing scenario
- Provides: bundled(gnulib)
- Move sedutil-cli to /usr/sbin and linuxbpa to /usr/libexec
- Provide a manual page for sedutil-cli

* Wed May  3 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-2
- Obsolete msed package
- Remove stray execute permissions from source code

* Wed May  3 2017 Charles R. Anderson <cra@wpi.edu> - 1.12-1
- Use nvme_ioctl.h for newer kernel versions (upstream pull request #56)

* Tue Jan  3 2017 Charles R. Anderson <cra@wpi.edu>
- update to 1.12
- sedutil-nvme_ioctl_h.patch for renamed linux/nvme.h header

* Wed Nov 11 2015 Charles R. Anderson <cra@wpi.edu> - 1.10-0.1.beta.git350b22c
- switch to DriveTrustAlliance/sedutil upstream where all further development
  of msed happens now.

* Fri Aug 07 2015 Rafael Fonseca <rdossant@redhat.com> - 0.23-0.7.beta.gite38a16d
- disable build on big endian architectures (rhbz#1251520)

* Mon Jul 27 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.6.beta.gite38a16d
- add comments about upstream pull requests for patches

* Sun Jul 26 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.5.beta.gite38a16d
- use Github Source0 URL and standard macros for git hash
- patch GitVersion.sh to use a static git tag so we do not need a
  full git tree or the git tool for building.
- preserve timestamps of installed files

* Tue Jul 21 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.4.beta.gite38a16d
- mark LICENSE.txt as a license text
- enable hardened build

* Tue Jul 21 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.3.beta.gite38a16d
- add more documentation

* Tue Jul 21 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.2.beta.gite38a16d
- add BR git to properly define GIT_VERSION 

* Mon Jul 20 2015 Charles R. Anderson <cra@wpi.edu> - 0.23-0.1.beta.gite38a16d
- initial package
