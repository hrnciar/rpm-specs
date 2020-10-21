###  for Fedora  ###

Name:     sylfilter
Summary:  A generic message filter library and command-line tools
Version:  0.8
Release:  19%{?dist}
License:  BSD
URL:      http://sylpheed.sraoss.jp/sylfilter/
Source0:  http://sylpheed.sraoss.jp/sylfilter/src/sylfilter-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: sqlite-devel
BuildRequires: glib2-devel
BuildRequires: sylpheed-devel

%package devel
Summary: Development files for sylfilter
Requires: sylfilter%{?_isa} = %{version}-%{release}
Requires: sqlite-devel
Requires: glib2-devel

%description
This is SylFilter, a generic message filter library, and some command-line tools
that provide a Bayesian filter which is very popular as a spam filtering
algorithm.

SylFilter is also internationalized and can be applied to any languages.

The SylFilter library provides simple but powerful C APIs and can be used from
C programs. 

SylFilter can be used as a command-line tool inside a junk filter mail program
similar to major tools such as bogofilter and bsfilter etc.

For further details, see http://sylpheed.sraoss.jp/sylfilter/

%description devel
Development files for sylfilter

%prep
%setup -q

%build
%configure --disable-rpath --with-libsylph=sylpheed --with-libsylph-dir=/usr --disable-static
%{make_build}

%install
%{make_install}
rm %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README
%{_bindir}/sylfilter
%{_libdir}/libsylfilter.*
%{_libdir}/libsylfilter.so.*
%license COPYING

%files devel
%{_libdir}/libsylfilter.so
%{_includedir}/sylfilter

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 25 2016 Ranjan Maitra 0.8-10
- corrections to changelog

* Fri Mar 25 2016 Ranjan Maitra 0.8-9
- removes *la files after installation
- cleans up spec changelog

* Tue Mar 22 2016 Ranjan Maitra 0.8-8
- removes %%description to after Requires

* Tue Mar 22 2016 Ranjan Maitra 0.8-7
- removes .so from the main subpackage.

* Thu Jan 7 2016 Ranjan Maitra 0.8-6
- removes requirement of sylpheed

* Thu Jan 7 2016 Ranjan Maitra 0.8-5
- fixes stylistic suggestions 

* Fri Dec 11 2015 Ranjan Maitra 0.8-4
- initial rebuild for Fedora (to include the devel file)

* Wed Dec 02 2015 Ranjan Maitra 0.8-3
- initial rebuild for Fedora
- makes dependent on sylpheed

* Tue Dec 01 2015 Ranjan Maitra 0.8-2
- initial rebuild for Fedora to take care of comments 

* Tue Sep 22 2015 Ranjan Maitra 0.8-1
- initial build for Fedora
