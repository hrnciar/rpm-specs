
%global _hardened_build	1
%define _legacy_common_support	1

# version revision
%global revision	8497

Name:		yadifa
Version:	2.3.9
Release:	4%{?dist}
Summary:	Lightweight authoritative Name Server with DNSSEC capabilities

License:	BSD
URL:		http://www.yadifa.eu
Source0:	http://cdn.yadifa.eu/sites/default/files/releases/%{name}-%{version}-%{revision}.tar.gz
Source1:	yadifad.service
Source3:	yadifa.logrotate

BuildRequires:	gcc
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	openssl-devel
BuildRequires:	sed

Requires:	yadifa-libs = %{version}-%{release}

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
BuildRequires:		systemd


%description
YADIFA is a name server implementation developed from scratch by .eu.
It is portable across multiple operating systems and supports DNSSEC,
TSIG, DNS notify, DNS update, IPv6.

%package libs
Summary:	Libraries used by the YADIFA packages

%description libs
Contains libraries used by YADIFA DNS server

%package tools
Summary:	Remote management client for YADIFA DNS server

%description tools
Contains utility for YADIFA DNS server remote management

%package devel
Summary:	Header files and libraries needed for YADIFA development
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The yadifa-devel package contains header files and libraries
required for development with YADIFA DNS server


%prep
%setup -q -n %{name}-%{version}-%{revision}

%build
export CPPFLAGS="%{optflags} -DNDEBUG -g"
export LDFLAGS="$LDFLAGS -lssl -lcrypto"

%configure \
    --with-tools \
    --enable-rrl \
    --enable-nsid \
    --enable-ctrl \
    --enable-dynamic-provisioning \
    --enable-messages \
    --enable-shared \
    --disable-static

# don't mess with rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/libtool
# avoid unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/libtool
# adjust build options
sed -i 's|-mtune=native||g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
sed -i 's|= -fno-ident|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
sed -i 's|= -ansi|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
sed -i 's|= -pedantic|=|g' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
sed -i '/^YRCFLAGS = -DNDEBUG $(CCOPTIMISATIONFLAGS) -DCMR/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
sed -i '/^YPCFLAGS = -DNDEBUG $(CCOPTIMISATIONFLAGS) -pg -DCMP/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
sed -i '/^YDCFLAGS = -DDEBUG $(DEBUGFLAGS) -DCMD/d' \
    {.,bin/yadifa,lib/dnscore,lib/dnsdb,lib/dnslg,lib/dnszone,sbin/yadifad}/Makefile
# adjust additional key options
sed -i 's|^include "keys.conf"|#include "keys.conf"|' etc/yadifad.conf.example
sed -i '/^<\/key>/a \ \n<key>\n \ name \ abroad-admin-key\n \ algorithm \ hmac-md5\n \ secret \ AbroadAdminTSIGKey==\n<\/key>' \
    etc/yadifad.conf.example

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -Dpm 0644 etc/yadifad.conf.example %{buildroot}%{_sysconfdir}/yadifad.conf
mkdir -p %{buildroot}%{_localstatedir}/log/yadifa
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_defaultdocdir}/yadifa

# bash completion
for comp in yadifa yadifad; do
install -Dpm 0644 etc/${comp}.bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/${comp}
done

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/yadifad.service

install -Dpm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/yadifa


%post
%systemd_post yadifad.service
exit 0

%preun
%systemd_preun yadifad.service
exit 0

%postun
%systemd_postun_with_restart yadifad.service
exit 0

%ldconfig_scriptlets libs


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc etc/*.conf.example
%config(noreplace) %{_sysconfdir}/yadifad.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/yadifa
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/yadifad
%{_unitdir}/yadifad.service
%{_localstatedir}/zones
%{_localstatedir}/log/yadifa
%{_sbindir}/yadifad
%{_mandir}/man5/yadifa.*.5*
%{_mandir}/man5/yadifad.*.5*
%{_mandir}/man8/yadifad.8*

%files libs
%{_libdir}/libdnscore.so.6*
%{_libdir}/libdnsdb.so.6*
%{_libdir}/libdnslg.so.6*
%{_libdir}/libdnszone.so.6*

%files tools
%license COPYING
%doc AUTHORS
%{_bindir}/yadifa
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/yadifa
%{_mandir}/man8/yadifa.8*

%files devel
%{_includedir}/dnscore
%{_includedir}/dnsdb
%{_includedir}/dnslg
%{_includedir}/dnszone
%{_libdir}/libdnscore.so
%{_libdir}/libdnsdb.so
%{_libdir}/libdnslg.so
%{_libdir}/libdnszone.so


%changelog
* Fri Feb 28 2020 Denis Fateyev <denis@fateyev.com> - 2.3.9-4
- Add "legacy_common_support" build option

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Denis Fateyev <denis@fateyev.com> - 2.3.9-1
- Update to 2.3.9 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Denis Fateyev <denis@fateyev.com> - 2.3.8-1
- Update to 2.3.8 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 16 2017 Denis Fateyev <denis@fateyev.com> - 2.3.7-1
- Update to 2.3.7 release

* Fri Dec 01 2017 Denis Fateyev <denis@fateyev.com> - 2.2.6-2
- Unified service configuration across all branches

* Sat Sep 30 2017 Denis Fateyev <denis@fateyev.com> - 2.2.6-1
- Update to 2.2.6 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Denis Fateyev <denis@fateyev.com> - 2.2.5-1
- Update to 2.2.5 release

* Fri Apr 14 2017 Denis Fateyev <denis@fateyev.com> - 2.2.4-2
- Added aliased IPs support ("--enable-messages" option)

* Sat Apr 08 2017 Denis Fateyev <denis@fateyev.com> - 2.2.4-1
- Update to 2.2.4 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Denis Fateyev <denis@fateyev.com> - 2.2.3-1
- Update to 2.2.3 release

* Sat Sep 03 2016 Denis Fateyev <denis@fateyev.com> - 2.2.1-1
- Update to 2.2.1 release

* Sat Jul 16 2016 Denis Fateyev <denis@fateyev.com> - 2.2.0-1
- Update to 2.2.0 release

* Tue Feb 23 2016 Denis Fateyev <denis@fateyev.com> - 2.1.6-1
- Update to 2.1.6 release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Denis Fateyev <denis@fateyev.com> - 2.1.5-1
- Update to 2.1.5 release

* Wed Sep 30 2015 Denis Fateyev <denis@fateyev.com> - 2.1.3-1
- Update to 2.1.3 release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Denis Fateyev <denis@fateyev.com> - 2.0.6-1
- Update to 2.0.6 release

* Sun Dec 21 2014 Denis Fateyev <denis@fateyev.com> - 2.0.4-1
- Update to 2.0.4 release

* Sat Oct 18 2014 Denis Fateyev <denis@fateyev.com> - 2.0.0-1
- Update to 2.0.0 release
- New program features added

* Thu Aug 28 2014 Denis Fateyev <denis@fateyev.com> - 1.0.3-2
- Build options clarification
- Minor specfile cleanup

* Sat Aug 16 2014 Denis Fateyev <denis@fateyev.com> - 1.0.3-1
- Initial Fedora RPM release
