%if %{?rhel}%{!?rhel:0} == 6
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
%endif

%if %{?fedora}%{!?fedora:0} >= 30
# Don't build Python 2 package for Fedora >= 30
%global buildpy2 0
%else
%global buildpy2 1
%endif

Name:		pythia8
Version:	8.2.43
Release:	6%{?dist}
Summary:	Pythia Event Generator for High Energy Physics

License:	GPLv2+
URL:		http://home.thep.lu.se/~torbjorn/Pythia.html
Source0:	http://home.thep.lu.se/~torbjorn/pythia8/pythia8243.tgz
#		Link plugins to the shared library
#		Remove rpath
Patch0:		%{name}-makefile.patch

BuildRequires:	lhapdf-devel
BuildRequires:	zlib-devel
BuildRequires:	gcc-c++
%if %{?rhel}%{!?rhel:0} == 6
BuildRequires:	gcc-gfortran
%endif
%if %{buildpy2}
BuildRequires:	python2-devel
%endif
BuildRequires:	python%{python3_pkgversion}-devel
%if %{?rhel}%{!?rhel:0} == 7
BuildRequires:	python%{python3_other_pkgversion}-devel
%endif
BuildRequires:	rsync
BuildRequires:	dos2unix
Requires:	%{name}-data = %{version}-%{release}
Obsoletes:	%{name}-hepmcinterface < 8.2
%if ! %{buildpy2}
Obsoletes:	python2-%{name} < %{version}-%{release}
%endif

%description
PYTHIA is a program for the generation of high-energy physics events, i.e.
for the description of collisions at high energies between elementary
particles such as e⁺, e⁻, p and p̄ in various combinations. It contains
theory and models for a number of physics aspects, including hard and soft
interactions, parton distributions, initial and final-state parton showers,
multiple interactions, fragmentation and decay.

%package devel
Summary:	Pythia 8 Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-hepmcinterface-devel < 8.2

%description devel
This package provides development files for Pythia 8.

%package lhapdf
Summary:	Pythia 8 LHAPDF Interface
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description lhapdf
This package provides the LHAPDF interface for Pythia 8.

%if %{buildpy2}
%package -n python2-%{name}
Summary:	Pythia 8 Python 2 bindings
%{?python_provide:%python_provide python2-%{name}}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python2-%{name}
This package provides the Python 2 bindings for Pythia 8.
%endif

%package -n python%{python3_pkgversion}-%{name}
Summary:	Pythia 8 Python 3 bindings
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
This package provides the Python 3 bindings for Pythia 8.

%if %{?rhel}%{!?rhel:0} == 7
%package -n python%{python3_other_pkgversion}-%{name}
Summary:	Pythia 8 Python 3 bindings
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{name}}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python%{python3_other_pkgversion}-%{name}
This package provides the Python 3 bindings for Pythia 8.
%endif

%package data
Summary:	Pythia 8 Data Files
BuildArch:	noarch

%description data
This package provides XML data files for Pythia 8.

%package examples
Summary:	Pythia 8 Example Source Files
BuildArch:	noarch

%description examples
This package provides example source files for Pythia 8.

%package doc
Summary:	Pythia 8 Documentation
BuildArch:	noarch

%description doc
This package provides documentation for Pythia 8.

%prep
%setup -q -n pythia8243
%patch0 -p1

# Remove DOS end-of-line
dos2unix -k share/Pythia8/htmldoc/pythia.css \
	    share/Pythia8/phpdoc/pythia.css \
	    share/Pythia8/xmldoc/mrstlostarstar.00.dat

# Remove junk
find . -name '._*' -exec rm {} ';'

%build
./configure --prefix=%{_prefix} --prefix-lib=%{_libdir} \
	    --cxx-common="%{optflags} -fPIC" \
	    --cxx-shared="%{?__global_ldflags} -Wl,-z,defs -shared" \
	    --lib-suffix="-%{version}.so" \
	    --enable-shared \
%if %{?rhel}%{!?rhel:0} == 6
	    --with-lhapdf5 \
%else
	    --with-lhapdf6 \
%endif
	    --with-gzip
make %{?_smp_mflags}
ln -s libpythia8-%{version}.so lib/libpythia8.so

make lib/pythia8.py PYTHON_BIN='#'
mv lib/pythia8.py .

