%define basen black-hole-solver
%define libname_orig lib%{basen}
%define major 1
%define libname lib%{basen}%{major}
%define develname lib%{basen}-devel

Name: %{basen}
Version: 1.6.0
Release: 2%{?dist}
# The entire source code is MIT except xxHash-0.6.5/ which is BSD
License: MIT and BSD
Source0: https://fc-solve.shlomifish.org/downloads/fc-solve/%{basen}-%{version}.tar.xz
URL: https://www.shlomifish.org/open-source/projects/black-hole-solitaire-solver/
Requires: %{libname}%{?_isa} = %version-%release
Summary: The Black Hole Solitaire Solver Executable
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Dir::Manifest)
BuildRequires: perl(Env::Path)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Inline)
BuildRequires: perl(Inline::C)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::RunValgrind)
BuildRequires: perl(Test::Trap)
BuildRequires: perl(autodie)
BuildRequires: perl(base)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-devel
BuildRequires: python3
BuildRequires: rinutils-devel
BuildRequires: valgrind
BuildRequires: xxhash-devel

%description
This is a solver, written in C, to solve the Solitaire variants “Golf”,
“Black Hole” and “All in a Row”. It provides a portable C library, and
a command line application that after being fed with a layout will emit the
cards to move.

%files
%license COPYING
%doc NEWS.asciidoc README.md
%_bindir/black-hole-solve
%{_mandir}/man6/black-hole-solve.6.*

#--------------------------------------------------------------------

%package -n %{libname}
Summary: The Black Hole Solver dynamic libraries

%description -n %{libname}
Contains the Black Hole Solver libraries that are used by some programs.

This package is mandatory for the Black Hole Solver executable too.

%files -n %{libname}
%{_libdir}/libblack_hole_solver.so.%{major}{,.*}

#--------------------------------------------------------------------

%package -n %{develname}
Summary: The Black Hole Solitaire development tools
Requires: %{libname}%{?_isa} = %version-%release
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
Development tools for the Black Hole Solitaire Solver.

%files -n %{develname}
%_includedir/black-hole-solver/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libblack_hole_solver.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
# The game limit flags are recommended by the PySolFC README.
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DBUILD_STATIC_LIBRARY= -DDISABLE_APPLYING_RPATH=TRUE -DUSE_SYSTEM_XHASH=TRUE
%make_build

%check
%ifarch %arm
# valgrind suppression not working without glibc-debuginfo breaks it
rm -f t/valgrind.t
%endif
rm -f t/clang-format.t
rm -f t/perltidy.t
# fails due to build containing binaries
rm -f t/style-trailing-space.t
# %%make_build test
perl ./run-tests.pl

%install
%{make_install}
rm -f %{buildroot}/%{_libdir}/*.a

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Shlomi Fish <shlomif@cpan.org> 0.20.0-1
- Initial Fedora package based on the Mageia one.
