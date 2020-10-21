Name:           wordgrinder
Version:        0.7.2
Release:        6%{?dist}
Summary:        A command line word processor

License:        MIT
URL:            http://cowlark.com/wordgrinder
%global pkgid   %{name}-%{version}
Source:         https://github.com/davidgiven/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc make ncurses-devel ninja-build
BuildRequires:  lua-devel lua-libs lua lua-filesystem
BuildRequires:  zlib-devel libXft-devel
Requires:       ncurses-libs lua-filesystem
# luaJIT is not available on all architectures
#ExcludeArch:   s390x ppc64 ppc64le

%description
WordGrinder is a Unicode-aware character cell word processor that runs in a
terminal (or a Windows console). It is designed to get the hell out of your way
and let you get some work done.

WordGrinder is a word processor for processing words. It is not WYSIWYG. It is
not point and click. It is not a desktop publisher. It is not a text editor. It
does not do fonts and it barely does styles. What it does do is words. It's
designed for writing text. It gets out of your way and lets you type

%package x11
Summary: X11 version of WordGrinder
Requires: %name = %version-%release
Requires: libX11
%description x11
An X11 version of the WordGrinder word processor.

%prep

%setup -q -n %{name}-%{version}

###############################################################################
%build

CFLAGS=-g PREFIX=$RPM_BUILD_ROOT/%{_prefix} OBJDIR=$RPM_BUILD_ROOT/tmp WANT_STRIPPED_BINARIES=no make %{?_smp_mflags}

###############################################################################
%install

make install PREFIX=$RPM_BUILD_ROOT/%{_prefix}
#make install

###############################################################################
%files
%license licenses/COPYING.WordGrinder
%_bindir/wordgrinder
%_docdir/wordgrinder/README.wg
%_mandir/man1/wordgrinder.1*

%files x11
%license licenses/COPYING.WordGrinder
%_bindir/xwordgrinder
###############################################################################
%changelog
* Tue Sep 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.7.2-6
- Change ncurses dependency to be more specific

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Ben Cotton <bcotton@fedoraproject.org> - 0.7.2-1
- Update to latest upstream release
- Remove unnecessary patch to build scripts

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.7.1-1
- Update to latest upstream release
- Remove unneeded dependences, which allows us more build arches
- Split the X11 version into an optional subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-4
- Fix debuginfo issues

* Thu Jul 06 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-3
- Update the patch to build on Fedora 26

* Sun Jul 02 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-2
- Change lua to a version supported by upstream (5.1)

* Wed Jun 07 2017 Ben Cotton <bcotton@fedoraproject.org> - 0.6-1
- Initial RPM release
