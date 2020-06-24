%global pesign_vre 0.106-1
%global gnuefi_vre 1:3.0.8-1
%global openssl_vre 1.0.2j

%global debug_package %{nil}
%global __debug_package 1
%global _binaries_in_noarch_packages_terminate_build 0
%global __debug_install_post %{SOURCE100} x64 ia32
%undefine _debuginfo_subpackages

%global efidir %(eval echo $(grep ^ID= /etc/os-release | sed -e 's/^ID=//' -e 's/rhel/redhat/'))
%global shimrootdir %{_datadir}/shim/
%global shimversiondir %{shimrootdir}/%{version}-%{release}
%global efiarch x64
%global shimdir %{shimversiondir}/%{efiarch}
%global efialtarch ia32
%global shimaltdir %{shimversiondir}/%{efialtarch}

Name:		shim-unsigned-%{efiarch}
Version:	15
Release:	1%{?dist}
Summary:	First-stage UEFI bootloader
ExclusiveArch:	x86_64
License:	BSD
URL:		https://github.com/rhboot/shim
Source0:	https://github.com/rhboot/shim/releases/download/%{version}/shim-%{version}.tar.bz2
Source1:	fedora-ca.cer
# currently here's what's in our dbx:
# grub2-efi-2.00-11.fc18.x86_64:
# grubx64.efi 6ac839881e73504047c06a1aac0c4763408ecb3642783c8acf77a2d393ea5cd7
# gcdx64.efi 065cd63bab696ad2f4732af9634d66f2c0d48f8a3134b8808750d378550be151
# grub2-efi-2.00-11.fc19.x86_64:
# grubx64.efi 49ece9a10a9403b32c8e0c892fd9afe24a974323c96f2cc3dd63608754bf9b45
# gcdx64.efi 99fcaa957786c155a92b40be9c981c4e4685b8c62b408cb0f6cb2df9c30b9978
# woops.
Source2:	dbx.esl

Source100:	shim-find-debuginfo.sh

BuildRequires:  gcc make
BuildRequires:	elfutils-libelf-devel
BuildRequires:	git openssl-devel openssl
BuildRequires:	pesign >= %{pesign_vre}
BuildRequires:	gnu-efi >= %{gnuefi_vre}
BuildRequires:	gnu-efi-devel >= %{gnuefi_vre}

# Shim uses OpenSSL, but cannot use the system copy as the UEFI ABI is not
# compatible with SysV (there's no red zone under UEFI) and there isn't a
# POSIX-style C library.
# BuildRequires:	OpenSSL
Provides:	bundled(openssl) = %{openssl_vre}

%global desc \
Initial UEFI bootloader that handles chaining to a trusted full \
bootloader under secure boot environments.
%global debug_desc \
This package provides debug information for package %{expand:%%{name}} \
Debug information is useful when developing applications that \
use this package or when debugging this package.

%description
%desc

%package -n shim-unsigned-%{efialtarch}
Summary:	First-stage UEFI bootloader (unsigned data)
Provides:	bundled(openssl) = %{openssl_vre}

%description -n shim-unsigned-%{efialtarch}
%desc

%package debuginfo
Summary:	Debug information for shim-unsigned-%{efiarch}
Requires:	%{name}-debugsource = %{version}-%{release}
AutoReqProv:	0
BuildArch:	noarch

%description debuginfo
%debug_desc

%package -n shim-unsigned-%{efialtarch}-debuginfo
Summary:	Debug information for shim-unsigned-%{efialtarch}
Requires:	%{name}-debugsource = %{version}-%{release}
AutoReqProv:	0
BuildArch:	noarch

%description -n shim-unsigned-%{efialtarch}-debuginfo
%debug_desc

%package debugsource
Summary:	Debug Source for shim-unsigned
AutoReqProv:	0
BuildArch:	noarch

%description debugsource
%debug_desc

%prep
%autosetup -S git -n shim-%{version}
git config --unset user.email
git config --unset user.name
mkdir build-%{efiarch}
mkdir build-%{efialtarch}

%build
COMMITID=$(cat commit)
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMITID=${COMMITID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_HTTPBOOT=true ENABLE_SHIM_HASH=true "
MAKEFLAGS+="%{_smp_mflags}"
if [ -f "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1}"
fi
if [ -f "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2}"
fi

cd build-%{efiarch}
make ${MAKEFLAGS} DEFAULT_LOADER='\\\\grub%{efiarch}.efi' all
cd ..

cd build-%{efialtarch}
setarch linux32 -B make ${MAKEFLAGS} ARCH=%{efialtarch} DEFAULT_LOADER='\\\\grub%{efialtarch}.efi' all
cd ..

%install
COMMITID=$(cat commit)
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMITID=${COMMITID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_HTTPBOOT=true ENABLE_SHIM_HASH=true "
if [ -f "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1}"
fi
if [ -f "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2}"
fi

cd build-%{efiarch}
make ${MAKEFLAGS} \
	DEFAULT_LOADER='\\\\grub%{efiarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
cd ..

cd build-%{efialtarch}
setarch linux32 make ${MAKEFLAGS} ARCH=%{efialtarch} \
	DEFAULT_LOADER='\\\\grub%{efialtarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
cd ..

%files
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimdir}
%{shimdir}/*.efi
%{shimdir}/*.hash

%files -n shim-unsigned-%{efialtarch}
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimaltdir}
%{shimaltdir}/*.efi
%{shimaltdir}/*.hash

%files debuginfo -f build-%{efiarch}/debugfiles.list

%files -n shim-unsigned-%{efialtarch}-debuginfo -f build-%{efialtarch}/debugfiles.list

%files debugsource -f build-%{efiarch}/debugsource.list

%changelog
* Thu Apr 05 2018 Peter Jones <pjones@redhat.com> - 15-1
- Update to shim 15
- better checking for bad linker output
- flicker-free console if there's no error output
- improved http boot support
- better protocol re-installation
- dhcp proxy support
- tpm measurement even when verification is disabled
- REQUIRE_TPM build flag
- more reproducable builds
- measurement of everything verified through shim_verify()
- coverity and scan-build checker make targets
- misc cleanups

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Peter Jones <pjones@redhat.com> - 13-0.1
- Make a new shim-unsigned-x64 package like the shim-unsigned-aarch64 one.
- This will (eventually) supersede what's in the "shim" package so we can
  make "shim" hold the signed one, which will confuse fewer people.
