# Bootstrap option, we have to build astrometry before we can generate index
# files, but later package will require them for tests at build time
%global bootstrap 1


Name:           astrometry
Version:        0.78
Release:        8%{?dist}
Summary:        Blind astrometric calibration of arbitrary astronomical images

# Software is BSD with some GPL code
# https://groups.google.com/forum/#!topic/astrometry/9GgP7rj4Y-g
# Here we asked to fix source headers:
# https://groups.google.com/forum/#!topic/astrometry/mCuyze3TOeM
# 
# Licensing breakdown
# ===================
#
# See also: file CREDITS in source folder
#
# General license for astrometry code: 3-clause BSD
#
# GPLv2+:
#    qfits-an/*
#    include/astrometry/qfits*
#    catalogs/ucac4-fits.h
#    libkd/an-fls.h
#    util/makefile.jpeg
#    util/md5.c
#    Makefile
#    doc/UCAC3_guide/* (not used for build and not shipped)
#    doc/UCAC4_guide/* (not used for build and not shipped)
#    
#    2MASS data files index-42xx.fits
#
# GPLv3+:
#    blind/an_mm_malloc.h
#    util/ctmf.c
#
License:        BSD and GPLv2+ and GPLv3+
URL:            http://www.astrometry.net

# Upstream sources contains nonfree stuff so we must clean them
# Download original sources from:
# Source0:        http://astrometry.net/downloads/%%{name}.net-%%{version}.tar.gz
# Then use the provided script to clean them with
# ./generate-tarball %%{version}
Source0:        %{name}.net-%{version}-clean.tar.xz
Source1:        %{name}-generate-tarball.sh

# 2MASS data files, ./astrometry-get-data.sh
Source2:        astrometry-data-4204.tar.xz
Source3:        astrometry-data-4205.tar.xz
Source4:        astrometry-data-4206.tar.xz
Source5:        astrometry-data-4207.tar.xz
Source6:        astrometry-data-4208-4219.tar.xz
Source7:        astrometry-get-data.sh

# Patches from Ole Streicher <olebole@debian.org> used on Debian to
#  * disable build of nonfree stuff removed from sources
#  * have a proper versioned soname
#  * use system libraries properly
#  * use dynamical linking
Patch0:         %{name}-0.73-Add-SONAME-to-libastrometry.so.patch
Patch1:         %{name}-Dynamically-link-to-libastrometry.so-when-possible.patch
Patch2:         %{name}-Fix-issues-when-using-Debian-libs-instead-of-convienience.patch
Patch3:         %{name}-Call-python-scripts-as-modules-instead-of-executables.patch
Patch4:         %{name}-0.73-Don-t-install-non-free-files-images-and-NGC2000.0-catalog.patch

BuildRequires:  gcc
BuildRequires:  netpbm-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-astropy
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  xorg-x11-proto-devel

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)

%if ! 0%{?bootstrap}
BuildRequires:  astrometry-tycho2
%endif

Requires:       %{name}-data = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       netpbm-progs
Requires:       python3-%{name} = %{version}-%{release}

# User could use own set of index files or another set from upstream.
# Therefore we suggest and not require astrometry-tycho2 here
Suggests:     astrometry-tycho2

# FIXME
# Kill s390x build for now, s390x build seems unknown
# "cpio: read failed - Inappropriate ioctl for device" error
# when unpacking srpm
ExcludeArch:	s390x

%description
The astrometry engine will take any image and return the astrometry
world coordinate system (WCS), a standards-based description of the
transformation between image coordinates and sky coordinates.

Other tools included in the astrometry package can do much more, like
plotting astronomic information over solved images, convertion utilities
or generate statistics from FITS images.


%package data
Summary:        2MASS catalog index files for astrometry (4208-4129, wide-field)
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-data-4208-4219 = %{version}-%{release}

%description data
2MASS index files 4208-4219 (wide-field, 30-2000 arcminutes) for astrometry.


