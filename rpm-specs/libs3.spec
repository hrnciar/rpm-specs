%global commit 287e4bee6fd430ffb52604049de80a27a77ff6b4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		libs3
Version:	4.1
Release:	0.7.20190408git%{shortcommit}%{?dist}
Summary:	C Library and Tools for Amazon S3 Access

License:	LGPLv3+ or GPLv2+
URL:		https://github.com/bji/libs3
Source0:	https://github.com/bji/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:	gcc
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel

%description
This package includes the libs3 shared object library, needed to run
applications compiled against libs3, and additionally contains the s3
utility for accessing Amazon S3.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{commit}

sed -e 's!^CFLAGS +=!& %{optflags}!' \
    -e 's!^LDFLAGS =!& %{?__global_ldflags}!' \
    -e 's!$(INSTALL) -Dps!$(INSTALL) -Dp!' \
    -i GNUmakefile

%build
make %{?_smp_mflags} exported VERBOSE=1

%install
make %{?_smp_mflags} install VERBOSE=1 \
     DESTDIR=%{buildroot}%{_prefix} LIBDIR=%{buildroot}%{_libdir}
rm %{buildroot}%{_libdir}/libs3.a
chmod 755 %{buildroot}%{_libdir}/libs3.so.4.1

%check
make %{?_smp_mflags} test VERBOSE=1

%ldconfig_scriptlets

%files
%{_bindir}/s3
%{_libdir}/libs3.so.*
%license COPYING-LGPLv3 COPYING-GPLv2 LICENSE

%files devel
%{_includedir}/libs3.h
%{_libdir}/libs3.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.7.20190408git287e4be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.6.20190408git287e4be
- New github snapshot

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.5.20181203git111dc30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-0.4.20181203git111dc30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.3.20181203git111dc30
- New github snapshot
- Drop patch libs3-curl-7.62.patch (merged upstream)
- Update License tag

* Thu Nov 22 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.2.20180821gita4d873f
- Support curl >= 7.62

* Fri Aug 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.1-0.1.20180821gita4d873f
- New github snapshot

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.0-0.6.20170206git208bcba
- Add BuildRequires on gcc
- Packaging updates
  - Remove Group and BuildRoot tags
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Install license in licensedir
  - Use new ldconfig scriptlets macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.5.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.4.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.3.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.2.20170206git208bcba
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.0-0.1.20170206git208bcba
- New github snapshot

* Thu Dec 01 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.5.20161104gita052a00
- New github snapshot
- Drop fix for old nice lib on EPEL 5 (fixed upstream)

* Fri May 20 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.4.20160322git0759f1d
- New github snapshot
- Drop patch libs3-format.patch (accepted upstream)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.20150902git247ba1b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.2.20150902git247ba1b
- Fix compilation on 32 bit archs

* Wed Sep 09 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.1.20150902git247ba1b
- Initial package
