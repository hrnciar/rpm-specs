#
# RPM Spec file for the PMDA++ project.
#

# Note, the following _pmdasdir definition should (does) match the one defined
# in the PCP project's build/rpm/fedora.spec file.
%global _pmdasdir %{_localstatedir}/lib/pcp/pmdas

Summary: PMDA++ Library
Name: pcp-pmda-cpp
Version: 0.4.4
Release: 8%{?dist}
License: Boost
URL: https://github.com/pcolby/%{name}
Source: https://github.com/pcolby/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: pcp4.patch

BuildRequires:  gcc-c++
BuildRequires: boost-devel >= 1.32
BuildRequires: cmake >= 2.6
BuildRequires: gtest-devel
BuildRequires: pcp pcp-libs-devel

%description
PMDA++ is a header-only library that allows developers to write Performance
Metrics Domain Agents (PMDAs) for Performance Co-Pilot (PCP) in C++.

%prep
%setup -c -q
%patch0 -p1

%build
%{cmake} %{name}-%{version}
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}

%check
%{__make} check

%package devel
Summary: Development headers for the PMDA++ library
Provides: %{name}-static = %{version}-%{release}
Requires: pcp-libs-devel%{?_isa}

%description devel
PMDA++ is a header-only library that allows developers to write Performance
Metrics Domain Agents (PMDAs) for Performance Co-Pilot (PCP) in C++.

%package examples
Summary: Examples for the PMDA++ library
Requires: pcp

%description examples
Examples from the PMDA++ project.

%files devel
%doc %{name}-%{version}/CHANGELOG.md
%doc %{name}-%{version}/README.md
%{_includedir}/pcp-cpp
%{license} %{name}-%{version}/LICENSE.md

%files examples
%{_pmdasdir}/%{name}-examples

%changelog
* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.4.4-8
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.4.4-4
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Lukas Berk <lberk@redhat.com> 0.4.4-2
- updated for pcp-4.0.0 and related api changes

* Sat Oct 14 2017 Paul Colby <git@colby.id.au> - 0.4.4-1
- updated to pcp-pmda-cpp 0.4.4.

* Tue Jul 12 2016 Paul Colby <git@colby.id.au> - 0.4.3-1
- updated to pcp-pmda-cpp 0.4.3.

* Sat Mar 14 2015 Paul Colby <git@colby.id.au> - 0.4.2-1
- updated to pcp-pmda-cpp 0.4.2.

* Sat Sep 06 2014 Paul Colby <git@colby.id.au> - 0.4.1-1
- updated to pcp-pmda-cpp 0.4.1.

* Thu May 15 2014 Paul Colby <git@colby.id.au> - 0.4.0-1
- updated to pcp-pmda-cpp 0.4.0.

* Sat May 10 2014 Paul Colby <git@colby.id.au> - 0.3.4-1
- updated to pcp-pmda-cpp 0.3.4.

* Tue Feb 18 2014 Paul Colby <git@colby.id.au> - 0.3.3-1
- updated to pcp-pmda-cpp 0.3.3.

* Sun Feb 16 2014 Paul Colby <git@colby.id.au> - 0.3.2-1
- updated to pcp-pmda-cpp 0.3.2.

* Fri Feb 14 2014 Paul Colby <git@colby.id.au> - 0.3.1-1
- initial pcp-pmda-cpp spec file.