%package data-4204
Summary:        2MASS catalog index files (4204 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4204
2MASS index files (4204 series) with 8-11 arcminutes skymarks for astrometry.


%package data-4205
Summary:        2MASS catalog index files (4205 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4205
2MASS index files (4205 series) with 11-16 arcminutes skymarks for astrometry.


%package data-4206
Summary:        2MASS catalog index files (4206 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4206
2MASS index files (4206 series) with 16-22 arcminutes skymarks for astrometry.


%package data-4207
Summary:        2MASS catalog index files (4207 series) for astrometry
License:        GPLv2+
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Enhances:       %{name}

%description data-4207
2MASS index files (4207 series) with 22-30 arcminutes skymarks for astrometry.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%package libs
Summary:        Libraries for %{name}

%description libs
Libraries for %{name}

%package -n python3-%{name}
Summary:        Python modules from %{name}
Requires:       python3-astropy
Provides:       %{name}-python2 = %{version}-%{release}
Obsoletes:      %{name}-python2 < %{version}-%{release}
Provides:       python2-%{name} = %{version}-%{release}
Obsoletes:      python2-%{name} < %{version}-%{release}

%description -n python3-%{name}
%{summary}


%prep
%autosetup -p1 -n %{name}.net-%{version}
%setup -T -D -a 2 -n %{name}.net-%{version}
%setup -T -D -a 3 -n %{name}.net-%{version}
%setup -T -D -a 4 -n %{name}.net-%{version}
%setup -T -D -a 5 -n %{name}.net-%{version}
%setup -T -D -a 6 -n %{name}.net-%{version}

# Fix Wrong FSF address - reported upstream
# https://groups.google.com/forum/#!topic/astrometry/mCuyze3TOeM
grep -rl '59 Temple Place, Suite 330, Boston, MA  02111-1307  USA' * | xargs -i@ sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA./g' @


%build
# Weird symlink required... (also in upstream git)
ln -sf . astrometry

# Astrometry doesn't automatically find netpbm
export NETPBM_INC=-I%{_includedir}/netpbm
export NETPBM_LIB="-L%{_libdir} -lnetpbm"

# Apply mandatory ld flags
export LDFLAGS="%__global_ldflags"

# We use Python3 here
export PYTHON=%{__python3}
# Parallel make flags on break build
make SYSTEM_GSL=yes all py extra ARCH_FLAGS="%{optflags}"


%install
export PYTHON=%{__python3}
%{make_install} SYSTEM_GSL=yes \
                INSTALL_DIR=%{buildroot}%{_prefix} \
                PY_BASE_INSTALL_DIR=%{buildroot}%{python3_sitearch}/%{name} \
                INCLUDE_INSTALL_DIR=%{buildroot}%{_includedir}/%{name} \
                LIB_INSTALL_DIR=%{buildroot}%{_libdir} \
                BIN_INSTALL_DIR=%{buildroot}%{_bindir} \
                DATA_INSTALL_DIR=%{buildroot}%{_datadir}/%{name}/data \
                PY_BASE_LINK_DIR=%{python3_sitearch}/%{name} \
                ETC_INSTALL_DIR=%{buildroot}%{_sysconfdir} \
                MAN1_INSTALL_DIR=%{buildroot}%{_mandir}/man1 \
                DOC_INSTALL_DIR=%{buildroot}%{_docdir}/%{name} \
                EXAMPLE_INSTALL_DIR=%{buildroot}%{_datadir}/%{name}/examples

# We need to correct the data dir link in config file
sed -i \
    "s:%{buildroot}%{_prefix}/data:%{_datadir}/%{name}/data:" \
    %{buildroot}/etc/astrometry.cfg

# Rename generic named executables with known conflict
pushd %{buildroot}%{_bindir}
for exec in tabmerge tablist; do
        mv $exec astrometry-$exec
done
popd

# Remove unuseful file
rm -f %{buildroot}%{_docdir}/%{name}/report.txt

# We don't ship static libraries so we remove them
rm -f %{buildroot}%{_libdir}/*.a

# Fix wrong python interpreter
pushd %{buildroot}%{_bindir}
for exec in degtohms image2pnm removelines text2fits hmstodeg votabletofits uniformize merge-columns; do
        sed -i "s,/usr/bin/env python,%{__python3},g" $exec
done
popd
find %{buildroot}/%{python3_sitearch}/%{name} -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

# LICENSE file is managed by %%license scriptlet
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

# Install data files
install -m0644 astrometry-data*/*.fits %{buildroot}%{_datadir}/%{name}/data

%check
export PYTHON=%{__python3}
make test ARCH_FLAGS="%{optflags}"


%ldconfig_scriptlets libs


%files
%doc CREDITS README.md
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*
%exclude %{_bindir}/*.py
%dir %{_datadir}/astrometry
%dir %{_datadir}/astrometry/data
%{_datadir}/astrometry/examples
%config(noreplace) %{_sysconfdir}/astrometry.cfg

%files data
%license astrometry-data-4208-4219/LICENSE
%{_datadir}/astrometry/data/index-4208.fits
%{_datadir}/astrometry/data/index-4209.fits
%{_datadir}/astrometry/data/index-421*.fits

%files data-4204
%license astrometry-data-4204/LICENSE
%{_datadir}/astrometry/data/index-4204*.fits

%files data-4205
%license astrometry-data-4205/LICENSE
%{_datadir}/astrometry/data/index-4205*.fits

%files data-4206
%license astrometry-data-4206/LICENSE
%{_datadir}/astrometry/data/index-4206*.fits

%files data-4207
%license astrometry-data-4207/LICENSE
%{_datadir}/astrometry/data/index-4207*.fits

%files devel
%{_includedir}/*
%{_libdir}/*.so

%files libs
%license LICENSE
%{_libdir}/*.so.*

%files -n python3-%{name}
%{python3_sitearch}/*
%{_bindir}/*.py

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.78-7
- Rebuilt for Python 3.9

* Wed Mar 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.78-6
- Rebuild for new wcslib

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.78-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.78-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.78-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 0.78-1
- new version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.76-1
- new version

* Mon Jul 16 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.75-2
- Dependency fix, require python3-astrometry, not python2-astrometry

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.75-1
- new version

* Sat Jul 14 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.74-3
- Switch to Python 3
- BuildRequires: gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.74-1
- new version

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.73-5
- rebuilt for cfitsio 3.450

* Sat Feb 24 2018 Christian Dersch <lupinix@mailbox.org> - 0.73-4
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.73-3
- rebuilt

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Christian Dersch <lupinix@mailbox.org> - 0.73-1
- new version

* Tue Oct 17 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-4
- Added subpackages for 4204-4207 index files

* Mon Oct 16 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-3
- Added data subpackage containing the wide-field 2MASS indices

* Mon Sep 25 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-2
- Move libs to subpackage to be multiarch compatible

* Tue Sep 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-1
- Initial SCM import (#1470436)

* Wed Jul 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.72-0.1
- initial spec (using the packaging effort from Mattia Verga, RHBZ  #1299139)

