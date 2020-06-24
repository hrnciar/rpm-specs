%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname fifo

Name:           lua-%{luapkgname}
Version:        0.2
Release:        3%{?dist}
Summary:        FIFO library for Lua

License:        MIT
URL:            https://github.com/daurnimator/%{luapkgname}.lua
Source0:        https://github.com/daurnimator/%{luapkgname}.lua/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua
BuildRequires:  pandoc

%description
A lua library/'class' that implements a FIFO. Objects in the fifo
can be of any type, including nil.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        FIFO library for Lua %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
A lua library/'class' that implements a FIFO. Objects in the fifo
can be of any type, including nil.
%endif

%prep
%setup -q -n fifo.lua-%{version}

%build
pandoc doc/index.md -s -t man -o fifo.lua.3

%install
install -D -p -m 0644 fifo.lua %{buildroot}/%{luapkgdir}/fifo.lua
install -D -p -m 0644 fifo.lua.3 %{buildroot}/%{_mandir}/man3/fifo.lua.3

%if 0%{?fedora} || 0%{?rhel} > 7
install -D -p -m 0644 fifo.lua %{buildroot}/%{luacompatpkgdir}/fifo.lua
%endif

%files
%license LICENSE
%{_mandir}/man3/fifo.lua.3*
%{luapkgdir}/fifo.lua

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%license LICENSE
%{_mandir}/man3/fifo.lua.3*
%{luacompatpkgdir}/fifo.lua
%endif

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.2-1
- Initial package for Fedora 28+ and EPEL 7
