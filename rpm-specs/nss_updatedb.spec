Name:		nss_updatedb
Version:	10
Release:	19%{?dist}
Summary:	Maintains a local cache of network directory user and group information

License:	GPL+
URL:		http://www.padl.com/OSS/%{name}.html
Source0:	http://www.padl.com/download/%{name}.tgz

#BuildRequires:	db4-devel
BuildRequires:  gcc
BuildRequires: libdb-devel

%description
The nss_updatedb utility maintains a local cache of network directory user
and group information. Used in conjunction with the pam_ccreds module, 
it provides a mechanism for disconnected use of network directories.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -ldb"

%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}/
install -p %{name} $RPM_BUILD_ROOT/%{_sbindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%name-%{version}



%files
%doc ChangeLog README COPYING AUTHORS
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*gz


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild


* Thu Aug 02 2012 Kashyap Chamarthy <kashyapc@fedoraproject.org> 10-5
- Updated BuildRequires to use libdb-devel instead of now obsolete db4-devel

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Wed Sep 23 2009 Kashyap Chamarthy <kashyapc@fedoraproject.org> 10-2
- Changed license to GPL+ and other change as specified in
  bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=524437

* Sun Sep 20 2009 Kashyap Chamarthy <kashyapc@fedoraproject.org> 10-1
- initial spec file
