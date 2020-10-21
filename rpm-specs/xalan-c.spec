Name:           xalan-c
Version:        1.11.0
Release:        19%{?dist}
Summary:        Xalan XSLT processor for C

License:        ASL 2.0
URL:            http://xml.apache.org/xalan-c/
Source0:        http://www.us.apache.org/dist/xalan/xalan-c/sources/xalan_c-1.11-src.tar.gz
Patch0:         xalan-c-1.10.0-escaping.patch

BuildRequires:  gcc-c++
BuildRequires:  xerces-c-devel

%description
Xalan is an XSLT processor for transforming XML documents into HTML, text, or
other XML document types.


%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%package doc
Summary:        Documentation for Xalan XSLT processor for C

%description doc
Documentation for %{name}.


%prep
%setup -q -n xalan-c-1.11/c
%patch0 -p2 -b .escaping
find -type d -name CVS -print0 | xargs -0 rm -rf
chmod 644 NOTICE

# Update config.guess for new architectures
cp /usr/lib/rpm/config.guess config.guess

%build
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
COMMONARGS="-plinux -cgcc -xg++ -minmem"
%ifarch alpha %{power64} s390x sparc64 x86_64 aarch64
./runConfigure ${COMMONARGS} -b64 -P %{_prefix} -C --libdir="%{_libdir}" -z '%{optflags}'
%else
./runConfigure ${COMMONARGS} -b32 -P %{_prefix} -C --libdir="%{_libdir}" -z '%{optflags}'
%endif
# _smp_mflags do not work
make


%install
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
make install DESTDIR=%{buildroot}


%ldconfig_scriptlets


%files
%doc LICENSE KEYS NOTICE
%{_bindir}/Xalan
%{_libdir}/libxalan*.so.*


%files devel
%{_libdir}/libxalan*.so
%{_includedir}/xalanc/


%files doc
%doc readme.html xdocs samples


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.11.0-8
- Use power64 macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.11.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.11.0-3
- Fix build on aarch64

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 1.11.0-2
- Bulk sad and useless attempt at consistent SPEC file formatting

* Tue Oct 08 2013 Nick Le Mouton <nick@noodles.net.nz> - 1.11.0-1
- Rebuilt for xalan-c 1.11, fixes a few problems with using newer xerces-c

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-11
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Kalev Lember <kalev@smartlink.ee> - 1.10.0-9
- Rebuilt with xerces-c 3.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 05 2010 Lubomir Rintel <lkundrak@v3.sk> - 1.10.0-7
- Rebuild for newer xerces-c

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.10.0-4
- Rebuild for newer xerces-c

* Thu Jan 03 2008 Lubomir Kundrak <lkundrak@redhat.com> 1.10.0-3
- Adding missing includes to fix build with gcc-4.3

* Mon Nov 19 2007 Lubomir Kundrak <lkundrak@redhat.com> - 1.10.0-2
- Fix passing of compiler flags
- Bump to stable source instead of CVS snapshot
- Fixed License tag

* Thu Feb 15 2007 Till Maas <opensource till name> - 1.10.0-1
- Initial spec for fedora extras
