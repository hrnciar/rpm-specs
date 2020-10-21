# avoid providing the private libs:
%global __provides_exclude_from ^(%{python3_sitearch})/.*\\.so.*$

# use grib_api for i686, ppc64, s390x. armv7hl
# and eccodes for the other archs since eccodes
# does not yet build for these 4 archs.
%ifarch i686 ppc64 s390x armv7hl
  %global use_eccodes 0
%else
  %global use_eccodes 1
%endif

Name:       pygrib
Version:    2.0.4
Release:    7%{?dist}
Summary:    Python module for reading and writing GRIB (editions 1 and 2) files

License:    MIT
URL:        https://github.com/jswhit/%{name}
Source0:    https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

# Adapt setup.py to not use packaged g2clib source code
Patch0: %{name}-%{version}-build.patch

# general BR
# note: build requires are global for the whole spec file
#       but the python BR packages have been sorted anyway for readibility
BuildRequires: gcc
%if 0%{?use_eccodes}
BuildRequires: eccodes-devel
%else
BuildRequires: grib_api-devel
%endif
BuildRequires: g2clib-static
BuildRequires: openjpeg-devel
BuildRequires: python3-numpy

# a note on the build requirements:
# pygrib installation instructions mention these requirements:
#    $GRIBAPI_DIR, $JASPER_DIR, $OPENJPEG_DIR, $PNG_DIR and $ZLIB_DIR 
# (see https://jswhit.github.io/pygrib/docs/index.html)
#
# grib_api-devel is mentioned above.
# g2clib-devel is included in the pygrib sources, but has been removed
# to comply to Fedora policy, so has been added as requirement
# jasper-devel is BR by grib_api-devel
# libpng-devel and jasper-devel are BR for g2clib-devel
# jasper-devel BRs libjpeg-devel and others
# libpng-devel BRs zlib-devel
# However, pygrib does not need header files from these packages
# during the build, therefore no explicit BuildRequires is needed
# for jasper, openjpeg, png or zlib
#
# in addition python3-pyproj has been added as BR
# below since it is needed to run the test.py script in the check stage 

%global _description \
Cython wrapper to provide python interfaces to the grib library. \
 \
GRIB is the the World Meteorological Organization (WMO) standard for \
distributing gridded data. This module contains python interfaces for reading \
and writing GRIB data using the ECMWF GRIB API C library, and the NCEP GRIB2 \
C library, as well as command-line utilities for listing and re-packing GRIB \
files. 

%description %_description

%package -n python3-%{name}

Summary: %summary

# python3 specific
BuildRequires: python3-devel
BuildRequires: python3-numpy
BuildRequires: python3-Cython
BuildRequires: python3-pyproj

# this requirement is not automatically resolved and needs to be
# inserted manually (see bug #996834)
%if 0%{?use_eccodes}
Requires:  eccodes
%else
Requires:  grib_api
%endif

Requires:  python3-pyproj

# specifying this is not needed. rpmbuild figures it out without help
# Requires: jasper-libs openjpeg-libs libpng zlib

# ensure python provides are provided when python3 becomes the default runtime
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name} %_description

%prep
%setup -q
%patch0 -p0 -b .build

# Delete g2clib sources
rm -rf g2clib_src

# Delete precooked cython *.c files
rm  g2clib.c
rm  pygrib.c
rm  redtoreg.c

# running cython is taken care of by the setup.py
# file now, so no explicit calls are needed anymore

%build

%if 0%{?use_eccodes}
# nothing to do since v2.0.3
%else
cp setup.cfg.template setup.cfg
echo "grib_api_libname = grib_api" >> setup.cfg
%endif

# TODO: move the next 2 exports to setup.cfg
export JASPER_DIR="%{_usr}/"
export PNG_DIR="%{_usr}/"

%if 0%{?use_eccodes}
# nothing to do since v2.0.3
%else
cp setup.cfg.template setup.cfg
echo "grib_api_libname = grib_api" >> setup.cfg
%endif

%py3_build

%install

# this setting triggers installation of man pages by the setup.py file
export MAN_DIR=/usr/share/man/

%py3_install