%if %{?fedora}%{!?fedora:0} >= 30
%ifarch %{arm}
# Reduce memory usage during compilation of the python module on 32 bit arm
MEMSAVE=-g1
%endif
%endif

%if %{buildpy2}
mkdir py2
if pkg-config --exists python2 ; then
    PY2INC=$(pkg-config --cflags python2)
    PY2LIB=$(pkg-config --libs python2)
else
    PY2INC=-I/usr/include/python%{python2_version}
    PY2LIB=-lpython%{python2_version}
fi
g++ -x c++ include/Pythia8Plugins/PythonWrapper.h -c -o py2/PythonWrapper.o \
    ${PY2INC} -Iinclude %{optflags} -fPIC -DGZIPSUPPORT $MEMSAVE
g++ py2/PythonWrapper.o -Llib -lpythia8 -o py2/_pythia8.so \
    ${PY2LIB} -ldl %{?__global_ldflags} -Wl,-z,defs -shared
%endif

mkdir py3
if pkg-config --exists python3-embed ; then
    PY3INC=$(pkg-config --cflags python3-embed)
    PY3LIB=$(pkg-config --libs python3-embed)
else
    PY3INC=$(pkg-config --cflags python3)
    PY3LIB=$(pkg-config --libs python3)
fi
PY3SOABI=$(%{__python3} -c "from distutils import sysconfig; print(sysconfig.get_config_vars().get('SOABI'))")
g++ -x c++ include/Pythia8Plugins/PythonWrapper.h -c -o py3/PythonWrapper.o \
    ${PY3INC} -Iinclude %{optflags} -fPIC -DGZIPSUPPORT $MEMSAVE
g++ py3/PythonWrapper.o -Llib -lpythia8 -o py3/_pythia8.${PY3SOABI}.so \
    ${PY3LIB} -ldl %{?__global_ldflags} -Wl,-z,defs -shared

%if %{?rhel}%{!?rhel:0} == 7
mkdir py3oth
if pkg-config --exists python-%{python3_other_version}-embed ; then
    PY3INC=$(pkg-config --cflags python-%{python3_other_version}-embed)
    PY3LIB=$(pkg-config --libs python-%{python3_other_version}-embed)
else
    PY3INC=$(pkg-config --cflags python-%{python3_other_version})
    PY3LIB=$(pkg-config --libs python-%{python3_other_version})
fi
PY3SOABI=$(%{__python3_other} -c "from distutils import sysconfig; print(sysconfig.get_config_vars().get('SOABI'))")
g++ -x c++ include/Pythia8Plugins/PythonWrapper.h -c -o py3oth/PythonWrapper.o \
    ${PY3INC} -Iinclude %{optflags} -fPIC -DGZIPSUPPORT
g++ py3oth/PythonWrapper.o -Llib -lpythia8 -o py3oth/_pythia8.${PY3SOABI}.so \
    ${PY3LIB} -ldl %{?__global_ldflags} -Wl,-z,defs -shared
%endif

%install
make %{?_smp_mflags} install \
     PREFIX_BIN=%{buildroot}%{_bindir} \
     PREFIX_INCLUDE=%{buildroot}%{_includedir} \
     PREFIX_LIB=%{buildroot}%{_libdir} \
     PREFIX_SHARE=%{buildroot}%{_datadir}/Pythia8

rm %{buildroot}%{_bindir}/pythia8-config
rm %{buildroot}%{_libdir}/libpythia8.a
rm -rf %{buildroot}%{_datadir}/Pythia8/htmldoc
rm -rf %{buildroot}%{_datadir}/Pythia8/pdfdoc
rm -rf %{buildroot}%{_datadir}/Pythia8/phpdoc
rm %{buildroot}%{_datadir}/Pythia8/AUTHORS
rm %{buildroot}%{_datadir}/Pythia8/COPYING
rm %{buildroot}%{_datadir}/Pythia8/GUIDELINES
rm %{buildroot}%{_datadir}/Pythia8/README
rm %{buildroot}%{_datadir}/Pythia8/examples/Makefile
rm %{buildroot}%{_datadir}/Pythia8/examples/Makefile.inc
rm %{buildroot}%{_datadir}/Pythia8/examples/runmains

