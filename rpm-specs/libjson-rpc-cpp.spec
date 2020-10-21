%global srcname jsonrpccpp

Name:           libjson-rpc-cpp
Version:        1.1.0
Release:        13%{?dist}
Summary:        C++ framework for json-rpc (json remote procedure call)

License:        MIT
URL:            https://github.com/cinemast/libjson-rpc-cpp
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fix finding catch in Fedora installation. We ship catch library in
# many files, not in one. Those are located under /usr/include/catch
Patch0:         catch-path_suffix-cmake.patch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake(jsoncpp)
BuildRequires:  argtable-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  hiredis-devel
BuildRequires:  catch1-devel
# Documentation
BuildRequires:  doxygen

Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{version}-%{release}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       %{name}-stub%{?_isa} = %{version}-%{release}

%description
%{summary}. This package is meta-package which requires:
* %{name}-common
* %{name}-client
* %{name}-server
* %{name}-stub

%package devel
Summary:        Development files for JSON-RPC C++ framework
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{version}-%{release}
Requires:       %{name}-server%{?_isa} = %{version}-%{release}
Requires:       %{name}-stub%{?_isa} = %{version}-%{release}
Requires:       jsoncpp-devel%{?_isa}
Requires:       libmicrohttpd-devel%{?_isa}
Requires:       hiredis-devel%{?_isa}

%description devel
This package provides all required developer resources like header-files of the
%{name} framework.

Features of this framework include:

* Type checking
* Malformed request handling
* Handling batch procedure calls
* JSON-RPC Method invocation
* JSON-RPC Notification invocation
* Simple Interface for implementing additional Server-Connectors beside HTTP
* Positional and named parameters

%package common
Summary:        Common functionality for %{name}-server and %{name}-client
Recommends:     %{name}-client%{?_isa} = %{version}-%{release}
Recommends:     %{name}-server%{?_isa} = %{version}-%{release}
Recommends:     %{name}-tools%{?_isa} = %{version}-%{release}

%description common
This library provides common classes for the libjson-rpc-cpp framework like:

* Exceptions
* Error-Codes
* Specification Parsers and Writers
* Procedure parameter validation

This package usually only makes sense with %{name}-client and/or
%{name}-server.

%package client
Summary:        Library implementing json-rpc C++ clients
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Recommends:     %{name}-tools%{?_isa} = %{version}-%{release}

%description client
This library provides classes to easily implement JSON-RPC C++ clients.
It comes with a built in HTTP-Client connector (based on libcurl) for
easy data exchange. It is fully JSON-RPC 2.0 and JSON-RPC 1.0 compatible,
including:

* Type checking
* Error response handling
* Batch procedure calls
* JSON-RPC Method invocation
* JSON-RPC Notification invocation
* Interface for additional Client-Connectors beside HTTP
* Positional and named parameters

%package server
Summary:        Library implementing json-rpc C++ clients
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Recommends:     %{name}-tools%{?_isa} = %{version}-%{release}

%description server
This library provides classes to easily implement JSON-RPC C++ Server
applications. It comes with a built in HTTP-Server connector (based on
libmicrohttpd) for easy data exchange. It is fully JSON-RPC 2.0 and
JSON-RPC 1.0 compatible, including:

* Type checking
* Malformed request handling
* Handling batch procedure calls
* JSON-RPC Method invocation
* JSON-RPC Notification invocation
* Simple Interface for implementing additional Server-Connectors beside HTTP
* Positional and named parameters

%package stub
Summary:        Library for stub generation of %{name} based applications
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Recommends:     %{name}-tools%{?_isa} = %{version}-%{release}

%description stub
This package provides the stub generator library for the %{name}
framework. It can automatically generate full functioning C++ and JavaScript
JSON-RPC Client classes, which are ready to use.

For JSON-RPC Server applications, this library can generate an abstract C++
class which just has to be sub classed and implement all pure virtual methods.
To make this possible, a interface description file (in the JSON format) is
required, which lists all available methods with corresponding parameters and
types.

%package tools
Summary:        Stub generator for %{name} based applications
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description tools
This package provides the stub generator for the libjson-rpc-cpp framework.
It can automatically generate full functioning C++ and JavaScript JSON-RPC
Client classes, which are ready to use.

For JSON-RPC Server applications, this tool can generate an abstract C++
class which just has to be sub classed and implement all pure virtual methods.
To make this possible, a simple interface description file (in the JSON
format) is required, which lists all available methods with corresponding
parameters and types.

%prep
%autosetup -p1
# Removing CMake file which will try to download catch
rm -rf src/catch
# Fix libdirs
find -name 'CMakeLists.txt' -exec sed -i 's,lib/${CMAKE_LIBRARY_PATH},%{_lib},g' {} ';'
# We are not going to run redis tests..
rm -vf src/test/test_connector_redis.cpp

%build
mkdir %{_target_platform}
pushd %{_target_platform}
  %cmake .. -DWITH_COVERAGE=OFF
  %make_build
popd

%install
%make_install -C %{_target_platform}
# XXX: For now, remove it.. because it seems like wrong location
rm -vrf %{buildroot}%{_libdir}/%{name}

%check
# needs networking for some tests
pushd %{_target_platform}
  ctest -VV
popd

%files devel
%{_includedir}/%{srcname}/
%{_libdir}/lib%{srcname}-common.so
%{_libdir}/pkgconfig/lib%{srcname}-common.pc
%{_libdir}/lib%{srcname}-client.so
%{_libdir}/pkgconfig/lib%{srcname}-client.pc
%{_libdir}/lib%{srcname}-server.so
%{_libdir}/pkgconfig/lib%{srcname}-server.pc
%{_libdir}/lib%{srcname}-stub.so
%{_libdir}/pkgconfig/lib%{srcname}-stub.pc

%ldconfig_scriptlets common

%files common
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_libdir}/lib%{srcname}-common.so.*

%ldconfig_scriptlets client

%files client
%{_libdir}/lib%{srcname}-client.so.*

%ldconfig_scriptlets server

%files server
%{_libdir}/lib%{srcname}-server.so.*

%ldconfig_scriptlets stub

%files stub
%{_libdir}/lib%{srcname}-stub.so.*

%files tools
%{_bindir}/jsonrpcstub
%{_mandir}/man1/jsonrpcstub.1*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.0-11
- Rebuild (jsoncpp)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.0-9
- Rebuild (jsoncpp)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.0-7
- Rebuild (jsoncpp)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-3
- Switch to %%ldconfig_scriptlets

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- catch → catch1

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-3
- Rebuilt for jsoncpp.so.20

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-2
- Rebuilt for jsoncpp-1.8.3

* Mon Aug 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.0-1
- Update to 0.7.0

* Sat Apr 02 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6.0-2
- Fix requirements for -devel
- Use packaged fedora's catch

* Thu Mar 24 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6.0-1
- Initial package
