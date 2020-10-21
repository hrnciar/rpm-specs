Name:          notcurses
Version:       2.0.1
Release:       1%{?dist}
Summary:       Character graphics and TUI library
License:       ASL 2.0
URL:           https://nick-black.com/dankwiki/index.php/Notcurses
Source0:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/notcurses_%{version}+dfsg.1.orig.tar.xz
Source1:       https://github.com/dankamongmen/%{name}/releases/download/v%{version}/notcurses_%{version}+dfsg.1.orig.tar.xz.asc
Source2:       https://nick-black.com/dankamongmen.gpg

BuildRequires: gnupg2
BuildRequires: cmake
BuildRequires: doctest-devel
BuildRequires: gcc-c++
BuildRequires: libqrcodegen-devel
BuildRequires: libunistring-devel
BuildRequires: OpenImageIO-devel
BuildRequires: pandoc
BuildRequires: python3-cffi
BuildRequires: python3-devel
BuildRequires: python3-pypandoc
BuildRequires: python3-setuptools
BuildRequires: pkgconfig(ncurses)

%description
Notcurses facilitates the creation of modern TUI programs,
making full use of Unicode and 24-bit TrueColor. It presents
an API similar to that of Curses, and rides atop Terminfo.
This package includes C and C++ shared libraries.

%package devel
Summary:       Development files for the Notcurses library
License:       ASL 2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the notcurses library.

%package static
Summary:       Static library for the Notcurses library
License:       ASL 2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description static
A statically-linked version of the notcurses library.

%package utils
Summary:       Binaries from the Notcurses project
License:       ASL 2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description utils
Binaries from Notcurses, and multimedia content used thereby.

%package -n python3-%{name}
Summary:       Python wrappers for notcurses
License:       ASL 2.0
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python wrappers and a demonstration script for the notcurses library.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake -DUSE_MULTIMEDIA=oiio -DDFSG_BUILD=on
%cmake_build
cd python
CFLAGS="-I../include -L../%{_target_platform}/" %py3_build

%check
cd %{_vpath_builddir}
ctest -V %{?_smp_mflags}

%install
%cmake_install
cd python
%py3_install

%files
%doc CONTRIBUTING.md OTHERS.md README.md USAGE.md NEWS.md TERMS.md
%license COPYRIGHT LICENSE
%{_libdir}/libnotcurses.so.%{version}
%{_libdir}/libnotcurses.so.2
%{_libdir}/libnotcurses++.so.2
%{_libdir}/libnotcurses++.so.%{version}

