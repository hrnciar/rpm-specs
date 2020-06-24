# The octave_pkg_build and octave_pkg_install macros assume a package that is
# only octave code, not an addon like in this package.  We define our own
# versions of the macros here to operate only on the correct directory.
%global my_octave_pkg_build(T) %{lua:
  if (rpm.expand("%{-T}") == "-T") then
    octpkg_tarfile = rpm.expand("%{SOURCE0}")
  else
    octpkg_tarfile = rpm.expand("%{_tmppath}/%{octpkg}-%{version}.tar.gz")
    print("tar czf "..octpkg_tarfile.." -C "..rpm.expand("%{_builddir}/%{buildsubdir}/examples %{buildsubdir}").."\\n")
  end
  print(rpm.expand("mkdir -p %{_builddir}/%{buildsubdir}/examples/%{buildsubdir}/build\\n"))
  print(rpm.expand("octave -H -q --no-window-system --no-site-file --eval 'pkg build -verbose -nodeps %{_builddir}/%{buildsubdir}/examples/%{buildsubdir}/build "..octpkg_tarfile).."'\\n")
  print(rpm.expand("tar xf "..octpkg_tarfile.." -C %{_builddir}/%{buildsubdir}/examples/%{buildsubdir}/build\\n"))
}

%global my_octave_pkg_install \
mkdir -p %{buildroot}%{octprefix} \
mkdir -p %{buildroot}%{octarchprefix} \
%octave_cmd pkg("prefix","%{buildroot}%{octprefix}","%{buildroot}%{octarchprefix}");pkg("global_list",fullfile("%{buildroot}%{octshareprefix}","octave_packages"));pkg("local_list",fullfile("%{buildroot}%{octshareprefix}","octave_packages"));pkg("install","-nodeps","-verbose",glob("%{_builddir}/%{buildsubdir}/examples/%{buildsubdir}/build/%{octpkg}-%{version}-*.tar.gz"){1,1});unlink(pkg("local_list"));unlink(pkg("global_list")); \
if [ -e %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m ] \
then \
  mv %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m.orig \
