Name:           trickle
Version:        1.07
Release:        33%{?dist}
Summary:        Portable lightweight userspace bandwidth shaper

License:        BSD with advertising
URL:            http://monkey.org/~marius/pages/?page=trickle
Source0:        http://monkey.org/~marius/trickle/%{name}-%{version}.tar.gz
Source1:        %{name}d.conf

BuildRequires:  gcc
BuildRequires:  libevent-devel
%if 0%{?fedora} >= 28
BuildRequires:	libtirpc-devel
%endif

Patch0:         %{name}-%{version}-include_netdb.patch
Patch1:         %{name}-%{version}-libdir.patch
Patch2:         %{name}-%{version}-CVE-2009-0415.patch
Patch3:         %{name}-%{version}-bwsta_getdelay-stop-if-no-packets.patch
# Fedora specific: https://bugzilla.redhat.com/show_bug.cgi?id=1037366
Patch4:         %{name}-%{version}-err-Werror=format-security.patch

%description
trickle is a portable lightweight userspace bandwidth shaper.
It can run in collaborative mode or in stand alone mode.

trickle works by taking advantage of the unix loader preloading.
Essentially it provides, to the application,
a new version of the functionality that is required
to send and receive data through sockets.
It then limits traffic based on delaying the sending
and receiving of data over a socket.
trickle runs entirely in userspace and does not require root privileges.

%prep
%setup -q
%patch0 -p1 -b .include_netdb
%patch1 -p1 -b .libdir
%patch2 -p1 -b .cve
%patch3 -p1
%patch4 -p1 -b .err-Werror=format-security.patch
touch -r configure aclocal.m4 Makefile.in stamp-h.in

iconv -f ISO88591 -t UTF8 < README > README.UTF8
mv README.UTF8 README


%build
%if 0%{?fedora} >= 28
# Workaround for https://fedoraproject.org/wiki/Changes/SunRPCRemoval
# https://bugzilla.redhat.com/show_bug.cgi?id=1556510
export CFLAGS="%build_cflags $(pkg-config --cflags libtirpc)"
export LDFLAGS="%build_ldflags $(pkg-config --libs libtirpc)"
%endif
%configure
# Parallel make is unsafe for this package, so %%{?_smp_mflags} is not used
make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# for rpmlint warning : unstripped-binary-or-object
chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}-overload.so
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}


%files
%doc LICENSE README TODO
%dir %{_libdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}d.conf
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}d
%{_libdir}/%{name}/%{name}-overload.so
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{name}d.conf.5.gz
%{_mandir}/man8/%{name}d.8.gz


%changelog
* Tue Sep 29 20:46:23 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.07-33
- Rebuilt for libevent 2.1.12

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-32
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.07-26
- Workaround for F-28 SunRPCRemoval to fix FTBFS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 6 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 1.07-17
- Add Fedora specific patch trickle-1.07-err-Werror=format-security.patch to fix trickle FTBFS if "-Werror=format-security" flag is used (bz#1037366)
- Fix bogus date in changelog.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 15 2011 Alon Levy <alevy@redhat.com> 1.07-12
- Fix endless loop in bwstat_delay (seen with spicec)
* Sun Feb 13 2011 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-11
- Revert to the working patch
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Thu Feb 12 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-7
- Replace sed with a patch for #484065 (CVE-2009-0415)
* Fri Feb  6 2009 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-6
- Add a fix for bug #484065 (CVE-2009-0415)
* Thu Aug 28 2008 Manuel Wolfshant <wolfy@fedoraproject.org> 1.07-5
- modify trickle-1.07-include_netdb.patch to adjust for building with fuzz=0
* Sun Jun 29 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-4
- rebuild for new libevent
* Mon Jun 16 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-3
- add configure.in
- add default configuration file for trickled
* Sun Jun 15 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-2
- Licence changed
- ldconfig no more used
- dir macro used for libdir/name
- config.h file modified (/lib/ hardcoded)
* Sun Jun  8 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.07-1
- Rebuild for version 1.07
- Removed smp_mflags flag for make
* Sat Jun  7 2008 Nicoleau Fabien <nicoleau.fabien@gmail.com> 1.06-1
- Initital build