# correct wrong write permission for group
chmod 755  %{buildroot}/%{python3_sitearch}/*.so

%check

export PYTHONPATH=%{buildroot}/%{python3_sitearch}
%{__python3} test.py

%files -n python3-%{name}
%doc COPYING PKG-INFO README.md
%doc docs ncepgrib2_docs
%{python3_sitearch}/*.so
%{python3_sitearch}/ncep*.py*
%{python3_sitearch}/__pycache__/ncep*.py*
%{python3_sitearch}/%{name}-*-py*.egg-info
%{_bindir}/cnv*
%{_bindir}/grib_*
%{_mandir}/man1/cnv*
%{_mandir}/man1/grib_*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Jos de Kloe <josdekloe@gmail.com> 2.0.4-1
- update to new upstream version 2.0.4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Jos de Kloe <josdekloe@gmail.com> 2.0.3-2
- remove python2 sub-package as per Mass Python 2 Package Removal for f30

* Fri Aug 24 2018 Jos de Kloe <josdekloe@gmail.com> 2.0.3-1
- update to new upstream version 2.0.3

* Fri Aug 17 2018 Jos de Kloe <josdekloe@gmail.com> 2.0.2-17
- merge with cython patch by Miro Hrončok <pagure@pkgs.fedoraproject.org>
  (there is no more cython3, use the -m syntax)

* Thu Aug 02 2018 Jos de Kloe <josdekloe@gmail.com> - 2.0.2-16
- Build using eccodes for those architectures that provide it

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-14
- Rebuilt for Python 3.7

* Thu Feb 15 2018 Jos de Kloe <josdekloe@gmail.com> - 2.0.2-13
- Rebuild after mass rebuild caused dependency troubles

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Jos de Kloe <josdekloe@gmail.com> 2.0.2-11
- Adapt to changed name of g2c static library

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Jos de Kloe <josdekloe@gmail.com> 2.0.2-8
- reorganize spec file (following pyproj) example to ensure
  Requires are used for the right sub-package, and added optflags

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0.2-7
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Jun 30 2017 Jos de Kloe <josdekloe@gmail.com> 2.0.2-6
- rename pygrib to python2-pygrib following the new package naming scheme

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuild for Python 3.6

* Sat Dec 3 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.2-3
- force a rebuild, needed due to libjasper so version bump

* Sat Nov 26 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.2-2
- fix mistake in patch for setup.py file that caused python3 package
  to provide python2 version tools

* Sun Nov 20 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.2-1
- update to new upstream version
- provide tools below /usr/bin for python3 in stead of python2
- move to new predictable pypi source location
- add python_provide macros

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Jos de Kloe <josdekloe@gmail.com> 2.0.1-1
- update to new upstream version

* Sun Nov 15 2015 Jos de Kloe <josdekloe@gmail.com> 2.0.0-5
- update patch pygrib-2.0.0-g2clib.pyx.patch and add a new
  pygrib-2.0.0-pygrib.pyx.patch to adapt to stricter
  variable type checking of cython
  
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jul 15 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-3
- Rebuild for grib_api 1.14.0 soname bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Jos de Kloe <josdekloe@gmail.com> 2.0.0-1
- update to upstream version 2.0.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 09 2014 Jos de Kloe <josdekloe@gmail.com> 1.9.9-2
- move requires for python3-pyproj above description section

* Sat Jul 05 2014 Jos de Kloe <josdekloe@gmail.com> 1.9.9-1
- update to upstream version 1.9.9
- replace python_sitearch macro with python2_sitearch
- activate installation of the newly added man pages
- fix requires problem for python3-pyproj
- update url for Source0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Oct 26 2013 Jos de Kloe <josdekloe@gmail.com> 1.9.7-1
- update to upstream version 1.9.7

* Fri Aug 23 2013 Jos de Kloe <josdekloe@gmail.com> 1.9.6-1
- update to upstream version 1.9.6
  and move to use grib_api-devel as BR as suggested by Orion Poplawski
  on devel mailinglist on 23-Aug-2013

* Wed Aug 14 2013 Jos de Kloe <josdekloe@gmail.com> 1.9.5-4
- add an explicit requirement on grib_api

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Nov 22 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.5-2
- adapt to build with python3 as well
- fix typo in weekdays in dates of changelog entries 1.9.2-1 and 1.9.4-1

* Thu Nov 08 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.5-1
- update to upstream version 1.9.5
- add the doc files to the files list
- activate the check section

* Sat Sep 08 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.4-3
- remove BR of grib_api-devel and g2clib-devel and some textual 
  changes in the comments

* Wed Aug 29 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.4-2
- address comments 3 and 4 in bugzilla review request 806037

* Thu Aug 23 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.4-1
- move to version 1.9.4 and fix a bunch of rpmlint warnings

* Sun Mar 18 2012 Jos de Kloe <josdekloe@gmail.com> 1.9.2-1
- initial version
