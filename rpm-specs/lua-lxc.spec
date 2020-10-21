%if 0%{?fedora} || 0%{?rhel} >= 8
%global luaver 5.4
%else
%global luaver 5.1
%endif
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-lxc
Version:        3.0.2
Release:        8%{?dist}
Summary:        Lua binding for LXC
License:        LGPLv2+
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lua)
BuildRequires:  lxc-devel >= 3.0.0
BuildRequires:  make
BuildRequires:  gcc


%description
Linux Resource Containers provide process and resource isolation
without the overhead of full virtualization.

The lua-lxc package contains the Lua binding for LXC.


%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}core\\.so\\.0


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install


%files
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{lualibdir}/lxc
%{luapkgdir}/lxc.lua


%changelog
* Wed Aug  5 2020 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.2-8
- Update for Lua 5.4.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.2-4
- Build against Lua 5.3 on EPEL8.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.2-1
- Update to 3.0.2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.0-2
- Update description.

* Fri Apr  6 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.0-1
- New package.
