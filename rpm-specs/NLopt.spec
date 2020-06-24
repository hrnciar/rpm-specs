# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# Conditionals controlling the build.
%global with_guile	1
%global with_octave	1
%if (0%{?fedora} && 0%{?fedora} < 30) || 0%{?rhel} == 7
%global with_py		1
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
%global with_py3	1
%endif

# Settings used for build from snapshots.
%{!?rel_build:%global commit		96ebb33c3143de3e050e040e1fd11c6ee9055471}
%{!?rel_build:%global commit_date	20180831}
%{!?rel_build:%global shortcommit	%(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global gitver		git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global gitrel		.git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global gittar		%{name}-%{version}-%{gitver}.tar.gz}

# Get a lowercase name for virtual provides.
%define lc_name %(echo %{name} | tr '[:upper:]' '[:lower:]')

Name:			NLopt
Version:		2.6.2
Release:		1%{?gitrel}%{?dist}
Summary:		Open-Source library for nonlinear optimization

# The detailed license-breakdown of the sources is:
#
# BSD (2 clause)
# --------------
# util/mt19937ar.c
#
#
# BSD (3 clause)
# --------------
# slsqp/*
#
#
# LGPL (v2 or later)
# ------------------
# luksan/*
#
# MIT/X11 (BSD like)
# ------------------
# api/*		auglag/*	bobyqa/*	cdirect/*	cobyla/*
# cquad/*	crs/*		direct/*	esch/*		isres/*
# mlsl/*	mma/*		neldermead/*	newuoa/*	octave/*
# stogo/*	tensor/*	test/*		util/* (ex. util/mt19937ar.c)
#
#
# Public Domain
# -------------
# praxis/*	subplex/*
#
License:		BSD and LGPLv2+ and MIT and Public Domain
URL:			http://ab-initio.mit.edu/%{lc_name}
%{?rel_build:Source0:	https://github.com/stevengj/%{lc_name}/archive/v%{version}/%{lc_name}-%{version}.tar.gz}
%{!?rel_build:Source0:	https://github.com/stevengj/%{lc_name}/archive/%{commit}/%{gittar}}

BuildRequires:		cmake
BuildRequires:		ncurses-devel

# The "gnulib" is a copylib and has a wildcard-permission from FPC.
# See: https://fedorahosted.org/fpc/ticket/174
Provides:		bundled(gnulib)
Provides:		%{lc_name}			=  %{version}-%{release}
Provides:		%{lc_name}%{?_isa}		=  %{version}-%{release}

%description
NLopt is a library for nonlinear local and global optimization, for
functions with and without gradient information.  It is designed as
as simple, unified interface and packaging of several free/open-source
nonlinear optimization libraries.

It features bindings for GNU Guile, Octave and Python.  This build has
been made with C++-support enabled.


%package devel
Summary:		Development files for %{name}

Requires:		%{name}%{?_isa}			=  %{version}-%{release}

Provides:		%{lc_name}-devel		=  %{version}-%{release}
Provides:		%{lc_name}-devel%{?_isa}	=  %{version}-%{release}

%description devel
This package contains development files for %{name}.


%package doc
Summary:		Documentation files for %{name}
BuildArch:	        noarch
Provides:		%{lc_name}-doc			=  %{version}-%{release}

%description doc
This package contains documentation files for %{name}.


%if 0%{?with_guile}
%package -n guile-%{name}
# For compatibility with RHEL <= 6.
%{!?guile_pkgconf:%global guile_pkgconf %(pkg-config --list-all | grep guile | sed -e 's! .*$!!g')}
%{!?guile_sitedir:%global guile_sitedir %(pkg-config --variable=sitedir %{guile_pkgconf})}

Summary:		Guile bindings for %{name}

BuildRequires:		guile-devel
BuildRequires:		pkgconfig
BuildRequires:		swig

Requires:		guile%{?_isa}
Requires:		%{name}%{?_isa}			=  %{version}-%{release}

Provides:		guile-%{lc_name}		=  %{version}-%{release}
Provides:		guile-%{lc_name}%{?_isa}	=  %{version}-%{release}

%description -n guile-%{name}
This package contains Guile bindings for %{name}.
%endif


%if 0%{?with_octave}
%package -n octave-%{name}
%global octpkg %{name}
# For compatibility with RHEL <= 6.
%{!?octave_api:		%global octave_api	%(octave-config -p API_VERSION || echo 0)}
%{!?octshareprefix:	%global octshareprefix	%{_datadir}/octave}
%{!?octprefix:		%global octprefix	%{octshareprefix}/packages}
%{!?octarchprefix:	%global octarchprefix	%{_libdir}/octave/packages}
%{!?octpkgdir:		%global octpkgdir	%{octshareprefix}/%{octpkg}-%{version}}
%{!?octpkglibdir:	%global octpkglibdir	%{octarchprefix}/%{octpkg}-%{version}}

Summary:		Octave bindings for %{name}

BuildRequires:		octave-devel

Requires:		%{name}%{?_isa}			=  %{version}-%{release}
Requires:		octave(api)			=  %{octave_api}
Requires(post):		octave
Requires(postun):	octave

Provides:		octave-%{lc_name}		=  %{version}-%{release}
Provides:		octave-%{lc_name}%{?_isa}	=  %{version}-%{release}

%description -n octave-%{name}
This package contains the Octave bindings for %{name}.
%endif


%if 0%{?with_py}
%package -n python2-nlopt
%{?python_provide:%python_provide python2-nlopt}
Summary:		Python bindings for %{name}

BuildRequires:		numpy
BuildRequires:		python2-devel

Requires:		%{name}%{?_isa}			=  %{version}-%{release}

Provides:		python-%{lc_name}		=  %{version}-%{release}
Provides:		python-%{lc_name}%{?_isa}	=  %{version}-%{release}

%description -n python2-nlopt
This package contains Python bindings for %{name}.
%endif


%if 0%{?with_py3}
%package -n python%{python3_pkgversion}-%{name}
Summary:		Python3 bindings for %{name}

BuildRequires:		python%{python3_pkgversion}-devel
BuildRequires:		python%{python3_pkgversion}-numpy

Requires:		%{name}%{?_isa}			=  %{version}-%{release}

Provides:		python%{python3_pkgversion}-%{lc_name}		=  %{version}-%{release}
Provides:		python%{python3_pkgversion}-%{lc_name}%{?_isa}	=  %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
This package contains Python3 bindings for %{name}.
%endif

%global sourcedir %{!?rel_build:%{lc_name}-%{commit}}%{?rel_build:%{lc_name}-%{version}}

%prep
%setup -qcn %{sourcedir}
pushd %{sourcedir}

# Move all %%doc to topdir and append their belonging.
[[ -f README.md ]] &&								\
mv -f README.md README
_topdir="`pwd`"
for _dir in `find . -type d |							\
	sed -e "/\.libs/d" -e "s/\.\///g" -e "/\./d" | sort -u`
do
  pushd ${_dir}
  for _file in 'AUTHOR*' 'COPY*' 'README*' '*[Pp][Dd][Ff]'
  do
    for _doc in `find . -name "${_file}" -maxdepth 1`
    do
      mv -f ${_doc} ${_topdir}/${_doc}.`echo ${_dir} | sed -e "s/\//_/g"`
    done
  done
  popd
done

popd

# Bootstrapping once before we create a copy in _python3
#touch swig/nlopt.scm.in

%if 0%{?with_py3}
# Creating a copy for building the Python3-plugin.
cp -a %{sourcedir} _python3
%endif


%build
%if 0%{?fedora} || 0%{?rhel} >= 7
export CFLAGS="%{optflags} -fpermissive"
export CXXFLAGS="%{optflags} -fpermissive"
%endif

pushd %{sourcedir}
%cmake				    \
%if 0%{?with_py}
 -DPYTHON_EXECUTABLE=%{__python2}   \
%endif
 -DINSTALL_M_DIR=%{octpkgdir}    \
 -DINSTALL_OCT_DIR=%{octpkglibdir}  \
 .

# Parallel-build might fail because of some race-condition
#make %{?_smp_mflags}
%make_build
popd

%if 0%{?with_py3}
pushd _python3
%cmake 			            \
%if 0%{?with_py3}
 -DPYTHON_EXECUTABLE=%{__python3}   \
%endif
 -DINSTALL_M_DIR=%{octpkgdir}    \
 -DINSTALL_OCT_DIR=%{octpkglibdir}  \
 .

# Parallel-build might fail because of some race-condition
#make %{?_smp_mflags}
%make_build
%endif


%install
pushd %{sourcedir}
%make_install
popd

%if 0%{?with_py3}
pushd _python3
%make_install
popd
%endif

# We don't want these static-libs and libtool-dumplings
find %{buildroot} -depth -name '*.*a' -print0 | xargs -0 rm -f

%if 0%{?with_octave}
# Setup octave stuff properly.
mkdir -p %{buildroot}%{octpkgdir}/packinfo
chmod 0755 %{buildroot}%{octpkglibdir}/*.oct
install -pm 0644 %{sourcedir}/COPYING %{buildroot}%{octpkgdir}/packinfo

cat > %{buildroot}%{octpkgdir}/packinfo/DESCRIPTION << EOF
Name: %{name}
Version: %{version}
Date: %(date +%Y-%m-%d)
Author: Steven G. Johnson <stevenj@alum.mit.edu>
Maintainer: Björn Esser <besser82@fedoraproject.org>
Title: Open-Source library for nonlinear optimization
Description: NLopt is a library for nonlinear local and global
 optimization, for functions with and without gradient information.
 It is designed as as simple, unified interface and packaging of
 several free/open-source nonlinear optimization libraries.
Url: %{url}
EOF

cat > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m << EOF
function on_uninstall (desc)
  error ('Can not uninstall %s installed by the redhat package manager', desc.name);
endfunction
EOF
%endif


%check
pushd %{sourcedir}/test
ctest -V .
popd

%if 0%{?with_py3}
pushd _python3/test
ctest -V .
popd
%endif


%ldconfig_scriptlets

%if 0%{?with_octave}
%if 0%{?fedora} || 0%{?rhel} >= 7
%post -n octave-%{name}
%octave_cmd pkg rebuild

%preun -n octave-%{name}
%octave_pkg_preun

%postun -n octave-%{name}
%octave_cmd pkg rebuild
%else
%post -n octave-%{name}
octave -H -q --no-window-system --no-site-file --eval "pkg rebuild"

%preun -n octave-%{name}
rm -f %{octpkgdir}/packinfo/on_uninstall.m
if [ -e %{octpkgdir}/packinfo/on_uninstall.m.orig ]
then
  mv -f %{octpkgdir}/packinfo/on_uninstall.m.orig %{octpkgdir}/packinfo/on_uninstall.m
  cd %{octpkgdir}/packinfo
  octave -H -q --no-window-system --no-site-file --eval "l=pkg('list');on_uninstall(l{cellfun(@(x)strcmp(x.name,'%{octpkg}'),l)});"
fi

%postun -n octave-%{name}
octave -H -q --no-window-system --no-site-file --eval "pkg rebuild"
%endif
%endif

%files
%doc %{sourcedir}/ChangeLog %{sourcedir}/COPY* %{sourcedir}/NEWS.md
%{_libdir}/lib%{lc_name}.so.*

%files devel
%doc %{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/cmake/nlopt/
%{_libdir}/lib%{lc_name}.so
%{_libdir}/pkgconfig/%{lc_name}.pc

%files doc
%doc %{sourcedir}/AUTHOR* %{sourcedir}/ChangeLog %{sourcedir}/COPY* %{sourcedir}/NEWS.md
%doc %{sourcedir}/README* %{sourcedir}/TODO %{sourcedir}/*.[Pp][Dd][Ff].*

%if 0%{?with_guile}
%files -n guile-%{name}
%{_libdir}/guile/2.0/extensions/*nlopt_guile.so
%{guile_sitedir}/*
%endif

%if 0%{?with_octave}
%files -n octave-%{name}
%{octpkglibdir}
%{octpkgdir}
%endif

%if 0%{?with_py}
%files -n python2-nlopt
%{python2_sitearch}/*
%endif

%if 0%{?with_py3}
%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/*.so*
%{python3_sitearch}/*.py*
%{python3_sitearch}/__pycache__/*.py*
%endif

%changelog
* Sun May 31 2020 Björn Esser <besser82@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 2.6.1-5
- Rebuild with octave 64bit indexes

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-1
- Update to 2.6.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-1
- Update to 2.5.0, uses cmake
- Rebuild for octave 4.4

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-18
- Remove Python 2 subpackage on Fedora 30+ (#1627303)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-16
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.2-14
- Python 2 binary package renamed to python2-nlopt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-10
- Rebuild for Python 3.6

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-9
- Rebuild for octave 4.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-5
- Rebuild for octave 4.0
- Add patch for octave 4.0 support

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.2-2
- disable octave-subpkg on el7

* Thu Jul 17 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.2-1
- new upstream release (#1116586)
- adapted spec to use named conditionals for packages

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 14 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-5
- fixed description-file for octave-NLopt (#1048510)

* Tue Jan 14 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-4
- fixed nlopt.pc to reflect the correct lib to link against

* Sat Dec 28 2013 Kevin Fenzi <kevin@scrye.com> - 2.4.1-3
- Rebuild to fix broken deps

* Sat Dec 28 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-2
- rebuild for octave-3.8.0-rc2

* Fri Dec 20 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-1
- new upstream release: v2.4.1
- adapted %%{source0} to match %%{name}
- changed `%%global lc_name` to `%%define lc_name`, because of globbing problems
- use `tr` instead of shell-builtin for `%%define lc_name`
- move `README.md` only if existing
- create an empty Makefile on el5 instead of modifying top-level Makefile.am
- do not autoreconf on el5
- append `-fpermissive` to C[XX]FLAGS on Fedora 19+

* Fri Dec 20 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4-3.git20130903.35e6377
- made %%clean-target conditional on el5
- restructured spec-file for quick switching between snapshot and release
- moved package-specific macros to the corresponding subpackage

* Wed Oct 02 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4-2.git20130903.35e6377
- adaptions for new Python-guidelines

* Thu Sep 19 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4-1.git20130903.35e6377
- Initial rpm release (#1004209)
