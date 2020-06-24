# vim: syntax=spec

%global libdir %{_prefix}/lib

Name: rpkg-macros
Version: 0.4
Release: 2%{?dist}
Summary: Set of preproc macros for rpkg utility
License: GPLv2+
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#537a18ab6caac978885a509c76c11d269f30ccb1:macros
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util/macros
# git checkout rpkg-macros-0.4-1
# ./rpkg spec --sources
Source0: rpkg-util-macros-537a18ab.tar.gz

BuildArch: noarch

BuildRequires: bash
BuildRequires: preproc
%if 0%{?fedora}
BuildRequires: git-core
%else
BuildRequires: git
%endif
BuildRequires: coreutils
BuildRequires: findutils

Requires: bash
%if 0%{?fedora}
Requires: git-core
%else
Requires: git
%endif
Requires: coreutils
Requires: findutils

%description
Set of preproc macros to be used by rpkg utilility. They
are designed to dynamically generate certain parts
of rpm spec files. You can use those macros also without
rpkg by:

   $ cat <file_with_the_macros> | preproc -s /usr/lib/rpkg.macros.d/all.bash

You can also source /usr/lib/rpkg.macros.d/all.bash into
your bash environment and then you can experiment with
them directly on your command-line. See content in
/usr/lib/rpkg.macros.d to discover available macros.

%prep
%setup -q -n rpkg-util-macros

%check
PATH=bin/:$PATH tests/run

%install
install -d %{buildroot}%{libdir}
install -d %{buildroot}%{libdir}/rpkg.macros.d
cp -ar macros.d/* %{buildroot}%{libdir}/rpkg.macros.d

install -d %{buildroot}%{_bindir}
install -p -m 755 bin/pack_sources %{buildroot}%{_bindir}/pack_sources

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{libdir}/rpkg.macros.d
%{_bindir}/pack_sources

%changelog
* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.4-2
- rebuild due to koji break down

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.4-1
- remove shebangs in library files according to Fedora review
- changes according to review - usage of %%{_prefix} in spec, g-w for
pack_sources
- use git-core on Fedoras

* Fri Mar 06 2020 clime <clime@fedoraproject.org> 0.3-1
- fix warning about unset git indetity in test_submodule_sources
- skip test for submodule_sources on epel6
- add missing sleep in tests, add TODO
- fix changelog renderring for legacy git as there is no points-at
  option
- resolve problem in git_pack and submodules for epel7

* Wed Mar 04 2020 clime <clime@fedoraproject.org> 0.2-1
- fix bug on centos7 bash in is_physical_subpath function

* Wed Mar 04 2020 clime <clime@fedoraproject.org> 0.1-1
- initial release
