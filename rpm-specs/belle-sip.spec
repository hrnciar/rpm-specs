Name:           belle-sip
Version:        1.4.2
Release:        11%{?dist}
Summary:        Linphone SIP stack
License:        GPLv2+ and BSD and BSD with advertising and MIT
URL:            http://www.linphone.org/technical-corner/belle-sip/overview
Source0:        http://www.linphone.org/releases/sources/belle-sip/%{name}-%{version}.tar.gz
# Patch0 generated with commands running in src/grammars
# /usr/bin/java -Xmx256m -jar antlr-3.4-complete.jar  -make -Xmultithreaded -Xconversiontimeout 10000 -fo  . ./belle_sip_message.g
# /usr/bin/java -Xmx256m -jar antlr-3.4-complete.jar  -make -Xmultithreaded -Xconversiontimeout 10000 -fo .  belle_sdp.g
# antlr-3.4-complete.jar downloaded from https://github.com/antlr/website-antlr3/blob/gh-pages/download/antlr-3.4-complete.jar
Patch0:         belle-sip-1.4.2-antlr34.patch
Patch1:         belle-sip-1.4.2-fix-typo.patch
# readdir_r is deprecated, other compiler warning fixes
Patch2:		belle-sip-1.4.2-warn.patch
BuildRequires:  gcc-c++
BuildRequires:  antlr3-tool
BuildRequires:  antlr3-C-devel
BuildRequires:  mbedtls-devel
BuildRequires:  libtool
# The version is used from src/md5.c line:
# /* $Id: md5.c,v 1.6 2002/04/13 19:20:28 lpd Exp $ */
Provides: bundled(md5-deutsch) = 1.6

%description
Belle-sip is an object oriented C written SIP stack used by Linphone.

%package devel
Summary:       Development libraries for belle-sip
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description    devel
Libraries and headers required to develop software with belle-sip.

%prep
%setup -q
%patch0 -p1 -b .antlr34
%patch1 -p1 -b .typo
%patch2 -p1 -b .warn

autoreconf -ifv


%build
%configure --disable-tests \
           --disable-silent-rules \
           --disable-static \
%if 0%{?fedora} > 22
           --disable-tls
%endif

%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%doc README
%{_libdir}/libbellesip.so.0*

%files devel
%{_includedir}/belle-sip
%{_libdir}/libbellesip.so
%{_libdir}/pkgconfig/belle-sip.pc

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Stuart Gathman <stuart@gathman.org> - 1.4.2-9
- Fix call to deprecated readdir_r
- Fix other compiler warnings

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.2-2
- Fix typo in comparison code (patch from bug #1050744)

* Sat Nov  7 2015 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.2-1
- belle-sip-1.4.2

* Sat Sep 19 2015 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.1-2
- disabled TLS for F23+ (mbedtls 2 incompatible)

* Fri Sep  4 2015 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.1-1
- belle-sip-1.4.1
- removed atlr3 3.4 SOURCE1
- added patch with files generated by antlr-3.4-complete.jar
- BR: mbedtls-devel instead of polarssl-devel

* Sun Feb 15 2015 Alexey Kurov <nucleo@fedoraproject.org> - 1.4.0-1
- belle-sip-1.4.0
- update Source0 URL
- use %%license macro

* Sun Feb 15 2015 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.3-1
- belle-sip-1.3.3
- added atlr3 3.4 SOURCE1
- License: GPLv2+ and BSD and BSD with advertising and MIT
- Provides: bundled(md5-deutsch) = 1.6

* Fri Feb 21 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.3.0-1
- belle-sip-1.3.0
- revert fix FSF address in COPYING

* Sat Jan 18 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.4-3
- License: GPLv2+
- fix FSF address in COPYING

* Sun Jan 12 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.4-2
- add %%{?_isa} in -devel Requires
- add verbose option to autoreconf
- verbose build output

* Thu Jan  9 2014 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.4-1
- Initial RPM release
