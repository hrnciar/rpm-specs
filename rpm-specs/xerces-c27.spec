Summary:  Validating XML Parser
Name:     xerces-c27
Version:  2.7.0
Release:  31%{?dist}
License:  ASL 2.0
URL:      http://xml.apache.org/xerces-c/
Source0:  http://archive.apache.org/dist/xml/xerces-c/Xerces-C_2_7_0/source/xerces-c-src_2_7_0.tar.gz
Patch0:   xerces-c--CVE-2009-1885.diff
# Backports for CVE-2016-4463
# http://xerces.apache.org/xerces-c/secadv/CVE-2016-4463.txt
# http://svn.apache.org/viewvc?view=revision&revision=1747619
Patch1:   xerces-c27-cve-2016-4463.patch
# http://svn.apache.org/viewvc?view=revision&revision=1747620
Patch2:   xerces-c27-cve-2016-4463-mitigation.patch
# Backport for CVE-2017-12627
# https://xerces.apache.org/xerces-c/secadv/CVE-2017-12627.txt
# http://svn.apache.org/viewvc?view=revision&revision=1819998
Patch3:   xerces-c27-cve-2017-12627.patch

BuildRequires:  gcc-c++
BuildRequires:  sed

%description
Xerces-C is a validating XML parser written in a portable subset of C++.
Xerces-C makes it easy to give your application the ability to read and write
XML data. A shared library is provided for parsing, generating, manipulating,
and validating XML documents. Xerces-C is faithful to the XML 1.0
recommendation and associated standards ( DOM 1.0, DOM 2.0. SAX 1.0, SAX 2.0,
Namespaces).

Note that this package contains Xerces-C++ 2.7.0 for compatibility with
applications that cannot use a newer version.


%package  devel
Summary:  Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for xerces-c 2.7.0. If you like to develop programs using
xerces-c 2.7.0, you will need to install %{name}-devel.

%package doc
Summary:  Documentation for Xerces-C++ validating XML parser

%description doc
Documentation for Xerces-C++ 2.7.0.

Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.


%prep
%setup -q -n xerces-c-src_2_7_0

rm -rf doc/html/resources/.svn
find ./doc -type f -perm 755 -exec chmod 644 {} \;
find ./samples -type f -perm 755 -exec chmod 644 {} \;
sed -i -e "s|\(PREFIX.\)/lib\b|\1/%{_lib}|g" src/xercesc/configure */Makefile.in

iconv -f iso8859-1 -t utf-8 credits.txt > credits.txt.conv && mv -f credits.txt.conv credits.txt;
for i in feedback.xml migration.xml releases_archive.xml; do {
  iconv -f iso8859-1 -t utf-8 doc/$i > doc/$i.conv && mv -f doc/$i.conv doc/$i;
  };
done;

%patch0 -p0 -b .CVE-2009-1885
%patch1 -p1 -b .cve-2016-4463
%patch2 -p1 -b .cve-2016-4463-mitig
%patch3 -p1 -b .cve-2017-12627


%build
export XERCESCROOT="$PWD"

# Update the various config.guess to upstream release for aarch64/ppc64le support (and other new arches)
find ./ -name config.guess -exec cp /usr/lib/rpm/config.guess {} ';'

# Let Makefiles be verbose
find -name 'Makefile.*' | while read f; do
  sed -i -e 's/$Q//g' \
  -e 's/{MAKE} -s/(MAKE)/g' \
  -e '/echo \"  (/d' \
  $f
done

# Remove conflicting flags from runConfigure
find -name runConfigure | while read f; do
  sed -i -e 's/-w -O -DNDEBUG/-DNDEBUG/g' $f
done

cd $XERCESCROOT/src/xercesc
CXXFLAGS="${RPM_OPT_FLAGS}" CFLAGS="${RPM_OPT_FLAGS}" ./runConfigure -plinux -cgcc -xg++ -minmem -nsocket -tnative -rpthreads -b%{__isa_bits} -P %{_prefix} -C --libdir="%{_libdir}"
# not smp safe
make V=1


%install
export XERCESCROOT="$PWD"
make install -C src/xercesc DESTDIR="$RPM_BUILD_ROOT"
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xerces-c-2.7.0
cd $RPM_BUILD_ROOT%{_libdir}/xerces-c-2.7.0/
ln -s ../libxerces-c.so.27 libxerces-c.so
ln -s ../libxerces-depdom.so.27 libxerces-depdom.so
cd -
rm $RPM_BUILD_ROOT%{_libdir}/libxerces*.so
mkdir -p $RPM_BUILD_ROOT%{_includedir}/xercesc-2.7.0
mv $RPM_BUILD_ROOT%{_includedir}/xercesc $RPM_BUILD_ROOT%{_includedir}/xercesc-2.7.0


%ldconfig_scriptlets


%files
%license LICENSE LICENSE.txt
%{_libdir}/libxerces*.so.*


%files devel
%dir %{_libdir}/xerces-c-2.7.0
%{_libdir}/xerces-c-2.7.0/libxerces*.so
%{_includedir}/xercesc-2.7.0/


%files doc
%license LICENSE LICENSE.txt
%doc Readme.html NOTICE STATUS credits.txt doc samples


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 08 2018 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-28
- Clean up spec.
- Add patch for CVE-2016-4463 (RHBZ#1351469).
- Add patch for CVE-2017-12627 (RHBZ#1551526).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.7.0-23
- Use sed instead of perl in spec (F26FTBFS, RHBZ#1424554).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.7.0-20
- Use __isa_bits macro instead of list of 64-bit architectures - rhbz#1256754

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.7.0-18
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.7.0-15
- Update all config.guess/sub for aarch64 (and ppc64le)
- Cleanup SPEC

* Thu May 22 2014 Brent Baude <baude@us.ibm.com> - 2.7.0-14
- Changed ppc64 arch to power64 macro
- Added xerces-c-add-ppc64le.patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  6 2009 Peter Lemenkov <lemenkov@gmail.com> 2.7.0-8
- Fix CVE-2009-1885

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 04 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-5
- Fix Source: url.

* Wed Feb 27 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-4
- Better descriptions.

* Tue Feb 26 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-3
- Fix some non-utf8 files.
- Fix files and dirs permissions.
- Properly own dir.

* Tue Feb 26 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-2
- Better files relocation.

* Mon Feb 18 2008 Xavier Bachelot <xavier@bachelot.org> - 2.7.0-1
- Initial build.
- Spec file forked from original xerces-c package.
