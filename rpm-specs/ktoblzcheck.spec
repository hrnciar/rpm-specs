Name: ktoblzcheck
Summary: A library to check account numbers and bank codes of German banks
Version: 1.49
Release: 3%{?dist}
Source: http://download.sourceforge.net/ktoblzcheck/%{name}-%{version}.tar.gz
License: LGPLv2+
URL: http://ktoblzcheck.sourceforge.net
BuildRequires:  gcc-c++
BuildRequires: perl-generators

%description 
KtoBLZCheck is a library to check account numbers and bank codes of
German banks. Both a library for other programs as well as a short
command-line tool is available. It is possible to check pairs of
account numbers and bank codes (BLZ) of German banks, and to map bank
codes (BLZ) to the clear-text name and location of the bank.

%package devel
Summary: Ktoblzcheck developer files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development files for the account number
checking library ktoblzcheck.

%prep
%setup -q
for file in NEWS ChangeLog ; do
	iconv -f iso8859-1 -t utf-8 $file -o $file.new
	touch -r $file $file.new
	mv -f $file.new $file
done

%build
%{configure} --disable-python
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README AUTHORS COPYING NEWS ChangeLog
%{_libdir}/*.so.*
%{_bindir}/ktoblzcheck
%{_datadir}/ktoblzcheck/*
%{_mandir}/man1/ktoblzcheck.1*

%files devel
%{_includedir}/iban.h
%{_includedir}/ktoblzcheck.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/ktoblzcheck.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Bill Nottingham <notting@splat.cc> - 1.49-1
- fix build, update to current (#1675240)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.44-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 31 2014 Bill Nottingham <notting@redhat.com> - 1.44-1
- update to 1.44

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.41-2
- Perl 5.18 rebuild

* Wed Apr 24 2013 Bill Nottingham <notting@redhat.com> - 1.41-1
- update to 1.41

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bill Nottingham <notting@redhat.com> - 1.37-1
- initial packaging
