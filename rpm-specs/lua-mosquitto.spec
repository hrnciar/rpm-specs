%global the_so_name mosquitto.so

Name:           lua-mosquitto
Version:        0.3
Release:        2%{?dist}
License:        MIT
Summary:        Lua bindings to libmosquitto
Url:            https://github.com/flukso/%{name}/
Source:         https://github.com/flukso/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz


BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  lua >= 5.1
BuildRequires:  lua-devel >= 5.1
BuildRequires:  mosquitto-devel

Requires:       lua(abi) = %{lua_version}


%description
%{name} is a Lua library that provides complete bindings to the
Eclipse Mosquitto message broker (https://mosquitto.org) API.


%prep
%setup -q


%build
# To make sure we are using proper flags
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
export OPT=
%make_build %{the_so_name}


%install
%make_install


%files
%license LICENSE
%doc README.md
%{lua_libdir}/%{the_so_name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.3-1
- Update to the latest available version.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2-2
- Use simplified form of source Url.

* Tue Sep 26 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.2-1
- Initial RPM release.
