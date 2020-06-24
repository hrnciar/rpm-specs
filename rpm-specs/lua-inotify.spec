%global gitrev   98822877a9d42
%global alphatag 20130510git%{gitrev}

%global luaver 5.2
%global lualibdir %{_libdir}/lua/%{luaver}

Name:           lua-inotify
Version:        1.0
Release:        0.19.%{alphatag}%{?dist}
Summary:        Inotify bindings for Lua

License:        MIT
URL:            http://hoelz.ro/projects/linotify
# Source only available from Git; instructions below
# git clone git://github.com/hoelzro/linotify.git
# (cd linotify && git archive --format=tar \
#  --prefix=linotify-%%{version}-%%{gitrev}/ %%{gitrev} \
#  | xz - ) > linotify-%%{version}-%%{gitrev}.tar.xz
Source0:        linotify-%{version}-%{gitrev}.tar.xz

BuildRequires:  gcc
BuildRequires:  lua-devel >= %{luaver}
Requires:       lua >= %{luaver}

%description
This is linotify, a binding for Linux's inotify library to Lua.


%prep
%setup -q -n linotify-%{version}-%{gitrev}
# do not strip when installing; preserve modtime (not strictly required)
sed -i.nostrip -e 's|install -D -s|install -D -p|' Makefile


%build
# original CFLAGS is computed using Lua's pkgconfig file, but ours
# does not set any.
#
# Overriding with the default %%{optflags}, and keeping the -fPIC
# from the original CFLAGS as the build target is a shared object
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_PATH=%{lualibdir}


%files
%doc COPYRIGHT README.md
%{lualibdir}/inotify.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.0-0.6.20130510git98822877a9d42
- update to latest git, rebuild for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.20110529git6d0f7a0973cfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.20110529git6d0f7a0973cfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.20110529git6d0f7a0973cfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  8 2011 Michel Salim <salimma@fedoraproject.org> - 1.0-0.2.20110529git6d0f7a0973cfb
- add source checkout instructions
- add explanation for overriding CFLAGS

* Tue Aug 16 2011 Michel Salim <salimma@fedoraproject.org> - 1.0-0.1.20110529git6d0f7a0973cfb
- Initial package