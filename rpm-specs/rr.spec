# Force out of source build
%undefine __cmake_in_source_build

%global commit b53e4d990b873e1b57284994ad7a65f3626880f5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global baserelease 19

ExclusiveArch:  %{ix86} x86_64

# Disable 32-bit builds on architectures with multilibs
# to avoid attempting pulling in 32-bit in to koji build.
%ifarch x86_64
%global disable32bit -Ddisable32bit=ON
%endif
Summary:        Tool to record and replay execution of applications
Name:           rr
Version:        5.3.0
Release:        %{baserelease}.20200828git%{shortcommit}%{?dist}
# The entire source code is MIT with the exceptions of
# files in following directories:
#   third-party/blake2       CC0
#   third-party/gdb          BSD
#   third-party/proc-service BSD
License:        MIT and CC0 and BSD
URL:            http://rr-project.org
 
Source: https://github.com/mozilla/rr/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

%if  0%{?rhel} == 7
BuildRequires: cmake3
BuildRequires: python36-pexpect
%else
BuildRequires: cmake
BuildRequires: python3-pexpect
%endif
BuildRequires: python3
BuildRequires: make gcc gcc-c++ gdb
BuildRequires: libgcc
BuildRequires: glibc-devel
BuildRequires: libstdc++-devel
BuildRequires: man-pages
BuildRequires: capnproto capnproto-libs capnproto-devel
BuildRequires: patchelf

%description
rr is a lightweight tool for recording and replaying execution
of applications (trees of processes and threads).
For more information, please visit http://rr-project.org

%package testsuite
Summary: Testsuite for checking rr functionality
Requires: rr
Requires: gdb
Requires: python3
%if  0%{?rhel} == 7
Requires: python36-pexpect
Requires: cmake3
%else
Requires: python3-pexpect
Requires: cmake
%endif
%description testsuite
rr-testsuite includes compiled test binaries and other files
which are used to test the functionality of rr.
 
%prep
%setup -q -n rr-%{commit}

%build
%if  0%{?rhel} == 7
%cmake3 -DCMAKE_BUILD_TYPE=Release -DINSTALL_TESTSUITE=ON %{?disable32bit}
%cmake3_build
%else
%cmake -DCMAKE_BUILD_TYPE=Release -DINSTALL_TESTSUITE=ON %{?disable32bit}
%cmake_build
%endif

%install
%if  0%{?rhel} == 7
%cmake3_install
%else
%cmake_install
%endif

rm -rf %{buildroot}%{_datadir}/rr/src

# Using a small hack from the Dyninst testsuite which changes file permissions
# to prevent any stripping of debugging information. This is done for libraries
# and executables used by the testsuite.
find %{buildroot}%{_libdir}/rr/testsuite/obj/bin \
  -type f -name '*' -execdir chmod 644 '{}' '+'

find %{buildroot}%{_libdir} \
  -type f -name '*.so' -execdir chmod 644 '{}' '+'

# Some files contain invalid RPATHS.
patchelf --set-rpath '%{_libdir}/rr/' %{buildroot}%{_libdir}/rr/testsuite/obj/bin/constructor

%files
%dir %{_libdir}/rr
%{_libdir}/rr/*.so
%exclude %{_libdir}/rr/libtest_lib*.so
%{_bindir}/rr
%{_bindir}/rr_exec_stub*
%{_bindir}/signal-rr-recording.sh
%{_bindir}/rr-collect-symbols.py
%{_datadir}/bash-completion/completions/rr
%dir %{_datadir}/rr
%{_datadir}/rr/*.xml
%{_datadir}/rr/rr_page_*

%attr(755,root,root) %{_libdir}/rr/*.so

%files testsuite
%{_libdir}/rr/libtest_lib*.so
%dir %{_libdir}/rr/testsuite
%{_libdir}/rr/testsuite/*

%attr(755,root,root) %{_libdir}/rr/libtest_lib*.so
%attr(755,root,root) %{_libdir}/rr/testsuite/obj/bin/*

%license LICENSE

%changelog
* Fri Aug 28 2020 Sagar Patel <sapatel@redhat.com> - 5.3.0-19.20200828gitb53e4d9
- Sync with upstream branch master,
  commit b53e4d990b873e1b57284994ad7a65f3626880f5.
- Fix package requirements for rr-testsuite.
- Note: There is an issue causing rr to hang on RHEL7 (RHBZ#1873266).
- Note: There are some pathing issues with rr-testsuite.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-17.20200427gitbab9ca9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Neal Gompa <ngompa13@gmail.com> - 5.3.0-16.20200427gitbab9ca9
- Rebuilt for capnproto 0.8.0 again

* Sat Jul 18 2020 Neal Gompa <ngompa13@gmail.com> - 5.3.0-15.20200427gitbab9ca9
- Rebuilt for capnproto 0.8.0

* Mon Apr 27 2020 Sagar Patel <sapatel@redhat.com> 14.20200427gitbab9ca9
- Sync with upstream branch master,
  commit bab9ca94fc03d893cf6b8bf58f7b4522a0113466.
- Build failures from the previous release are now fixed.

* Fri Apr 24 2020 Sagar Patel <sapatel@redhat.com> 13.20200424gitcf5169b
- Sync with upstream branch master,
  commit cf5169bb3e29ce9db4a73e26164bec0e92b083fb.
- Introduces support for installable testsuite.

* Mon Feb 24 2020 Sagar Patel <sapatel@redhat.com> 11.20200224git4513b23
- Sync with upstream branch master,
  commit 4513b23c8092097dc42c73f3cbaf4cfaebd04efe.
- New patches enable rr to be built on older compilers.

* Thu Feb 13 2020 Sagar Patel <sapatel@redhat.com> 10.20200213gitabd3442
- Sync with upstream branch master,
  commit abd344288878c9b4046e0b8664927992947a46eb.
- New patches enable rr to be built on RHEL7.2 and later.

* Tue Jan 14 2020 William Cohen <wcohen@redhat.com> 5.3.0-8.20200124git7908fea
- Sync with upstream branch master,
  commit 70ba28f7ab2923d4e36ffc9d5d2e32357353b25c.
- SRPM buildable on Fedora koji or other rpm build systems.
