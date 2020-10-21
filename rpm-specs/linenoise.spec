
%global git_rev 7946e2c

Name:           linenoise
Version:        0
Release:        17.git%{git_rev}%{?dist}
Summary:        Minimal replacement for readline
# The licenses are a bit of a mess here...
# utf8.{c,h} contain incomplete license headers. They refer to a "LICENSE" file 
# which is actually from jimtcl. A copy is committed in dist-git as 
# jimtcl-LICENSE, retrieved from 
# <https://raw.github.com/msteveb/jimtcl/master/LICENSE>. I received a mail 
# from the author, committed as steve-bennett-license-confirmation, confirming 
# that that is indeed the LICENSE file referred to and therefore utf8.{c,h} are 
# under a BSD-like license.
# linenoise.{c,h} contain complete BSD-like license headers so they are fine. 
# And it means the whole library is definitely under a BSD-like license.
# But there is no separate license file shipped in the tarball. I queried Tad 
# Marshall on 2013-01-10 to include one but never received a reply. So 
# I synthesized one as Source1.
License:        BSD
URL:            https://github.com/tadmarshall/linenoise
Source0:        https://github.com/tadmarshall/linenoise/tarball/%{git_rev}/%{name}-%{git_rev}.tar.gz
Source1:        COPYING
Patch0:         %{name}-build-shared-lib.patch
Patch1:         %{name}-symbol-visibility.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description
Linenoise is a replacement for the readline line-editing library with the goal 
of being smaller.

%description devel
This package contains files needed for developing software that uses
%{name}.

%prep
%setup -q -n tadmarshall-%{name}-%{git_rev}
cp %{SOURCE1} COPYING
%patch0 -p1
%patch1 -p1

%build
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
LIBDIR="%{_libdir}" INCLUDEDIR="%{_includedir}" CFLAGS="%{optflags}" make %{?_smp_mflags} DESTDIR="%{buildroot}" install

%files
%doc README.markdown COPYING
%{_libdir}/liblinenoise.so.*

%files devel
%{_includedir}/linenoise.h
%{_libdir}/liblinenoise.so

%ldconfig_scriptlets

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.git7946e2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Dan Callaghan <dcallagh@redhat.com> - 0-2.git7946e2c
- added licensing clarifications

* Tue Jan 08 2013 Dan Callaghan <dcallagh@redhat.com> - 0-1.git7946e2c
- initial version
