%global deb_ver 1.8.1+git20161012-2

Name:            pseudo
Version:         1.9.0
Release:         11%{?dist}
Summary:         Advanced tool for simulating superuser privileges

License:         GPLv3+ and LGPLv2+
URL:             https://www.yoctoproject.org/software-item/pseudo/
Source0:         https://downloads.yoctoproject.org/releases/pseudo/pseudo-%{version}.tar.bz2
Source1:         http://http.debian.net/debian/pool/main/p/pseudo/pseudo_%{deb_ver}.debian.tar.xz

# Fix build with latest libattr
Patch0:          pseudo-1.9.0-attr.patch
# Fix build with GCC-10
Patch1:          pseudo-1.9.0-gcc10.patch

BuildRequires:   attr
BuildRequires:   gcc
BuildRequires:   libattr-devel
BuildRequires:   python3
BuildRequires:   python3-rpm-macros
BuildRequires:   sqlite-devel
Requires(post):  %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%global __provides_exclude_from ^(%{_libdir}/pseudo/.*\\.so)$

%description
The pseudo utility offers a way to run commands in a virtualized "root"
environment, allowing ordinary users to run commands which give the illusion of
creating device nodes, changing file ownership, and otherwise doing things
necessary for creating distribution packages or filesystems.

Pseudo has a lot of similarities to fakeroot but is a new implementation that
improves on the problems seen using fakeroot. Pseudo is now extensively used by
Poky as a replacement to fakeroot but can also be used standalone in many other
use cases.

%prep
%autosetup -p1 -a1
sed -i -e "1s,#!.*,#!%{__python3}," make*
sed -e 's,@LIBDIR@,%{_libdir}/pseudo,g' debian/fakeroot-pseudo.in > debian/fakeroot-pseudo
# tclsh is not available in Fedora
rm test/test-tclsh-fork.sh

%build
# custom configure script
%set_build_flags
./configure                  \
  --bits=%{__isa_bits}       \
  --cflags="$CFLAGS"         \
  --enable-memory-db         \
  --enable-xattr             \
  --enable-xattrdb           \
  --libdir=%{_libdir}/pseudo \
  --prefix=%{_prefix}        \
  --without-rpath
%make_build

%install
%make_install
install -Dpm0755 debian/fakeroot-pseudo %{buildroot}%{_bindir}
install -Dpm0644 debian/fakeroot-pseudo.1 %{buildroot}%{_mandir}/man1/fakeroot-pseudo.1
install -Dpm0644 pseudo.1 %{buildroot}%{_mandir}/man1/pseudo.1
install -Dpm0644 pseudolog.1 %{buildroot}%{_mandir}/man1/pseudolog.1
# For alternatives support
touch %{buildroot}%{_bindir}/fakeroot %{buildroot}%{_mandir}/man1/fakeroot.1

%check
./run_tests.sh -v
chmod u+x d2

%post
%if 0%{?rhel} && 0%{?rhel} < 7
# fakeroot in RHEL < 7 doesn't support alternatives
link=$(readlink -e "%{_bindir}/fakeroot")
if [ "$link" = "%{_bindir}/fakeroot" ]; then
  rm -f %{_bindir}/fakeroot
fi
%endif
%{_sbindir}/update-alternatives --install %{_bindir}/fakeroot fakeroot \
  %{_bindir}/fakeroot-pseudo 5 \
  --slave %{_mandir}/man1/fakeroot.1.gz fakeroot.1.gz %{_mandir}/man1/fakeroot-pseudo.1.gz

%preun
if [ $1 = 0 ]; then
  %{_sbindir}/alternatives --remove fakeroot %{_bindir}/fakeroot-pseudo
fi

%files
%license COPYING
%doc ChangeLog.txt Futures.txt README
%ghost %{_bindir}/fakeroot
%{_bindir}/fakeroot-pseudo
%{_bindir}/pseudo
%{_bindir}/pseudodb
%{_bindir}/pseudolog
%{_libdir}/pseudo
%ghost %{_mandir}/man1/fakeroot.1*
%{_mandir}/man1/fakeroot-pseudo.1*
%{_mandir}/man1/pseudo.1*
%{_mandir}/man1/pseudolog.1*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Dominik Mierzejewski <dominik@greysector.net> 1.9.0-10
- fix build with GCC-10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.9.0-6
- Rebuild with fixed binutils

* Sat Jul 28 2018 Dominik Mierzejewski <dominik@greysector.net> 1.9.0-5
- update upstream URL
- set build flags using set_build_flags macro
- use python3 explicitly during build (ignatenko)
- add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot (ignatenko)
- add patch to fix compilation with libattr 2.4.48 (ignatenko)
- improve libattr patch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Dominik Mierzejewski <dominik@greysector.net> 1.8.2-2
- drop tclsh test, tclsh is not shipped in Fedora
- drop obsolete patch

* Tue Mar 28 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Dominik Mierzejewski <dominik@greysector.net> 1.8.1-3
- fix condition on Fedora

* Mon Oct 10 2016 Dominik Mierzejewski <dominik@greysector.net> 1.8.1-2
- make sure _libdir/pseudo is owned
- fakeroot without alternatives support exists on RHEL < 7 only

* Sun Oct 09 2016 Dominik Mierzejewski <dominik@greysector.net> 1.8.1-1
- update to 1.8.1
- use upstream release tarball
- add missing NAME section to manpage (patch from Debian)
- fix passing CFLAGS containing commas via --cflags
- install missing pseudolog(1) manpage

* Thu Apr 07 2016 Dominik Mierzejewski <dominik@greysector.net> 1.7.5-1
- update to 1.7.5

* Mon Nov 30 2015 Dominik Mierzejewski <dominik@greysector.net> 1.7.4-1
- initial build
- filter private library from Provides:
- filter -m32/-m64 option from compiler flags on arm and s390
