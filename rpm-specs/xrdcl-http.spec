%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

Name:		xrdcl-http
Version:	5.0.2
Release:	1%{?dist}
Summary:	HTTP client plug-in for XRootD

License:	BSD
URL:		https://github.com/xrootd/%{name}
Source0:	https://github.com/xrootd/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake3
BuildRequires:	gcc-c++
BuildRequires:	xrootd-client-devel
BuildRequires:	davix-devel

%description
xrdcl-http is an XRootD client plugin which allows XRootD to interact
with HTTP repositories.

%prep
%setup -q

%build
%cmake3 -DPLUGIN_VERSION:STRING=$(xrootd-config --plugin-version) \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}
%cmake3_build

%install
%cmake3_install

# client plug-in config
mkdir -p %{buildroot}%{_sysconfdir}/xrootd/client.plugins.d
sed 's!/usr/local/lib!%{_libdir}!' config/http.client.conf.example > \
    %{buildroot}%{_sysconfdir}/xrootd/client.plugins.d/xrdcl-http-plugin.conf

%ldconfig_scriptlets

%files
%{_libdir}/libXrdClHttp-5.so
%{_sysconfdir}/xrootd/client.plugins.d/xrdcl-http-plugin.conf
%license LICENSE
%doc README.md

%changelog
* Fri Sep 18 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0.2-1
- Update to version 5.0.2
- Drop patches (accepted upstream or previously backported)

* Thu Aug 27 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0.1-1
- Update to version 5.0.1
- Don't use versioned plugin names in configuration
- Backport plugin version change from git master

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.12.2-1
- Update to version 4.12.2

* Sat Mar 21 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.11.3-1
- Update to version 4.11.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.10.0-2
- Correct License tag and install LICENSE file
- Install README.md file

* Sun Jul 28 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.10.0-1
- Initial Fedora package
