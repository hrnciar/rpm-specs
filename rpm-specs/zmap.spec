%bcond_with     pfring
%bcond_without  hiredis
%bcond_with     mongodb
%bcond_without  debug

Name:           zmap
Version:        2.1.1
Release:        13%{?dist}
Summary:        Network scanner for Internet-wide network studies
License:        ASL 2.0
URL:            https://zmap.io
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  byacc
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gengetopt
BuildRequires:  gmp-devel
%if %{with hiredis}
BuildRequires:  hiredis-devel
%endif
BuildRequires:  json-c-devel
BuildRequires:  libpcap-devel
%if %{with mongodb}
BuildRequires:  pkgconfig(libmongoc-1.0)
%endif

%description
ZMap is an open-source network scanner that enables researchers to easily 
perform Internet-wide network studies. With a single machine and a well 
provisioned network uplink, ZMap is capable of performing a complete scan of 
the IPv4 address space in under 45 minutes, approaching the theoretical limit
of gigabit Ethernet.

ZMap can be used to study protocol adoption over time, monitor service 
availability, and help us better understand large systems distributed across 
the Internet.

========== WARNING ==========
While ZMap is a powerful tool for researchers, please keep in mind that by 
running ZMap, you are potentially scanning the ENTIRE IPv4 address space and 
some users may not appreciate your scanning. We encourage ZMap users to 
respect requests to stop scanning and to exclude these networks from ongoing 
scanning.

%prep
%setup -q
# RHEL6 ld is too old.
%{?el6:sed -i 's|-z relro -z now||g' CMakeLists.txt}
# EL7 has 2.8.11
%{?el7:sed -i -e 's|2.8.12|2.8.11|' CMakeLists.txt}

# https://github.com/zmap/zmap/pull/332
sed -i 's|${CMAKE_C_FLAGS} ${GCCWARNINGS}|${GCCWARNINGS} ${CMAKE_C_FLAGS}|g;s|${CMAKE_EXE_LINKER_FLAGS} ${LDHARDENING}|${LDHARDENING} ${CMAKE_EXE_LINKER_FLAGS}|g' CMakeLists.txt

%build
%cmake -DWITH_JSON=ON     \
%if %{with mongodb}
       -DWITH_MONGO=ON    \
%endif
%if %{with hiredis}
       -DWITH_REDIS=ON    \
%endif
       -DWITH_PFRING=OFF  \
       .

make %{?_smp_mflags}

chmod 644 -v examples/udp-probes/*
find ./examples/ -type f -exec sed -i 's/\r$//' {} \+

%install
%make_install

%files
%doc AUTHORS CHANGELOG.md README.md examples/
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/zmap
%{_sbindir}/zblacklist
%{_sbindir}/ztee
%{_mandir}/man1/zmap.1*
%{_mandir}/man1/zblacklist.1*
%{_mandir}/man1/ztee.1*

%changelog
* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.1.1-13
- Rebuild (json-c)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 2.1.1-9
- Append curdir to CMake invokation. (#1668512)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.1.1-7
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.1.1-5
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 02 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1
- Clean the spec a little bit

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-2
- rebuild (hiredis)

* Thu Sep 03 2015 Christopher Meng <rpm@cicku.me> - 2.1.0-1
- Update to 2.1.0

* Sun Feb 22 2015 Christopher Meng <rpm@cicku.me> - 1.2.1-3
- Rebuilt for hiredis 0.12.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Christopher Meng <rpm@cicku.me> - 1.2.1-1
- Update to 1.2.1

* Wed Mar 12 2014 Christopher Meng <rpm@cicku.me> - 1.2.0-1
- Update to 1.2.0

* Mon Jan 27 2014 Christopher Meng <rpm@cicku.me> - 1.1.2-1
- Update to 1.1.2

* Thu Dec 19 2013 Christopher Meng <rpm@cicku.me> - 1.1.1-1
- Update to 1.1.1

* Fri Nov 22 2013 Christopher Meng <rpm@cicku.me> - 1.1.0-2
- Set 644 to examples.
- Fix wrong line endings.

* Tue Nov 19 2013 Christopher Meng <rpm@cicku.me> - 1.1.0-1
- Update to 1.1.0
- Enable harden building.

* Mon Aug 26 2013 Christopher Meng <rpm@cicku.me> - 1.0.3-2
- Correct the license and summary.

* Mon Aug 19 2013 Christopher Meng <rpm@cicku.me> - 1.0.3-1
- Initial Package.
