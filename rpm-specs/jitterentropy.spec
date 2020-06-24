Name:	jitterentropy
Version:	2.2.0
Release:	2%{?dist}
Summary:	Library implementing the jitter entropy source

License:	BSD or GPLv2
URL:		https://github.com/smuellerDD/jitterentropy-library
Source0:	%url/archive/%{name}-library-%{version}.tar.gz

BuildRequires: gcc

# Disable Upstream Makefiles debuginfo strip on install
Patch0: jitterentropy-rh-makefile.patch
%description
Library implementing the CPU jitter entropy source

%package devel
Summary: Development headers for jitterentropy library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for jitterentropy

%prep
%autosetup -n %{name}-library-%{version}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}/usr/include/
%make_install PREFIX=/usr LIBDIR=%{_lib}

%ldconfig_scriptlets

%files
%doc README.md
%license COPYING COPYING.bsd COPYING.gplv2
%{_libdir}/libjitterentropy.so.2*


%files devel
%{_includedir}/*
%{_libdir}/libjitterentropy.so
%{_mandir}/man3/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Neil Horman <nhorman@redhat.com> - 2.2.0-1
- Update to latest upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 21 2018 Neil Horman <nhorman@tuxdriver.com> - 2.1.2-3
- Drop static library
- Fix up naming
- Add gcc buildrequires
- Fix files glob

* Thu Sep 13 2018 Neil Horman <nhorman@tuxdriver.com> - 2.1.2-2
- Fixed license
- Fixed up some macro usage in spec file
- Documented patches
- Modified makefile to use $(INSTALL) macro

* Thu Sep 06 2018 Neil Horman <nhorman@tuxdriver.com> - 2.1.2-1
- Initial import