%if %{buildpy2}
mkdir -p %{buildroot}%{python2_sitearch}
install -p -m 644 pythia8.py %{buildroot}%{python2_sitearch}
install -p -m 755 py2/_pythia8.so %{buildroot}%{python2_sitearch}
touch %{buildroot}%{python2_sitearch}/%{name}-%{version}.egg-info
%endif

mkdir -p %{buildroot}%{python3_sitearch}
install -p -m 644 pythia8.py %{buildroot}%{python3_sitearch}
install -p -m 755 py3/_pythia8.*.so %{buildroot}%{python3_sitearch}
touch %{buildroot}%{python3_sitearch}/%{name}-%{version}.egg-info

%if %{?rhel}%{!?rhel:0} == 7
mkdir -p %{buildroot}%{python3_other_sitearch}
install -p -m 644 pythia8.py %{buildroot}%{python3_other_sitearch}
install -p -m 755 py3oth/_pythia8.*.so %{buildroot}%{python3_other_sitearch}
touch %{buildroot}%{python3_other_sitearch}/%{name}-%{version}.egg-info
%endif

%ldconfig_scriptlets

%ldconfig_scriptlets lhapdf

%files
%{_libdir}/libpythia8-%{version}.so
%doc AUTHORS GUIDELINES
%license COPYING

%files devel
%{_libdir}/libpythia8.so
%{_includedir}/Pythia8
%{_includedir}/Pythia8Plugins
%doc CODINGSTYLE

%files lhapdf
%{_libdir}/libpythia8lhapdf*.so

%if %{buildpy2}
%files -n python2-%{name}
%{python2_sitearch}/%{name}-%{version}.egg-info
%{python2_sitearch}/_pythia8.so
%{python2_sitearch}/pythia8.py*
%endif

%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/%{name}-%{version}.egg-info
%{python3_sitearch}/_pythia8.*.so
%{python3_sitearch}/pythia8.py
%{python3_sitearch}/__pycache__/pythia8.*

%if %{?rhel}%{!?rhel:0} == 7
%files -n python%{python3_other_pkgversion}-%{name}
%{python3_other_sitearch}/%{name}-%{version}.egg-info
%{python3_other_sitearch}/_pythia8.*.so
%{python3_other_sitearch}/pythia8.py
%{python3_other_sitearch}/__pycache__/pythia8.*
%endif

%files data
%dir %{_datadir}/Pythia8
%{_datadir}/Pythia8/xmldoc
%license COPYING

%files examples
%dir %{_datadir}/Pythia8
%doc %{_datadir}/Pythia8/examples
%doc %{_datadir}/Pythia8/outref
%license COPYING

%files doc
%doc share/Pythia8/htmldoc
%doc share/Pythia8/pdfdoc
%license COPYING

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.2.43-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 8.2.43-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.2.43-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.43-1
- Update to version 8.2.43
- Add Python 3 package for EPEL 6
- Remove ppc64 specific conditionals (ppc64 no longer built in Fedora or EPEL)

* Tue Jun 11 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.35-8
- Use python-embed pkg-config module if it exists (python 3.8 compatibility)

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 8.2.35-6
- Rebuilt to change main python from 3.4 to 3.6

* Wed Feb 06 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.35-7
- Reduce memory usage during compilation of the python module on 32 bit arm

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.35-5
- Don't build Python 2 package for Fedora >= 30
- Add Python 3.6 package for EPEL 7
- Use empty .egg-info files instead of empty .dist-info files to make
  virtualenv happy

* Tue Jul 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.35-4
- Don't own toplevel __pycache__ directory

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.35-2
- Create empty .dist-info files so that rpm auto-generates provides

* Wed Jul 04 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 8.2.35-1
- Update to version 8.2.35
- Add python bindings (except on ppc64 for EPEL 6)
- Change license tag from GPLv2 to GPLv2+

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 8.2.15-7
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.2.15-2
- Add missing obsoletes

* Thu Apr 07 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.2.15-1
- Update to version 8.2.15

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.86-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8.1.86-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.86-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1.86-1
- Update to version 8.1.86

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 30 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1.80-1
- Update to version 8.1.80
- Use full version in soname

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1.76-3
- Remove DOS end-of-line

* Thu May 23 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1.76-2
- Fix race condition in Makefile
- Add isa to dependencies

* Sat May 18 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1.76-1
- New upstream release

* Wed Nov 14 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1.70-1
- Initial build
