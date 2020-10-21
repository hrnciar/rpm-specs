# Private libraries must not be exposed globally by RPM
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Summary:        The world's most popular Open Source IRC bot
Name:           eggdrop
Version:        1.8.4
Release:        2%{?dist}
License:        GPLv2+
URL:            https://www.eggheads.org/
Source0:        https://ftp.eggheads.org/pub/eggdrop/source/1.8/%{name}-%{version}.tar.gz
Source1:        https://ftp.eggheads.org/pub/eggdrop/source/1.8/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-E01C240484DE7DBE190FE141E7667DE1D1A39AFF.gpg
Patch0:         eggdrop-1.6.17-langdir.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  tcl-devel >= 8.3
BuildRequires:  zlib-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel >= 0.9.8
%else
BuildRequires:  openssl11-devel
%endif

%description
Eggdrop is the world's most popular Open Source IRC bot, designed
for flexibility and ease of use. It is extendable with Tcl scripts
and/or C modules, has support for the big five IRC networks and is
able to form botnets, share partylines and userfiles between bots.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch0 -p1 -b .langdir

%build
%configure \
%if 0%{?rhel} == 7
  --with-sslinc=%{_includedir}/openssl11 \
  --with-ssllib=%{_libdir}/openssl11
%endif

make config
# Parallel builds are not supported 
make

%install
mkdir -p $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir}}/
%make_install DEST=$RPM_BUILD_ROOT%{_datadir}/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{README,doc,eggdrop*,filesys,logs,modules,scripts/CONTENTS}
install -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 doc/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# Move modules into /usr/lib*
mv -f $RPM_BUILD_ROOT{%{_datadir}/%{name}/modules-%{version},%{_libdir}/%{name}}/

# Fix paths of example eggdrop.conf
sed -e '2d' -e '1s@^.*@#!%{_bindir}/%{name}@' \
    -e 's@scripts/@%{_datadir}/%{name}/scripts/@g' \
    -e 's@help/@%{_datadir}/%{name}/help/@g' \
    -e 's@modules/@%{_libdir}/%{name}/@g' \
    -e 's@text/"@%{_libdir}/%{name}/text/"@g' \
    eggdrop.conf > eggdrop.conf.mod
touch -c -r eggdrop.conf eggdrop.conf.mod
mv -f eggdrop.conf.mod eggdrop.conf

%files
%license COPYING
%doc FEATURES NEWS README doc/Changes1.8 eggdrop.conf
%doc doc/ABOUT doc/BANS doc/BOTNET doc/BUG-REPORT doc/FIRST-SCRIPT
%doc doc/IPV6 doc/MODULES doc/PARTYLINE doc/TEXT-SUBSTITUTIONS doc/TLS
%doc doc/TRICKS doc/USERS doc/WEIRD-MESSAGES
%doc doc/tcl-commands.doc doc/settings doc/html
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Robert Scheck <robert@fedoraproject.org> 1.8.4-1
- Upgrade to 1.8.4 (#1546581)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 1.6.21-21
- Add missing #include for gcc-10

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Robert Scheck <robert@fedoraproject.org> 1.6.21-15
- Added patch for build failures with "-Werror=format-security" 

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.6.21-13
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Robert Scheck <robert@fedoraproject.org> 1.6.21-10
- Added patch to make rebuilding with GCC 5 working

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.21-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 08 2012 Robert Scheck <robert@fedoraproject.org> 1.6.21-2
- Private libraries are not be exposed globally by RPM

* Sun Jan 08 2012 Robert Scheck <robert@fedoraproject.org> 1.6.21-1
- Upgrade to 1.6.21 (#771492)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Robert Scheck <robert@fedoraproject.org> 1.6.20-1
- Upgrade to 1.6.20

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.19-6
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Robert Scheck <robert@fedoraproject.org> 1.6.19-4
- Added upstream ctcpfix to solve CVE-2009-1789 (#502650)

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.6.19-3
- Rebuild for gcc 4.4 and rpm 4.6

* Sat Aug 30 2008 Robert Scheck <robert@fedoraproject.org> 1.6.19-2
- Re-diffed eggdrop configuration patch for no fuzz

* Tue Apr 22 2008 Robert Scheck <robert@fedoraproject.org> 1.6.19-1
- Upgrade to 1.6.19

* Mon Feb 25 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-16
- Cause the DNS linking against libc rather libdns (#433111)

* Fri Feb 15 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-15
- Rebuild for bind 9.5.0

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-14
- Added patch to provide better non-latin support (#429621)

* Sat Jan 05 2008 Robert Scheck <robert@fedoraproject.org> 1.6.18-13
- Rebuild for tcl 8.5

* Sat Dec 08 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-12
- Added a patch to fix some stack based overflows (CVE-2007-2807)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.6.18-11
- Rebuild for selinux ppc32 issue.

* Tue Aug 28 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-10
- Updated the license tag according to the guidelines

* Thu Jul 19 2007 Jesse Keating <jkeating@redhat.com> 1.6.18-9
- Rebuild for new bind

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-8
- Rebuild

* Tue Mar 13 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-7
- Rebuild for bind 9.4.0

* Wed Feb 14 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-6
- Rebuild for tcl 8.4

* Sat Feb 03 2007 Robert Scheck <robert@fedoraproject.org> 1.6.18-5
- Rebuild for tcl 8.5

* Wed Oct 25 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-4
- Rebuild

* Mon Oct 16 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-3
- Rebuild

* Sun Sep 03 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-2
- Rebuild for Fedora Core 6

* Sat Jul 15 2006 Robert Scheck <robert@fedoraproject.org> 1.6.18-1
- Upgrade to 1.6.18

* Mon Jun 19 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-4
- Replaced hardcoded LANGDIR with /usr/share/eggdrop/language to
  avoid use of EGG_LANGDIR env variable per default (#194481 #c9)

* Sun Jun 18 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-3
- Changes to match with Fedora Packaging Guidelines (#194481)

* Sun Mar 12 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-2
- Don't deliver autobotchk and botchk as documentation

* Sun Jan 22 2006 Robert Scheck <robert@fedoraproject.org> 1.6.17-1
- Upgrade to 1.6.17
- Initial spec file for Fedora Core
