Name:           pen
Version:        0.34.1
Release:        7%{?dist}
Summary:        Load balancer for "simple" tcp based protocols such as http or smtp
License:        GPLv2
URL:            http://siag.nu/pen/
Source0:        http://siag.nu/pub/pen/%{name}-%{version}.tar.gz
Source1:        pen.httpd
BuildRequires:  GeoIP-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc
Requires:       httpd

%description
pen is a load balancer for "simple" tcp based protocols such as http or
smtp. It allows several servers to appear as one to the outside and 
automatically detects servers that are down and distributes clients among the
available servers. This gives high availability and scalable performance. 

%prep
%setup -q

# Convert to utf-8
for file in ChangeLog penctl.1; do
   mv $file timestamp
   iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
   touch -r timestamp $file
done

sed -i 's/\/var/\%{_localstatedir}/g' %{SOURCE1}
chmod 0644 penstats

%build
%configure --with-ssl --with-geoip
%make_build

%install
%make_install
install -pDm0755 penctl.cgi %{buildroot}%{_localstatedir}/www/pen/penctl.cgi
install -pDm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/pen.conf

%files
%doc AUTHORS ChangeLog COPYING HOWTO penstats README TODO
%{_mandir}/man1/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/pen.conf
%{_localstatedir}/www/pen/
%exclude %{_prefix}/doc/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.34.1-3
- add gcc into buildrequires

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild


* Mon Feb 05 2018 Daniel Lara <danniel@fedoraproject.org> - 0.34.1-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.34.0-1
- new version

* Fri Oct 21 2016 Daniel Lara <danniel@fedoraproject.org> - 0.33.2-1
- new version

* Fri Jul 15 2016 Daniel Lara <danniel@fedoraproject.org> - 0.33.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.29.0-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Christopher Meng <rpm@cicku.me> - 0.25.1-1
- Update to 0.25.1

* Wed Jun 18 2014 Christopher Meng <rpm@cicku.me> - 0.23.0-1
- Update to 0.23.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Christopher Meng <rpm@cicku.me> - 0.22.1-1
- Update to 0.22.1
- Patch merged upstream.

* Wed Apr 02 2014 Christopher Meng <rpm@cicku.me> - 0.22.0-2
- Patch messed with syntax.

* Tue Apr 01 2014 Christopher Meng <rpm@cicku.me> - 0.22.0-1
- Update to 0.22.0
- Built with GeoIP support.

* Mon Jan 27 2014 Christopher Meng <rpm@cicku.me> - 0.20.2-1
- Update to 0.20.2, SPEC cleanup.
- Built with OpenSSL support.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Remi Collet <rcollet@redhat.com> - 0.18.0-9
- fix configuration for httpd 2.4, #871450

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 0.18.0-3
- replace $RPM_BUILD_DIR with %%{_builddir}

* Wed Nov 12 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 0.18.0-2
- preserve timestamp when converting files to UTF-8

* Sun Nov 09 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 0.18.0-1
- Initial Release
