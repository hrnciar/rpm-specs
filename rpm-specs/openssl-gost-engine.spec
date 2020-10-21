Name: openssl-gost-engine
Version: 1.1.1.0
Release: 0.1%{?dist}

URL: https://github.com/gost-engine/engine
License: OpenSSL
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL


Source: engine-%version.tar.gz

BuildRequires: cmake-rpm-macros gcc perl-Test-Simple
BuildRequires: cmake openssl-devel pkgconf-pkg-config

%{?!_without_check:%{?!_disable_check:BuildRequires: perl-devel openssl}}

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n gostsum
GOST file digesting utilities.

%global _enginesdir %(pkg-config --variable=enginesdir libcrypto)
%prep
%setup -n engine-%version -q

%build
%cmake -B "%{_vpath_builddir}"

%make_build -C "%{_vpath_builddir}"

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
mkdir -p %buildroot%_enginesdir
cp "%{_vpath_builddir}"/bin/gost.so README.gost %buildroot%_enginesdir/
cp "%{_vpath_builddir}"/bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_mandir/man1/

%check
# tests currently do not work due to missing crypto-policies support
exit 0
echo "ALL" > "$PWD/openssl-crypto-policy.override"
OPENSSL_ENGINES="$PWD/%{_vpath_builddir}/bin" \
	OPENSSL_SYSTEM_CIPHERS_OVERRIDE="$PWD/openssl-crypto-policy.override" \
	LD_LIBRARY_PATH="$PWD/%{_vpath_builddir}/bin" \
	CTEST_OUTPUT_ON_FAILURE=1 \
	make -C "%{_vpath_builddir}" test ARGS="--verbose"

%files
%_enginesdir/gost.so
%doc %_enginesdir/README.gost

%files -n gostsum
%_bindir/gost*sum*
%_mandir/man1/gost*sum*

%changelog
* Mon Aug 17 2020 Alexander Bokovoy <abokovoy@redhat.com> - 1.1.1.0-0.1
- Initial build for upcoming gost-engine release 1.1.1.0
- Fixes: rhbz#1865169

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Dmitry Belyavskiy <beldmit@gmail.com> - 1.1.0.3-3
- Update after review by Tomas Mraz

* Sun Oct 07 2018 Dmitry Belyavskiy <beldmit@gmail.com> - 1.1.0.3-2
- Update after rpmlint

* Thu Oct 04 2018 Alexander Bokovoy <abokovoy@redhat.com> 1.1.0.3-1
- Initial build using git master commit 3383ad1
