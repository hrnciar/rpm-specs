%global realname eleveldb
%global upstream basho


Name:		erlang-%{realname}
Version:	2.0.35
Epoch:		1
Release:	8%{?dist}
Summary:	Erlang LevelDB API
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
#Source1:	https://github.com/basho/leveldb/archive/%{version}/basho-leveldb-%{version}.tar.gz
Source1:	https://github.com/basho/leveldb/archive/%{version}/basho-leveldb-2.0.34.tar.gz
# Fedora/EPEL-specific
Patch1:		erlang-eleveldb-0001-Use-system-wide-snappy.patch
Patch2:		erlang-eleveldb-0002-Fix-deprecation-warning-while-building-with-Erlang-1.patch
Patch5:		erlang-eleveldb-0005-Don-t-treat-warnings-as-errors.patch
# switch to <atomic> from non-standard <cstdatomic>
# https://github.com/basho/leveldb/pull/194
Patch101:	basho-leveldb-0001-Switch-from-cstdatomic-to-atomic.patch
# https://github.com/basho/leveldb/pull/220
Patch102:	basho-leveldb-0002-correct-code-in-the-32bit-path-to-correctly-compile.patch
Patch103:	basho-leveldb-0003-Fix-least-byte-extraction.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-rebar
BuildRequires:	erlang-os_mon
#BuildRequires:	leveldb-devel
# Requires for using ps utility in tests
BuildRequires:	procps-ng
BuildRequires:	snappy-devel
# Remove when https://bugzilla.redhat.com/show_bug.cgi?id=1770256 is resolved
ExcludeArch: s390x


%description
Erlang LevelDB API.


%prep
%setup -q -n %{realname}-%{version}
rm -f c_src/build_deps.sh
rm -f c_src/snappy-1.0.4.tar.gz
%patch1 -p1 -b .use_systemwide
%patch2 -p1 -b .fix_deprecation_warnings
%patch5 -p1 -b .no_warns_as_errors
tar xvf %{SOURCE1}
#cd leveldb-%{version}
cd leveldb-2.0.34
%patch101 -p1 -b .atomic
%patch102 -p1 -b .32_bit
%patch103 -p1 -b .fix_extraction
cd -


%build
# Building Basho's leveldb fork first
#cd leveldb-%{version}
cd leveldb-2.0.34
OPT="%{optflags}" make
cd -

%{erlang_compile}


%install
%{erlang_install}

install -p -m 0644 priv/eleveldb.schema %{buildroot}%{erlang_appdir}/priv
install -p -m 0644 priv/eleveldb_multi.schema %{buildroot}%{erlang_appdir}/priv


%check
%{erlang_test}


%files
%doc README.md
%{erlang_appdir}/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.35-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.35-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 1:2.0.35-5
- Rebuild for Erlang 22

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.35-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Peter Lemenkov <lemenkov@gmail.com> - 1:2.0.35-3
- Rebuild for Erlang 21

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 16 2018 Peter Lemenkov <lemenkov@gmail.com> - 1:2.0.35-1
- Ver. 2.0.35

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Peter Lemenkov <lemenkov@gmail.com> - 1:2.0.34-7
- Rebuild for Erlang 20 (with proper builddeps)

* Fri Feb 23 2018 Peter Lemenkov <lemenkov@gmail.com> - 1:2.0.34-6
- Rebuild for Erlang 20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 1:2.0.34-4
- Fix building on 32-bit arches

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.34-1
- Ver. 2.0.34
- Upstream abandoned 2.2.x branch and switched to 2.0.x

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 16 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.19-4
- Fix FTBFS with Erlang 19

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.2.19-3
- Rebuild for Erlang 19

* Fri Jun 03 2016 Dan Horák <dan[at]danny.cz> - 2.2.19-2
- Fix build on secondary arches (#1340829)

* Sat May 21 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.19-1
- Ver. 2.2.19

* Sat May 14 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.18-2
- Install schemas

* Wed May 11 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.18-1
- Ver. 2.2.18

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.17-2
- Drop unneeded macro

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.2.17-1
- Ver. 2.2.17
- Use Basho's leveldb fork

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-11
- Rebuild with Erlang 18.3

* Fri Feb 12 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-10
- Fixed FTBFS in Rawhide

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-7
- Rebuild with Erlang 17.3.3

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-6
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Ville Skyttä <ville.skytta@iki.fi> - 1.3.2-4
- Use new erlang macros to build with $RPM_OPT/LD_FLAGS etc, verbosely
- Disable cache leak test on F-20, F-21, and F-22 (#1107767, #1106223)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-1
- Ver. 1.3.2

* Tue Apr 02 2013 Dan Horák <dan[at]danny.cz> - 1.3.0-2
- fix build on s390

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.2-1
- Ver. 1.2.2

* Wed Jul 18 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-2
- Remove EL5-specific stuff from spec-file
- Enable tests

* Thu May 17 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.1.0-1
- Ver. 1.1.0

* Fri Sep 16 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.0.0-1
- Ver. 1.0.0
