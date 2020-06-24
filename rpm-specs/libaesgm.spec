Name:		libaesgm
Version:	20090429
Release:	22%{?dist}
License:	BSD
Summary:	Library implementation of AES (Rijndael) cryptographic methods
URL:		http://gladman.plushost.co.uk/oldsite/AES/index.php
Source0:	http://gladman.plushost.co.uk/oldsite/AES/aes-src-29-04-09.zip
Source1:	Makefile.aes
# Add fileencryption support
# http://www.gladman.me.uk/cryptography_technology/fileencrypt/
Patch0:		libaesgm-20090429-fileencrypt.patch

BuildRequires: gcc
BuildRequires: make

%description
Library implementation of AES (Rijndael) cryptographic methods.

%package devel
Summary:	Development files for libaesgm
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for libaesgm.

%prep
%setup -q -c -n %{name}-%{version}
cp %{SOURCE1} Makefile
%patch0 -p1 -b .fileencrypt
sed -i 's/\r//' *.txt

%build
make CFLAGS="%{optflags} -fPIC -DUSE_SHA1" LDFLAGS="%{build_ldflags}"

%install
make DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" install

%ldconfig_scriptlets

%files
%doc *.txt
%{_libdir}/libaesgm.so.*

%files devel
%{_includedir}/aes/
%{_libdir}/libaesgm.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar  5 2018 Tom Callaway <spot@fedoraproject.org> - 20090429-18
- fix typo in spec causing ldflags to be empty

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 20090429-17
- Use LDFLAGS from redhat-rpm-config
- Remove "%defattr(-,root,root,-)"
- Remove "Group:"
- Add BuildRequires for gcc, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20090429-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090429-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Tom "spot" Callaway <tcallawa@redhat.com> 20090429-3
- add fileencrypt support

* Mon Feb 22 2010 Tom "spot" Callaway <tcallawa@redhat.com> 20090429-2
- use sane versioning to ensure proper upgrade ordering without epoch
- fix Makefile.aes to not use double-zero in soname, don't make double zero symlink
- add default clean section
- put headers in /aes/ namespace dir

* Thu Feb 18 2010 Tom "spot" Callaway <tcallawa@redhat.com> 290409-1
- initial Fedora package
