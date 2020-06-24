Name:           libss7
Version:        2.0.0
Release:        2%{?dist}
Summary:        SS7 protocol services to applications


License:        GPLv2

URL:            http://www.asterisk.org/
Source0:        http://downloads.digium.com/pub/telephony/libss7/releases/libss7-%{version}.tar.gz


BuildRequires:  gcc
%description
libss7 is a userspace library that is used for providing SS7 protocol
services to applications.  It has a working MTP2, MTP3, and ISUP for
ITU and ANSI style SS7, however it was written in a manner that will
easily allow support for other various national specific variants in
the future.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup0 -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_PREFIX=$RPM_BUILD_ROOT libdir=%{_libdir}
#ln -s libss7.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libss7.so.1
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc ChangeLog NEWS* README LICENSE
%{_libdir}/*.so.*

%files devel
%doc README LICENSE
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.2-1
- Update to 1.0.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-3
- Don't forget to add spec file.

* Tue Oct  7 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-2
- Add LICENSE to docs

* Tue Aug  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-1
- Update to 1.0.1

* Tue Jul 29 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.0-1
- First version for Fedora