%files devel
%{_includedir}/notcurses/
%{_includedir}/ncpp/
%{_libdir}/libnotcurses.so
%{_libdir}/libnotcurses++.so
%{_libdir}/cmake/Notcurses
%{_libdir}/pkgconfig/notcurses.pc
%{_libdir}/pkgconfig/notcurses++.pc
%{_mandir}/man3/*.3*

%files static
%{_libdir}/libnotcurses.a
%{_libdir}/libnotcurses++.a

%files utils
# Don't use a wildcard, lest we pull in notcurses-*pydemo.1.
%{_bindir}/ncneofetch
%{_bindir}/notcurses-demo
%{_bindir}/notcurses-input
%{_bindir}/notcurses-tester
%{_bindir}/notcurses-tetris
%{_bindir}/notcurses-view
%{_mandir}/man1/ncneofetch.1*
%{_mandir}/man1/notcurses-demo.1*
%{_mandir}/man1/notcurses-input.1*
%{_mandir}/man1/notcurses-tester.1*
%{_mandir}/man1/notcurses-tetris.1*
%{_mandir}/man1/notcurses-view.1*
%{_datadir}/%{name}

%files -n python3-%{name}
%{_bindir}/notcurses-pydemo
%{_bindir}/notcurses-direct-pydemo
%{_mandir}/man1/notcurses-pydemo.1*
%{_mandir}/man1/notcurses-direct-pydemo.1*
%{python3_sitearch}/*egg-info/
%{python3_sitearch}/notcurses/
%attr(0755, -, -) %{python3_sitearch}/notcurses/notcurses.py
%{python3_sitearch}/*.so

%changelog
* Mon Oct 19 2020 Nick Black <dankamongmen@gmail.com> - 2.0.1-1
- New upstream version, quadblitter perf+transparency improvements

* Tue Oct 13 2020 Nick Black <dankamongmen@gmail.com> - 2.0.0-1
- New upstream version, stable API!

* Sat Oct 10 2020 Nick Black <dankamongmen@gmail.com> - 1.7.6-1
- New upstream version

* Tue Sep 29 2020 Nick Black <dankamongmen@gmail.com> - 1.7.5-1
- New upstream version, drop notcurses-ncreel binary

* Sun Sep 20 2020 Nick Black <dankamongmen@gmail.com> - 1.7.4-1
- New upstream version

* Sat Sep 19 2020 Nick Black <dankamongmen@gmail.com> - 1.7.3-1
- New upstream version

* Fri Sep 11 2020 Nick Black <dankamongmen@gmail.com> - 1.7.2-1
- New upstream version
- Undo cmake changes from 1.7.1-2, which broke build on fc34

* Fri Sep 04 2020 Richard Shaw <hobbes1069@gmail.com> - 1.7.1-2
- Rebuild for OpenImageIO 2.2.
- Replace _target_platform with _vtable_builddir as that's what %%cmake
  current uses but may change in the future.

* Mon Aug 31 2020 Nick Black <dankamongmen@gmail.com> - 1.7.1-1
- New upstream version

* Sun Aug 30 2020 Nick Black <dankamongmen@gmail.com> - 1.7.0-1
- New upstream version, add notcurses-direct-pydemo

* Sun Aug 30 2020 Nick Black <dankamongmen@gmail.com> - 1.6.20-1
- New upstream version, note change to CMake install

* Thu Aug 27 2020 Nick Black <dankamongmen@gmail.com> - 1.6.19-1
- New upstream version, reenable unit tests for s390

* Wed Aug 12 2020 Nick Black <dankamongmen@gmail.com> - 1.6.12-1
- New upstream version, many small bugfixes

* Mon Aug 03 2020 Nick Black <dankamongmen@gmail.com> - 1.6.11-1
- New upstream version with new 'zoo' demo

* Sun Aug 02 2020 Nick Black <dankamongmen@gmail.com> - 1.6.10-1
- New upstream version with Linux console font reprogramming

* Sun Jul 12 2020 Nick Black <dankamongmen@gmail.com> - 1.6.1-1
- New upstream version, purge vt100 patch (applied upstream), install TERMS.md

* Sat Jul 04 2020 Nick Black <dankamongmen@gmail.com> - 1.6.0-1
- New upstream version, backport patch to work on vt100 autobuilder, enable all tests

* Sun Jun 28 2020 Nick Black <dankamongmen@gmail.com> - 1.5.3-1
- New upstream version

* Fri Jun 19 2020 Nick Black <dankamongmen@gmail.com> - 1.5.2-1
- New upstream version, new binary 'ncneofetch'

* Sun Jun 14 2020 Nick Black <dankamongmen@gmail.com> - 1.5.1-1
- New upstream version

* Mon Jun 08 2020 Nick Black <dankamongmen@gmail.com> - 1.5.0-1
- New upstream version

* Sat Jun 06 2020 Nick Black <dankamongmen@gmail.com> - 1.4.5-1
- New upstream version, disable Ncpp,Exceptions unit tests for now

* Tue Jun 02 2020 Nick Black <dankamongmen@gmail.com> - 1.4.4.1-1
- New upstream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-3
- Rebuilt for Python 3.9

* Sun May 24 2020 Nick Black <dankamongmen@gmail.com> - 1.4.3-2
- Dep on doctest-devel, run tests, use _target_platform in place of "build"

* Fri May 22 2020 Nick Black <dankamongmen@gmail.com> - 1.4.3-1
- New upstream version

* Wed May 20 2020 Nick Black <dankamongmen@gmail.com> - 1.4.2.4-1
- New upstream version, add python3-setuptools dep

* Sun May 17 2020 Nick Black <dankamongmen@gmail.com> - 1.4.2.3-1
- New upstream version

* Sat Apr 25 2020 Nick Black <dankamongmen@gmail.com> - 1.4.1-1
- New upstream version, incorporate review feedback
- Build against OpenImageIO, install notcurses-view and data

* Tue Apr 07 2020 Nick Black <dankamongmen@gmail.com> - 1.3.3-1
- Initial Fedora packaging
