Summary: Client and protocol library for the Couchbase project
Name: libcouchbase
Version: 2.10.8
Release: 1%{?dist}
License: ASL 2.0
BuildRequires: gcc, gcc-c++
BuildRequires: cmake >= 2.8.9
BuildRequires: pkgconfig(libevent) >= 2
BuildRequires: pkgconfig(libuv) >= 1
BuildRequires: libev-devel >= 3
BuildRequires: openssl-devel
BuildRequires: systemtap-sdt-devel, systemtap-devel
URL: https://developer.couchbase.com/server/other-products/release-notes-archives/c-sdk
Source: https://packages.couchbase.com/clients/c/%{name}-%{version}.tar.gz
%if ! (0%{?rhel} && 0%{?rhel} <= 7)
Recommends: %{name}-libevent%{_isa} = %{version}-%{release}
Suggests: %{name}-libev%{_isa} = %{version}-%{release}
Suggests: %{name}-tools%{_isa} = %{version}-%{release}
%endif

Patch0: %{name}-0001-enforce-system-crypto-policies.patch
Patch1: %{name}-0002-do-not-install-plugins-into-libdir.patch
Patch2: %{name}-0003-fix-pkgconfig-paths.patch

# exclude from "Provides" private IO plugins
%{?filter_provides_in: %filter_provides_in %{name}/%{name}.*\.so$}
%{?filter_setup}

%description
This package provides the core for libcouchbase. It contains an IO
implementation based on select(2). If preferred, you can install one
of the available back-ends (libcouchbase-libevent or libcouchbase-libev).
libcouchbase will automatically use the installed back-end. It is also
possible to integrate another IO back-end or write your own.

%package libevent
Summary: Couchbase client library - libevent IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libevent
This package provides libevent back-end for libcouchbase.

%package libev
Summary: Couchbase client library - libev IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libev
This package provides libev back-end for libcouchbase.

%package libuv
Summary: Couchbase client library - libuv IO back-end
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libuv
This package provides libuv back-end for libcouchbase.

%package tools
Summary: Couchbase client tools
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libevent%{?_isa} = %{version}-%{release}
%description tools
This is the CLI tools Couchbase project.

%package devel
Summary: Couchbase client library - Header files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the Couchbase client Library.

%prep
%autosetup -p1
%cmake -DLCB_NO_MOCK=1 -B . -S .

%build
%make_build

%install
%make_install

%check
# ARGS needed to pass arguments to ctest
export CTEST_OUTPUT_ON_FAILURE=1
make %{_smp_mflags} alltests test ARGS=%{_smp_mflags}

%ldconfig_scriptlets

%files
%{_libdir}/%{name}.so.*
%doc README.markdown RELEASE_NOTES.markdown
%license LICENSE
%dir %{_libdir}/%{name}
%{_datadir}/systemtap/tapset/libcouchbase.so*

%files libevent
%{_libdir}/%{name}/%{name}_libevent.so

%files libev
%{_libdir}/%{name}/%{name}_libev.so

%files libuv
%{_libdir}/%{name}/%{name}_libuv.so

%files tools
%{_bindir}/cbc*
%{_mandir}/man1/cbc*.1*
%{_mandir}/man4/cbcrc*.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Sep 24 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.8-1
- Update to 2.10.8

- Mon Sep  7 2020 Remi Collet <remi@remirepo.net> - 2.10.6-3
- fix FTBFS #1863985

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.6-1
- Update to 2.10.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.5-1
- Update to 2.10.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.4-1
- Update to 2.10.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.3-2
- Add explicit curdir on CMake invocation

* Thu Dec 20 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.3-1
- Update to 2.10.3

* Fri Nov 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.2-1
- Update to 2.10.2

* Fri Nov 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Thu Oct 18 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Fri Sep 21 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.5-1
- Update to 2.9.5

* Wed Aug 29 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.4-1
- Update to 2.9.4

* Wed Jul 18 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.3-1
- Update to 2.9.3

* Sat Jul 14 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.2-4
- Display output of failed tests

* Fri Jul 13 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.2-3
- Fix build with libuv-1.21.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Fri Jun 22 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Thu May 24 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Wed May 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.7-2
- Port patch for JSON datatype

* Wed May 02 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.7-1
- Update to 2.8.7

* Fri Apr 06 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.6-1
- Update to 2.8.6

* Fri Feb 23 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.5-1
- Update to 2.8.5

* Mon Feb 19 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.4-5
- Rebuilt with libevent-2.1.8

* Wed Feb 14 2018 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.4-4
- replace ldconfig scriptlets with macro
  https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Remi Collet <remi@remirepo.net> - 2.8.4-2
- filter private plugins (not shared libraries)

* Wed Dec 20 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.4-1
- Update to 2.8.4

* Wed Nov 22 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.3-2
- Parallel tests

* Wed Nov 22 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.3-1
- Update to 2.8.3

* Mon Nov 13 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.2-2
- Fix loading IO plugins

* Wed Oct 18 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Tue Sep 26 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.8.1-1
- Initial package
