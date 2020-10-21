Name:          tnftp
Version:       20151004
Release:       11%{?dist}
Summary:       FTP (File Transfer Protocol) client from NetBSD

License:       BSD and ISC
# From the README:
# `tnftp' is a `port' of the NetBSD FTP client to other systems.
# See http://www.NetBSD.org/ for more details about NetBSD.
URL:           http://www.NetBSD.org/
Source0:       ftp://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz

Patch0:        tnftp-20130505-libedit.patch

BuildRequires: libedit-devel
BuildRequires: openssl-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
%{name} is the FTP (File Transfer Protocol) client from NetBSD.  FTP is a widely
used protocol for transferring files over the Internet and for archiving files.
%{name} provides some advanced features beyond the Linux netkit ftp client, but
maintains a similar user interface to the traditional ftp client.  It was
formerly called lukemftp.

%prep
%setup -q

# use system libedit
%patch0 -p1 -b .libedit

%build

export CFLAGS="%{optflags}"
%configure --enable-editcomplete --enable-ipv6 --enable-ssl
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc ChangeLog COPYING NEWS README THANKS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 David Cantrell <dcantrell@redhat.com> - 20151004-1
- Upgrade to tnftp-20151004 (#1268664)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 David Cantrell <dcantrell@redhat.com> - 20141104-1
- Upgrade to tnftp-20141104 (#1160314)

* Fri Oct 31 2014 David Cantrell <dcantrell@redhat.com> - 20141031-1
- Upgrade to tnftp-20141031 to fix CVE-2014-8517 (#1158287)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130505-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 David Cantrell <dcantrell@redhat.com> - 20130505-7
- Link with system libedit rather than using internal one (#1079639)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130505-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130505-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 David Cantrell <dcantrell@redhat.com> - 20130505-4
- Add missing %%changelog lines and increment release number

* Thu May 30 2013 David Cantrell <dcantrell@redhat.com> - 20130505-3
- Remove the remaining unnecessary 'rm -rf %%{buildroot}'
- Include ChangeLog on the %%doc line
- Change License field to 'BSD and ISC'

* Wed May 29 2013 David Cantrell <dcantrell@redhat.com> - 20130505-2
- Remove unnecessary %%clean section
- Remove unnecessary %%defattr line in %%files section
- Use the %%{name} macro in the %%description and %%files sections
- Change URL to 'http://www.NetBSD.org/'

* Thu May 16 2013 David Cantrell <dcantrell@redhat.com> - 20130505-1
- Initial package
