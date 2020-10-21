%define soname 6

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

Name:           xtb
Version:        6.3.3
Release:        1%{?dist}
Summary:        Semiempirical Extended Tight-Binding Program Package
License:        LGPLv3+
URL:            https://github.com/grimme-lab/xtb/
Source0:        https://github.com/grimme-lab/xtb/archive/v%{version}/xtb-%{version}.tar.gz

# Fedora versioning
Patch0:         xtb-6.3.2-fedora.patch
# Use LAPACK for matmul; https://github.com/grimme-lab/xtb/pull/266
Patch2:         xtb-6.3.1-lapack.patch
# Add sanity checks to environment variables, https://github.com/grimme-lab/xtb/pull/317
Patch4:         xtb-6.3.2-environment.patch

BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{blaslib}-devel
# To generate man pages
BuildRequires:  rubygem-asciidoctor
# The program queries $HOSTNAME at runtime and so fails to run in mock without this
BuildRequires:  hostname

# Tests fail on s390x for some reason
ExcludeArch:    s390x

%description
The xtb program package developed by the Grimme group in Bonn.

%package libs
Summary:   Data files and shared libraries for xtb
# The program queries $HOSTNAME at runtime and so fails to run in mock without this
Requires: hostname

%description libs
This package contains the data files and shared libraries for xtb.

%package devel
Summary:   Development headers for xtb
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers for xtb.

%prep
%setup -q
%patch0 -p1 -b .fedoraver
%patch2 -p1 -b .lapack
%patch4 -p1 -b .env

%build
%meson -Dla_backend=custom -Dcustom_libraries=%{blaslib}%{blasvar} -Dtest_timeout=2000
date=$(date)
# Create customized Fedora versioning
cat > %{_vpath_builddir}/xtb_version.fh <<EOF
character(len=*),parameter :: version = "%{version}-%{release}%{dist}"
character(len=*),parameter :: date = "$date"
character(len=*),parameter :: author = "Fedora project"
EOF
%meson_build

%install
%meson_install
# Remove static library
rm %{buildroot}%{_libdir}/libxtb.a
# Remove environment module files
rm -rf %{buildroot}%{_datadir}/modules

# Create profile files
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.sh <<EOF
XTBPATH=%{_datadir}/xtb
export XTBPATH
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.csh <<EOF
setenv XTBPATH %{_datadir}/xtb
EOF

%check
set
# Set missing environment variable
export HOSTNAME=$(hostname)
%meson_test

%files
# LGPLv3+ license is stated at bottom of README.md
%doc README.md CONTRIBUTING.md
%{_bindir}/xtb

%files libs
%license COPYING COPYING.LESSER README.md
%{_sysconfdir}/profile.d/xtb.sh
%{_sysconfdir}/profile.d/xtb.csh
%{_datadir}/xtb/
%{_mandir}/man1/xtb.1*
%{_mandir}/man7/xcontrol.7*
%{_libdir}/libxtb.so.%{soname}*

%files devel
%{_includedir}/xtb.h
%{_libdir}/libxtb.so
%{_libdir}/pkgconfig/xtb.pc

%changelog
* Thu Sep 17 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.3-1
- Update to 6.3.3.

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 6.3.2-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Aug 05 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.2-1
- Update to 6.3.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-5
- Review fixes.

* Sun Jun 21 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-4
- Drop Python requirements since the python stuff is now in another project.

* Thu Jun 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-3
- Fix crashes on several architectures.

* Thu Jun 18 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-2
- Add dependency on rubygem-asciidoc to get man pages.
- Increase test timeouts to avoid build failures.
- Disable architectures that fail to work.
- Use external BLAS library for matmul.

* Wed Jun 17 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.3.1-1
- First release.
