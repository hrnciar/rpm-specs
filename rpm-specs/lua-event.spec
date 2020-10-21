%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_libdir: %global lua_libdir %{_libdir}/lua/%{lua_version}}
%{!?lua_pkgdir: %global lua_pkgdir %{_datadir}/lua/%{lua_version}}

%global enable_docs 1
%{?el6:%global enable_docs 0}
%{?el7:%global enable_docs 0}
%{?el8:%global enable_docs 0}

Name:           lua-event
Version:        0.4.6
Release:        6%{?dist}
Summary:        This is a binding of libevent to Lua

License:        MIT
URL:            https://github.com/harningt/luaevent/
Source0:        https://github.com/harningt/luaevent/archive/v%{version}/luaevent-%{version}.tar.gz

# Make sure CFLAGS/LDFLAGS are respected.
Patch0:         %{name}-0.4.3-respect-cflags.patch
# Conditionalize env calls which are gone in modern lua
Patch1:         luaevent-0.4.3-envfix.patch

BuildRequires:  gcc
BuildRequires:  lua       >= %{lua_version}
BuildRequires:  lua-devel >= %{lua_version}
BuildRequires:  libevent-devel >= 1.4
Requires:       lua-socket

%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires:       lua(abi)   = %{lua_version}
%else
Requires:       lua       >= %{lua_version}
%endif

%description
This package contains the bindings for libevent, a synchronous event
notification library that provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout has been
reached.

# ikiwiki is not available on EPEL
%if 0%{?enable_docs}
%package doc
Summary:        Documentation for %{name}
BuildRequires:  ikiwiki

%description doc
%{summary}.
%endif


%prep
%setup -q -n luaevent-%{version}
%patch0 -p1
%patch1 -p1 -b .envfix
# Remove 0-byte file.
rm -f doc/modules/luaevent.mdwn


%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="%{optflags} -shared %{?__global_ldflags}"
%make_build

%if 0%{?enable_docs}
/bin/sh makeDocs.sh
%endif


%install
%make_install \
    INSTALL_DIR_LUA=%{lua_pkgdir} \
    INSTALL_DIR_BIN=%{lua_libdir}


%files
%doc CHANGELOG README doc/*
%dir %{lua_libdir}/luaevent
%{lua_libdir}/luaevent/core.so
%{lua_pkgdir}/luaevent.lua

%if 0%{?enable_docs}
%files doc
%doc html/*
%endif


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.4.6-5
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Robert Scheck <robert@fedoraproject.org> - 0.4.6-3
- Correct GitHub source URL
- Ensure linker flag injection

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Robert Scheck <robert@fedoraproject.org> - 0.4.6-1
- Upgrade to 0.4.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.4.3-9
- rebuild for lua 5.3
- conditionalize env calls that are no longer in modern lua

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-6
- fix conditional logic

* Sat Aug 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-5
- temporarily disable docs for f20 due as ikiwiki has dependency problems

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 0.4.3-3
- rebuild for lua 5.2

* Wed Apr 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-2
- amend directory ownership
- include markdown documentation
- change from %%define to %%global

* Tue Apr 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-1
- update to upstream release 0.4.3
- fix typo in %%description
- fix license tag
- make sure CFLAGS/LDFLAGS are respected
- put documentation in -doc subpackage, and only build for Fedora as ikiwiki
  is not available on EPEL

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- initial package