fi \
echo "function on_uninstall (desc)" > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
echo "  error ('Can not uninstall %s installed by the redhat package manager', desc.name);" >> %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
echo "endfunction" >> %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
if [ -e %{_builddir}/%{buildsubdir}/examples/%{buildsubdir}/build/%{octpkg}-%{version}/*.metainfo.xml ] \
then \
  echo "Found .metainfo.xml appdata file" \
  mkdir -p %{buildroot}/%{_metainfodir} \
  cp -p %{_builddir}/%{buildsubdir}/examples/%{buildsubdir}/build/%{octpkg}-%{version}/*.metainfo.xml %{buildroot}/%{_metainfodir}/ \
  appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml \
else \
  echo "Did not find a .metainfo.xml appdata file" \
fi \
%{nil}

Name:           mpsolve
Version:        3.2.1
Release:        1%{?dist}
Summary:        Multiprecision polynomial solver

License:        GPLv3+
URL:            https://numpi.dm.unipi.it/software/mpsolve
Source0:        https://github.com/robol/MPSolve/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  doxygen-latex
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gmp-devel
BuildRequires:  ImageMagick
BuildRequires:  libtool
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(octave)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  python3-devel
BuildRequires:  tex(dvips)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global _desc %{expand:
MPSolve stands for Multiprecision Polynomial SOLVEr.  It aims to provide
an easy to use universal blackbox for solving polynomials and secular
equations.

Its features include:
- Arbitrary precision approximation.
- Guaranteed inclusion radii for the results.
- Exploiting of polynomial structures: it can take advantage of sparsity
  as well as coefficients in a particular domain (i.e. integers or
  rationals).
- It can be specialized for specific classes of polynomials.  As an
  example, the roots of the Mandelbrot polynomial of degree 2,097,151
  were computed in about 10 days on a dual Xeon server.}

%description %_desc

This package contains command-line interfaces to %{name}.

%package        libs
Summary:        Multiprecision polynomial solver library

%description    libs %_desc

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc %_desc

This package contains developer documentation for %{name}.

%package        devel
Summary:        Headers and library links for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
This package contains header and library links for developing
applications that use %{name}.

%package     -n xmpsolve
Summary:        Qt GUI for mpsolve
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info%{?_isa}

%description -n xmpsolve %_desc

This package contains a Qt-based graphical interface to mpsolve.

%package     -n python3-mpsolve
Summary:        Python 3 interface to mpsolve
BuildArch:      noarch
Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-mpsolve %_desc

This package contains a python 3 interface to mpsolve.

%global octpkg  %{name}

%package     -n octave-mpsolve
Summary:        Octave interface to mpsolve
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description -n octave-mpsolve %_desc

This package contains an octave interface to mpsolve.

%prep
%autosetup -n MPSolve-%{version} -p1

# Fix the version number in the octave interface
sed -i 's/3\.1\.7/%{version}/' examples/octave/DESCRIPTION

# Octave wants the COPYING file
cp -p COPYING examples/octave

# We do not need both HTML and PDF documentation
sed -i '/GENERATE_LATEX/s/YES/NO/' doc/Doxyfile.in

# Doxygen wants the CSS file up one level
cp -p doc/doxygen/doxygen.css doc

# Invoke python3, not python
sed -i 's,%{_bindir}/env python,%{__python3},' examples/python/tests/*.py

# Do not force use of -fomit-frame-pointer
sed -i '/-fomit-frame-pointer/d' configure.ac

# Generate the configure script
autoreconf -fi .

%build
%configure --disable-static --disable-debug --enable-qml-ui LIBS=-lpthread

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# Work around https://bugs.ghostscript.com/show_bug.cgi?id=702024
export GS_OPTIONS=-dNOSAFER

%make_build

# Rebuild the octave package the Fedora way
cd examples
rm octave/mpsolve.tar.gz
cp -a octave MPSolve-%{version}
%my_octave_pkg_build
cd -

%install
%make_install

# We do not want the libtool files
rm -f %{buildroot}%{_libdir}/*.la

# Move the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/192x192/apps
mv %{buildroot}%{_datadir}/icons/xmpsolve.png \
   %{buildroot}%{_datadir}/icons/hicolor/192x192/apps

# Generate more icon sizes
for sz in 16 22 24 32 36 48 64 72 96 128 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  convert src/xmpsolve/xmpsolve.png -resize ${sz}x${sz} \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/xmpsolve.png
done

# Reinstall the octave package the Fedora way
%my_octave_pkg_install

%check
make check

%post        -n octave-mpsolve
%octave_cmd pkg rebuild

%preun       -n octave-mpsolve
%octave_pkg_preun

%postun      -n octave-mpsolve
%octave_cmd pkg rebuild

%files
%{_bindir}/mandelbrot-solver
%{_bindir}/mpsolve
%{_bindir}/quadratic-solver
%{_bindir}/root_of_unity
%{_bindir}/secular
%{_mandir}/man1/mandelbrot-solver.1*
%{_mandir}/man1/mpsolve.1*
%{_mandir}/man1/quadratic-solver.1*

%files          libs
%doc AUTHORS README
%license COPYING
%{_libdir}/libmps.so.3*
%{_libdir}/libmps-fortran.so.0*

%files          doc
%doc doc/html/*
%license COPYING

%files          devel
%doc ChangeLog
%{_includedir}/mps/
%{_libdir}/libmps.so
%{_libdir}/libmps-fortran.so

%files       -n xmpsolve
%{_bindir}/xmpsolve
%{_datadir}/applications/xmpsolve.desktop
%{_datadir}/icons/hicolor/*/apps/xmpsolve.png
%{_datadir}/mime/packages/mpsolve.xml
%{_datadir}/mime-info/mpsolve.mime
%{_mandir}/man1/xmpsolve.1*

%files       -n python3-mpsolve
%{python3_sitelib}/mpsolve.py
%{python3_sitelib}/__pycache__/mpsolve.*

%files       -n octave-mpsolve
%{octpkglibdir}/
%dir %{octpkgdir}/
%{octpkgdir}/mps_polyeig.m
%{octpkgdir}/packinfo/
%doc %{octpkgdir}/doc-cache

%changelog
* Fri Jun 12 2020 Jerry James <loganjerry@gmail.com> - 3.2.1-1
- Version 3.2.1
- The formerly missing files are now included in the tarball

* Thu Jun 11 2020 Jerry James <loganjerry@gmail.com> - 3.2.0-1
- Version 3.2.0
- Drop upstreamed patches: -strict-aliasing and -mpq-canonicalize

* Wed May 27 2020 Jerry James <loganjerry@gmail.com> - 3.1.8-1
- Initial RPM
