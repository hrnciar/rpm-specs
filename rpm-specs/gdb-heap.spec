# We build this as an arch-specific package so that we can follow /lib
# vs /lib64 differences in the location of the underlying glibc library

# We don't want a -debuginfo package:
%global debug_package %{nil}
# (I tried using _enable_debug_packages but that didn't work for some reason)

Name:           gdb-heap
Version:        0.5
%global commit  f3dcc5309e55683c67ccb35e98b090421825a22a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Release:        37.20191013git%{shortcommit}%{?dist}
Summary:        Extensions to gdb for debugging dynamic memory allocation

# The code is almost all LGPLv2+, apart from heap/python.py, which is
# Python-licensed:
License:        LGPLv2+ and Python

URL:            https://github.com/rogerhu/gdb-heap
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Fix sorting for Python3, field names, and lib paths
Patch1:         %{url}/pull/25.patch

BuildRequires:  python3-devel

Requires:       python3
Requires:       python3-ply

%global glibc_version %(rpm -q glibc --qf "%%{VERSION}")
%global glibc_soversion %{glibc_version}
%global glibc_dso_name  ld-%{glibc_soversion}.so
%global gdb_autoload_dir %{_datadir}/gdb/auto-load
%global script_install_dir %{gdb_autoload_dir}/%{_lib}
%global script_install_path %{script_install_dir}/%{glibc_dso_name}-gdb.py

%global module_install_path %{_datadir}/gdb-heap

# This is autoloaded by gdb if the relevant glibc library is in memory.
# To do this, it must be at the correct location on the filesystem 
# For this to work, we need a matching glibc version:
Requires: glibc%{_isa} = %{glibc_version}

Requires: gdb

# It is only really usable if that glibc library's debuginfo is available, but
# the user may not have enable the debuginfo repository.
# 
# From version 0.3 onwards the code detects missing debuginfo and provides a
# suggestion to the user on how to install it

%description
gdb-heap adds a "heap" command to the gdb debugger, for use in debugging
dynamic memory allocation problems in user space.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
# empty

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{module_install_path}/heap
cp -a heap/*.py %{buildroot}/%{module_install_path}/heap

mkdir -p %{buildroot}/%{script_install_dir}

# Build the auto-loaded entrypoint script, adding module_install_path
# to sys.path:
echo \
  "import sys; sys.path.append('%{module_install_path}')" \
  > %{buildroot}/%{script_install_path}

cat gdbheap.py \
  >> %{buildroot}/%{script_install_path}



%files
%doc LICENSE.txt LICENSE-lgpl-2.1.txt LICENSE-python.txt
%{script_install_path}*
%{module_install_path}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-37.20191013gitf3dcc53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-36.20191013gitf3dcc53
- Switch to new upstream
- Switch to Python 3
- Get glibc version dynamically

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5-32
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 17 2017 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.5-31
- Update glibc version to rawhide (2.26.90).

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar  8 2017 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.5-29
- Update glibc version to rawhide (2.25.90).

* Sat Feb 25 2017 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.5-28
- Update glibc version to rawhide (2.25).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.5-26
- Version bump to fix UPGRADEPATH.

* Wed Aug 10 2016 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.5-25
- Update glibc version to rawhide (2.24.90).

* Tue Mar  1 2016 Siddhesh Poyarekar <sid@reserved-bit.com> - 0.5-24
- Update glibc version to rawhide (2.23.90).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 16 2015 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.5-22
- Update glibc version to rawhide (2.22.90).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.5-20
- Update glibc version to rawhide (2.21.90).

* Mon Sep  8 2014 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.5-19
- Update glibc version to rawhide (2.20.90).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.5-16
- Update glibc version to rawhide (2.19.90).

* Wed Sep 18 2013 David Malcolm <dmalcolm@redhat.com> - 0.5-15
- update glibc version to rawhide (2.18.90)

* Sat Aug 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.5-14
- update glibc version to rawhide (2.18)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 0.5-12
- Rebuild for latest glibc.

* Wed Oct 31 2012 Tom Callaway <spot@fedoraproject.org> - 0.5-11
- update glibc version to rawhide (2.16.90)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb  7 2012 David Malcolm <dmalcolm@redhat.com> - 0.5-8
- update glibc version to 2.15

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 David Malcolm <dmalcolm@redhat.com> - 0.5-6
- update glibc version to 2.14.90

* Fri Jun 10 2011 Adam Jackson <ajax@redhat.com> 0.5-5
- Rebuild for new glibc version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 David Malcolm <dmalcolm@redhat.com> - 0.5-3
- update glibc version to 2.13.90

* Wed Sep 29 2010 David Malcolm <dmalcolm@redhat.com> - 0.5-2
- cherrypick fix for rhbz#638662

* Thu Aug 12 2010 David Malcolm <dmalcolm@redhat.com> - 0.5-1
- 0.5
- add requirement on python-ply

* Wed Aug  4 2010 David Malcolm <dmalcolm@redhat.com> - 0.4-1
- 0.4: add licenses and license headers

* Tue Aug  3 2010 David Malcolm <dmalcolm@redhat.com> - 0.3-1
- 0.3: detect and warn about missing debuginfo; disable C++ support for
now (rhbz620930)

* Tue Aug  3 2010 David Malcolm <dmalcolm@redhat.com> - 0.2-2
- use the gdb autoload directory, relative to the glibc.so, rather than the
.debug file
- add requirement on gdb
- bump glibc version to that in F14

* Thu Jul 29 2010 David Malcolm <dmalcolm@redhat.com> - 0.2-1
- 0.2
- install private modules to _datadir rather than _libdir

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-2
- fix License tag
- require specific glibc package version, rather than a specific file within
glibc-debuginfo
- standardize on buildroot rpm macro rather than RPM_BUILD_ROOT env var

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-1
- initial packaging
