Name:           flatpak-rpm-macros
Version:        33
Release:        2%{?dist}
Summary:        Macros for building RPMS for flatpaks
Source0:        macros.flatpak
Source1:        distutils.cfg
Source2:        flatpak.xml
License:        MIT

# Buildrequire these to satisfy Pyton byte-compilation hooks
BuildRequires:  python3

%description
The macros in this package set up the RPM build environment so built
applications install in /app rather than /usr. This package is meant
only for installation in buildroots for modules that will be packaged
as Flatpaks.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm
install -t $RPM_BUILD_ROOT%{_sysconfdir}/rpm -p -m 644 %{SOURCE0}
for v in 3.9 ; do
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/python$v/distutils/
    install -t $RPM_BUILD_ROOT%{_libdir}/python$v/distutils/ %{SOURCE1}
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}/xmvn/config.d
install -t $RPM_BUILD_ROOT%{_datadir}/xmvn/config.d -m 644 %{SOURCE2}

%files
# The location in sysconfdir contradicts
# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
# but I believe is necessary to properly override macros that are otherwise set.
%{_sysconfdir}/rpm/
%{_libdir}/python*/distutils/distutils.cfg
%{_datadir}/xmvn/config.d/flatpak.xml

%changelog
* Sat Sep 19 2020 Kalev Lember <klember@redhat.com> - 33-2
- Redefine __python2 macro to point to /app/bin/python2

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 33-1
- Update %%python_sitearch for python-3.9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 18 2020 Kalev Lember <klember@redhat.com> - 32-2
- Remove Python 2 support (#1805232)

* Wed Mar 18 2020 Stephan Bergmann <sbergman@redhat.com> - 32-1
- Let xmvn_install store artifacts under /app

* Thu Feb 06 2020 David King <amigadave@amigadave.com> - 29-12
- Update %%python_sitearch for python-3.8 (#1799346)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Kalev Lember <klember@redhat.com> - 29-9
- Use optflags, rather than __global_compiler_flags

* Thu Apr 04 2019 Stephan Bergmann <sbergman@redhat.com> - 29-8
- Add CFLAGS and CXXFLAGS to macros.flatpak, to match LDFLAGS

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Owen Taylor <otaylor@redhat.com> - 29-6
- Fix accidentally not installing the macro file

* Thu Sep 27 2018 Owen Taylor <otaylor@redhat.com> - 29-5
- Install a distutils.cfg to redirect installation of Python packages to /app
  this makes the package no longer noarch because the file is in
  /usr/lib or /usr/lib64.

* Tue Sep 25 2018 Owen Taylor <otaylor@redhat.com> - 29-4
- Remove space in -L <libdir>

* Thu Sep 20 2018 Owen Taylor <otaylor@redhat.com> - 29-3
- Extend set of overriden Python macros

* Wed Sep 19 2018 Owen Taylor <otaylor@redhat.com> - 29-2
- Improve LDFLAGS flags handling in macros.flatpak

* Sat Sep  8 2018 Owen Taylor <otaylor@redhat.com> - 29-1
- Instead of defining %%app to true, define %%flatpak to 1
- Update %%python_sitearch for python-3.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Owen Taylor <otaylor@redhat.com> - 27-2
See https://bugzilla.redhat.com/show_bug.cgi?id=1460076
- Wrap description lines
- Own /etc/rpm, to avoid requiring rpm package
- Preserve timestamp on installation

* Wed May 31 2017 Owen Taylor <otaylor@redhat.com> - 27-1
- Initial version, based on work by Alex Larsson <alexl@redhat.com>
