# Header-only library.
%global debug_package %{nil}

Name:           cppzmq
Version:        4.7.1
Release:        1%{?dist}
Summary:        Header-only C++ binding for libzmq

License:        MIT
URL:            https://zeromq.org
Source0:        https://github.com/zeromq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/zeromq/cppzmq/issues/283
Patch0001:      0001-Fix-broken-test-macro-condition.patch
# https://github.com/zeromq/cppzmq/pull/288
Patch0002:      0002-Use-external-Catch2.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  cmake(Catch2)

%global _description \
cppzmq is a C++ binding for libzmq. \
\
cppzmq maps the libzmq C API to C++ concepts. In particular, it is type-safe, \
provides exception-based error handling, and provides RAII-style classes that \
automate resource management. cppzmq is a light-weight, header-only binding.

%description %{_description}


%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

Requires:       pkgconfig(libzmq)

%description devel %{_description}


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files devel
%doc README.md
%license LICENSE
%{_includedir}/zmq*.hpp
%{_datadir}/cmake/%{name}


%changelog
* Tue Oct 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.7.1-1
- Update to latest version (#1884030)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.6.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.5.0-1
- Update to latest version

* Sun Sep 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.4.1-1
- Update to latest version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-2
- Add missing Requires on zeromq

* Tue Jan 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-1
- Initial package (split out of zeromq)
