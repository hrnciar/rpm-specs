%global luaver 5.3
%global luapkgdir %{_datadir}/lua/%{luaver}

%global pkgname moonscript
#global src_suffix -2

Name:           lua-%{pkgname}
Version:        0.5.0
Release:        4%{?dist}
Summary:        A little language that compiles to Lua

# license text part of README.md
License:        MIT
URL:            http://moonscript.org/
Source0:        https://github.com/leafo/moonscript/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  lua >= 5.1
BuildRequires:  lua-alt-getopt >= 0.7
BuildRequires:  lua-filesystem >= 1.5
# avoid lpeg 0.11 per upstream rockspec
BuildRequires:  lua-lpeg >= 0.12
%if 0%{?el6}
Requires:       lua >= %{luaver}
%else
Requires:       lua(abi) = %{luaver}
%endif
Requires:       lua-alt-getopt >= 0.7
Requires:       lua-filesystem >= 1.5
Requires:       lua-lpeg >= 0.12
# lua-inotify is a soft requirement;
# needed for the directory watching feature
Requires:       lua-inotify


%description
MoonScript is a dynamic scripting language that compiles into Lua. It
gives you the power of Lua combined with a rich set of features.

MoonScript can either be compiled into Lua and run at a later time, or
it can be dynamically compiled and run using the moonloader. It’s as
simple as require "moonscript" in order to have Lua understand how to
load and run any MoonScript file.

Because it compiles right into Lua code, it is completely compatible
with alternative Lua implementations like LuaJIT, and it is also
compatible with all existing Lua code and libraries.

The command line tools also let you run MoonScript directly from the
command line, like any first-class scripting language.


%prep
%autosetup -n %{pkgname}-%{version}


%build
# tarball already ships with precompiled sources
# make compile

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p bin/moon{,c} $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{luapkgdir}
cp -pr moon moonscript $RPM_BUILD_ROOT%{luapkgdir}/


%check
# wait until dependencies are packaged
#make test


%files
%doc CHANGELOG.md README.md docs/*
%{_bindir}/moon
%{_bindir}/moonc
%{luapkgdir}/moon
%{luapkgdir}/moonscript


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 26 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Tom Callaway <spot@fedoraproject.org> - 0.2.4-4
- rebuild for lua 5.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul  4 2013 Michel Salim <salimma@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 0.2.3-2
- rebuild for lua 5.2

* Mon Feb 11 2013 Michel Salim <salimma@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  8 2011 Michel Salim <salimma@fedoraproject.org> - 0.1.0-2
- Clean up spec file
- Add explicit checkout instructions

* Tue Aug 16 2011 Michel Salim <salimma@fedoraproject.org> - 0.1.0-1
- Initial package
