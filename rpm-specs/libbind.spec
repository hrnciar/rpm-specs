#%define PREVER rc1
#%define VERSION %{version}%{PREVER}
%define VERSION %{version}

Name:		libbind
Version:	6.0
Release:	22%{?dist}
Summary:	ISC's standard resolver library

License:	ISC
URL:		ftp://ftp.isc.org/isc/libbind/
Source0:	ftp://ftp.isc.org/isc/libbind/%{VERSION}/libbind-%{VERSION}.tar.gz
Source1:	libbind.pc

BuildRequires:	groff, gcc

Patch0:     libbind60-install.patch
Patch1:     libbind-aarch64.patch

%description
ISC's libbind provides the standard resolver library,
for communicating with domain name servers, retrieving network host
entries from /etc/hosts or via DNS, converting CIDR network
addresses, perform Hesiod information lookups, retrieve network
entries from /etc/networks, implement TSIG transaction/request
security of DNS messages, perform name-to-address and
address-to-name translations, utilize /etc/resolv.conf
for resolver configuration

%package devel
Summary:	Header files for ISC's libbind
Requires:	%{name} = %{version}-%{release}

%description devel
libbind-devel provides header files and documentation for development with
ISC's libbind

%prep
%setup -q -n libbind-%{VERSION}

%patch0 -p1 -b .install
%patch1 -p1 -b .aarch64

%build
%configure --with-libtool --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT includedir=%{_includedir}/bind

# We don't want this...
rm -f $RPM_BUILD_ROOT/%{_libdir}/libbind.la
rm -rf $RPM_BUILD_ROOT/%{_mandir}/cat{3,5,7}

# libbind manpages has traditionally libbind_* prefix

# section 3
for all in getaddrinfo getipnodebyname gethostbyname getnameinfo getnetent \
	hesiod inet_cidr resolver tsig; do
	oldname=$RPM_BUILD_ROOT/%{_mandir}/man3/$all.3
	newname=$RPM_BUILD_ROOT/%{_mandir}/man3/libbind_$all.3
	cp -p $oldname $newname
	rm -f $oldname
done

# section 5
for all in irs.conf resolver; do
	oldname=$RPM_BUILD_ROOT/%{_mandir}/man5/$all.5
	newname=$RPM_BUILD_ROOT/%{_mandir}/man5/libbind_$all.5
	cp -p $oldname $newname
	rm -f $oldname
done

# section 7
for all in hostname; do
	oldname=$RPM_BUILD_ROOT/%{_mandir}/man7/$all.7
	newname=$RPM_BUILD_ROOT/%{_mandir}/man7/libbind_$all.7
	cp -p $oldname $newname
	rm -f $oldname
done

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libbind.pc

%ldconfig_scriptlets

%files
%doc CHANGES COPYRIGHT README
%{_libdir}/libbind.so.4
%{_libdir}/libbind.so.4.2.1

%files devel
%{_libdir}/libbind.so
%{_libdir}/pkgconfig/libbind.pc
%{_includedir}/bind
%{_mandir}/man3/libbind_*
%{_mandir}/man5/libbind_*
%{_mandir}/man7/libbind_*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 6.0-17
- Added gcc as an explicit BuildRequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Tomas Hozza <thozza@redhat.com> - 6.0-7
- add support for aarch64 (#925674)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Adam Tkac <atkac redhat com> 6.0-1
- update to final 6.0

* Mon Mar 09 2009 Adam Tkac <atkac redhat com> 6.0-0.4.rc1
- updated to 6.0rc1
- added pkg-config file

* Mon Mar 02 2009 Adam Tkac <atkac redhat com> 6.0-0.3.b1
- removed unneeded Obsoletes/Provides

* Thu Feb 19 2009 Adam Tkac <atkac redhat com> 6.0-0.2.b1
- package review related fixes

* Mon Feb 02 2009 Adam Tkac <atkac redhat com> 6.0-0.1.b1
- initial package
