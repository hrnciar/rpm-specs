# Run valgrind test
# valgrind is available only on selected arches
%ifarch %{valgrind_arches}
%bcond_without csnappy_enables_valgrind
%else
%bcond_with csnappy_enables_valgrind
%endif

%global commit cbd205bfec1d2adfbe8a3b3b120b7a3556f982d1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       csnappy 
Version:    0
Release:    18.20191203git%{shortcommit}%{?dist}
Summary:    Snappy compression library ported to C 
License:    BSD
URL:        https://github.com/zeevt/%{name}
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# Tests:
%if %{with csnappy_enables_valgrind}
BuildRequires:  coreutils
BuildRequires:  diffutils
BuildRequires:  valgrind
%endif

%description
This is an ANSI C port of Google's Snappy library. Snappy is a compression
library designed for speed rather than compression ratios.

%package devel
Summary:    Development files for the %{name} library
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use the %{name} library.


%prep
%setup -qn %{name}-%{commit}

# Extract BSD license and copyright notices, bug #1152057
! test -e LICENSE
for F in $(< Makefile sed -e '/libcsnappy.so:/ s/.*:// p' -e 'd'); do
    < $F sed -e '/Copyright/,/\*\//p' -e 'd'
done > LICENSE
test -s LICENSE

%build
%{make_build} 'OPT_FLAGS=%{optflags}' 'LDFLAGS=%{?__global_ldflags}' \
    lib%{name}.so cl_tester

%if %{with csnappy_enables_valgrind}
%check
make %{?_smp_mflags} 'OPT_FLAGS=%{optflags}' 'LDFLAGS=%{?__global_ldflags}' lib%{name}.so test
%endif

%install
%{make_install} 'DESTDIR=%{buildroot}' 'LIBDIR=%{_libdir}'

%files
%license LICENSE
%doc README TODO
# No soname <https://github.com/zeevt/csnappy/issues/33>
%{_libdir}/lib%{name}.so

%files devel
%{_includedir}/%{name}.h


%changelog
* Tue Feb 04 2020 Petr Pisar <ppisar@redhat.com> - 0-18.20191203gitcbd205b
- Rebased to cbd205bfec1d2adfbe8a3b3b120b7a3556f982d1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20181121git973f62f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Petr Pisar <ppisar@redhat.com> - 0-16.20181121git973f62f
- Rebased to 973f62f7eede7412e04be230adcb52e78dd25079

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20181121gitb476930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20181121gitb476930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Petr Pisar <ppisar@redhat.com> - 0-13.20181121gitb476930
- Rebased to b47693024402fa8760edcd4fed71131cbd5ac175

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20180322git51802a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 David Abdurachmanov <david.abdurachmanov@gmail.com> - 0-11.20180322git51802a8
- Switch to %%{valgrind_arches}

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 0-10.20180322git51802a8
- Rebase to 51802a869db97326c803dcabdb6e6ed0797a715a

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20150729gitd7bc683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20150729gitd7bc683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20150729gitd7bc683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20150729gitd7bc683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20150729gitd7bc683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Petr Pisar <ppisar@redhat.com> - 0-4.20150729gitd7bc683
- Rebase to d7bc683b6eaba225f483621485035a8044634376

* Wed Jul 29 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0-3.20150331gitcf029fa
- Fix build on aarch64 (upstream issue https://github.com/zeevt/csnappy/issues/23 got note)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.20150331gitcf029fa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0-1.20150331gitcf029fa
- Rebase to 20150331
- Use same make flags for tests
- Use %%license

* Fri Jan 16 2015 Dan Horák <dan[at]danny.cz> - 0-1.20141010gitb43c183
- valgrind is available only on selected arches

* Mon Oct 13 2014 Petr Pisar <ppisar@redhat.com> - 0-0.20141010gitb43c183
- b43c183fdad31be0500a5f2ae022a54a66cb1a3d snapshot

