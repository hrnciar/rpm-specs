# This is a serial build of NEURON
%global _description %{expand:
NEURON is a simulation environment for modeling individual neurons and networks
of neurons. It provides tools for conveniently building, managing, and using
models in a way that is numerically sound and computationally efficient. It is
particularly well-suited to problems that are closely linked to experimental
data, especially those that involve cells with complex anatomical and
biophysical properties.

This package does not include MPI support.

Please install the %{name}-devel package to compile nmodl files and so on.
}

%global tarname nrn

# fails somehow, disabled by default
%bcond_with metis

# Music support
%bcond_with music

Name:       neuron
Version:    7.8.1
Release:    4%{?dist}
Summary:    A flexible and powerful simulator of neurons and networks

License:    GPLv3+
URL:        http://www.neuron.yale.edu/neuron/
Source0:    https://github.com/neuronsimulator/%{tarname}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:     0001-Unbundle-Random123.patch
# libstdc++ bundled is from 1988: seems heavily modified. Headers from there
# are not present in the current version
# https://github.com/neuronsimulator/nrn/issues/145

# Use system copy of Catch
Patch1:     0002-Unbundle-catch.patch
# We install the python bits ourselves
Patch2:     0003-Disable-python-build-and-install.patch
# Set soversions for all shared objects
Patch3:     0004-Set-soversions-for-libs.patch
# Set the right path for libdir
# Upstreamable
Patch4:     0005-Correct-librxdmath-path-for-64bit.patch

# Quite a lot of files have been dropped in 7.8.1
# https://github.com/neuronsimulator/nrn/issues/719

# Random123 does not build on these, so neither can NEURON
# https://github.com/neuronsimulator/nrn/issues/114
ExcludeArch:    mips64r2 mips32r2 s390

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bison-devel
BuildRequires:  cmake
BuildRequires:  catch-devel
# Needs to be packaged separately
# BuildRequires:  coreneuron-devel
BuildRequires:  flex
BuildRequires:  (flex-devel or libfl-devel)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
# the cmake build requires iv with cmake too
BuildRequires:  iv-devel >= 0.1
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libtool
%if %{with metis}
BuildRequires:  metis-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  Random123-devel

# Bundles sundials. WIP
# https://github.com/neuronsimulator/nrn/issues/113
# BuildRequires:  sundials-devel
Provides: bundled(sundials) = 2.0.1

%description %_description

%package devel
Summary:    Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires:  ncurses-devel
Requires:  readline-devel
Requires:  gcc-c++
Requires:  libtool
Requires:  libX11-devel
Requires:  libXext-devel

%description devel
Headers and development shared libraries for the %{name} package

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch

%description doc
Documentation for %{name}

%package -n python3-%{name}
Summary:   Python3 interface to %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%description -n python3-%{name} %_description


%prep
%autosetup -n %{tarname}-%{version} -S git

# Remove executable perms from source files
find src -type f -executable ! -name '*.sh' -exec chmod -x {} +

# Remove bundled Random123
rm -rf src/Random123
rm -rf src/readline

# Create version file ourselves
export TIMESTAMP=$(date +%Y-%m-%d)
export COMMIT=%{shortcommit}
cat > src/nrnoc/nrnversion.h << EOF
#define GIT_DATE "$TIMESTAMP"
#define GIT_BRANCH "master"
#define GIT_CHANGESET "$COMMIT"
#define GIT_DESCRIBE "Neuron built for Fedora"
EOF

# Use system libtool instead of a local copy that neuron tries to install
for f in bin/*_makefile.in; do
    sed -r -i 's|(LIBTOOL.*=.*)\$\(pkgdatadir\)(.*)|\1$(bindir)\2|' $f
done

# Stop system from using hard coded flags
sed -i '/CompilerFlagsHelpers/ d' cmake/ReleaseDebugAutoFlags.cmake

%build
# Not yet to be used
# export SUNDIALS_SYSTEM_INSTALL="yes"

%cmake \
-DNRN_ENABLE_SHARED=ON \
-DNRN_ENABLE_INTERVIEWS=ON \
-DNRN_ENABLE_PYTHON=ON \
-DNRN_ENABLE_PYTHON_DYNAMIC=OFF \
-DNRN_ENABLE_THREADS=ON \
-DNRN_ENABLE_MEMACS=ON \
-DNRN_ENABLE_RX3D=ON \
-DNRN_ENABLE_CORENEURON=OFF \
-DNRN_ENABLE_TESTS=ON \
-DNRN_ENABLE_REL_RPATH=ON \
-DNRN_ENABLE_MODULE_INSTALL=ON \
-DNRN_ENABLE_INTERNAL_READLINE=OFF \
-DNRN_ENABLE_MPI=OFF \

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool && \
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%cmake_build

# MUSIC support
%if %{with music}
%cmake_build -C src/neuronmusic
pushd %{__cmake_builddir}/src/neuronmusic
%{py3_build}
popd
%endif

%install
%cmake_install

# Music support
%if %{with music}
pushd %{__cmake_builddir}/src/neuronmusic
%{py3_install}
popd
%endif


# Bits from the post install hook
# It requires the libraries before to be installed, not just built, so it must
# be done here. The only alternative is a different package that requires this,
# but this is simpler

# It can't find these somehow.
RPM_LD_FLAGS="%{?__global_ldflags} -L$RPM_BUILD_ROOT/%{_libdir}"
pushd %{__cmake_builddir}/src/nrnpython/
%{py3_build}
%{py3_install}
popd

# Remove installed libtool copy
rm -fv $RPM_BUILD_ROOT/%{_datadir}/%{tarname}/libtool

# Post install clean up
# Remove stray object files
# Probably worth a PR
# Must be done at end, otherwise it deletes object files required for other builds
find . $RPM_BUILD_ROOT/%{_libdir}/ -name "*.o" -exec rm -f '{}' \;
# Remove libtool archives
find . $RPM_BUILD_ROOT/%{_libdir}/ -name "*.la" -exec rm -f '{}' \;
# Remove duplicate files. These are installed in the correct python locations already
# rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{tarname}/lib/python/%{name}

# Remove installed libfiles
rm -rfv $RPM_BUILD_ROOT/%{_prefix}/lib/python/neuron/

# set up second symlink for shared objects
pushd $RPM_BUILD_ROOT/%{_libdir}/
    ln -sv ./libnrniv.so.0.0.0 libnrniv.so.0
    ln -sv ./librxdmath.so.0.0.0 librxdmath.so.0
popd

# Remove stray cpp file
rm -fv $RPM_BUILD_ROOT/%{_datadir}/%{tarname}/*.cpp

# Remove iv header provided by iv package
rm -rf $RPM_BUILD_ROOT/%{_includedir}/ivstream.h

# The makefiles do not have shebangs
%files
%license Copyright
%{_bindir}/modlunit
%{_bindir}/neurondemo
%{_bindir}/nrngui
%{_bindir}/nrniv
%{_bindir}/sortspike
# Not needed but I'll include them for completeness anyway
%{_bindir}/nrnpyenv.sh
%{_bindir}/set_nrnpyenv.sh
# Libs
%{_libdir}/libnrniv.so.0.0.0
%{_libdir}/libnrniv.so.0
%{_libdir}/librxdmath.so.0.0.0
%{_libdir}/librxdmath.so.0
# other hoc files and data
%dir %{_datadir}/%{tarname}
%{_datadir}/%{tarname}/lib

# Python bits
%files -n python3-%{name}
# A data file resides here
%{python3_sitelib}/%{name}
# The libraries are here
%{python3_sitearch}/%{name}
# Egg info
%{python3_sitearch}/NEURON-7.8-py%{python3_version}.egg-info

%files devel
%license Copyright
%doc README.md
%{_bindir}/mkthreadsafe
%{_bindir}/nocmodl
%{_bindir}/nrnivmodl
%{_bindir}/nrnmech_makefile
# Headers
%{_includedir}/*.h
%{_includedir}/nrncvode/
# Shared objects
%{_libdir}/libnrniv.so
%{_libdir}/librxdmath.so

%files doc
%license Copyright
%{_datadir}/%{tarname}/demo

%changelog
* Thu Oct 08 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-4
- Add missing g++ and X dependencies
- Patch to let it correctly find librxdmath

* Thu Oct 08 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-3
- Remove iv header
- disable dynamic build, not needed for Fedora: we support the default python version
- disble hard coded compiler flags

* Fri Sep 04 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-2
- Correct flex dependency
- #1871091

* Tue Aug 18 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.8.1-1
- Update to new release
- Move to cmake build system
- use new cmake out of source build

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-7
- Bump to build in py3.9 side tag

* Thu May 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-6
- Include libtool as Requires for the makefiles
- Reshuffle files for better subpackages

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.7.2-5
- Rebuilt for Python 3.9

* Thu May 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-4
- Update supported architectures

* Thu May 14 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-3
- Add missing BR for neuron-devel
- Move makefiles to -devel sub package

* Wed May 13 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.2-2
- Update description: this is built with iv support.
- Remove unneeded scriptlet
- Fix sed command to modify neuron's make files

* Sun Mar 22 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.7.2-1
- Update to latest version (seems to be just bugfixes)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-12
- Build with iv support

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.7.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 7.7.1-10
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-8
- Enable Python build also

* Sat Jul 13 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-7
- Test a fixed python setup
- https://github.com/neuronsimulator/nrn/issues/238#issuecomment-505191230

* Sun Jun 23 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-6
- Add another patch

* Sun Jun 23 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-5
- Improve patch to install all headers

* Sun Jun 23 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-4
- Install all header files

* Wed Jun 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-3
- Replace patch to inclde required headers

* Wed Jun 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-2
- Remove iv header from nrnconfig file

* Wed Jun 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.7.1-1
- Revert to using release tar
- Use bundled sundials

* Fri May 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-7.20181214git
- Fix file list

* Fri May 17 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-6.20181214git
- Rename oc to hoc to prevent conflict with origin-client binary
- rhbz 1696118

* Sat Mar 02 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-5.20181214git5687519
- Bump and rebuild

* Thu Jan 31 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-4.20181214git5687519
- Remove libtool archives
- Remove stray comment
- Improve previous changelog

* Sun Jan 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-3.20181214git5687519
- Unbundle readline
- Remove readme: only speaks about installation
- Move header to includedir
- Update license
- Remove exec permissions from source files

* Sun Jan 06 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-2.20181214git5687519
- Put each BR on different line
- Remove unneeded comment
- Re-do random123 patch to only modify autotools files
- Remove random123 in prep

* Fri Dec 28 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.5-1.20181214git5687519
- Update to latest git snapshot that uses current sundials
- Build without MPI
