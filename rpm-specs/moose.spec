#global commit 0e12e41b52deb8ea746bc760cddd6e100ca5cfd8
#global shortcommit %%(c=%{commit}; echo ${c:0:7})

Name:           moose
Version:        3.1.4
%global codename chamcham
Release:        11%{?dist}%{?prerelease:.%{prerelease}}%{?commit:.git%{shortcommit}}
Summary:        Multiscale Neuroscience and Systems Biology Simulator
License:        GPLv3
URL:            http://moose.ncbs.res.in/
%if %{defined commit}
Source0:        https://github.com/BhallaLab/moose-core/archive/%{commit}.tar.gz#/moose-core-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/BhallaLab/moose-core/archive/v%{version}.tar.gz#/moose-core-%{version}.tar.gz
%endif

# https://github.com/BhallaLab/moose-core/pull/282
Patch0001:      0001-Avoid-open-coded-strdup-that-cause-compilation-failu.patch
Patch0002:      0002-Avoid-open-coded-strdup-that-causes-a-warning.patch
Patch0003:      0003-Use-sys.executable-to-execute-test.-It-breaks-on-pyt.patch
Patch0004:      0004-Do-not-try-to-access-position-1-in-string.patch

# https://github.com/BhallaLab/moose-core/pull/375
Patch0005:       https://github.com/BhallaLab/moose-core/pull/375/commits/137e348313436782f8cf5eccc8e707ebbdc07170.patch

ExcludeArch: s390x

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  tinyxml-devel
BuildRequires:  muParser-devel
BuildRequires:  libsbml-devel
# for tests
BuildRequires:  checksec
BuildRequires:  procps-ng
BuildRequires:  openssl

BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-libsbml

%description
MOOSE is the base and numerical core for large, detailed simulations
including Computational Neuroscience and Systems Biology. MOOSE spans
the range from single molecules to subcellular networks, from single
cells to neuronal networks, and to still larger systems. It is
backwards-compatible with GENESIS, and forward compatible with Python
and XML-based model definition standards like SBML and NeuroML.

MOOSE uses Python as its primary scripting language. For backward
compatibility we have a GENESIS scripting module, but this is
deprecated. MOOSE numerical code is written in C++.

%package -n python3-%{name}
Summary:  %{summary}
%{?python_provide:%python_provide python3-moose}

Requires: python3-numpy
Requires: python3-matplotlib
Requires: python3-matplotlib-qt4
Requires: python3-lxml

%description -n python3-%{name}
This package contains the %{summary}.

%prep
%autosetup -p1 -n moose-core-%{version}

%global py_setup setup.cmake.py

%build
cmake_opts=(
        -DBUILD_SHARED_LIBS:BOOL=OFF
        -DCMAKE_SKIP_RPATH:BOOL=ON
        -DCMAKE_C_FLAGS="%optflags"
        -DCMAKE_CXX_FLAGS="%optflags"
        -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -Wl,--build-id"
        -DCMAKE_MODULE_LINKER_FLAGS="$LDFLAGS -Wl,--build-id"
        -DVERSION_MOOSE=%{version}
        -DCMAKE_BUILD_TYPE="Release|RelWithDebugInfo"
        -DCMAKE_INSTALL_DO_STRIP=0
        -DPYTHON_EXECUTABLE=%{__python3}
)

mkdir -p build
pushd build
CXXFLAGS="%optflags" \
%cmake .. "${cmake_opts[@]}"
%make_build VERBOSE=1
cd python
%py3_build
popd

%install
install -vD build/moose.bin %{buildroot}%{_bindir}/moose
install -vDt %{buildroot}%{_libdir}/ build/libmoose.so

pushd build/python
%py3_install \--install-lib=%{python3_sitearch}
# this is necessary for the dependency generator to work
chmod +x %{buildroot}%{python3_sitearch}/moose/_moose*.so
popd

%check
checksec --file=%{buildroot}%{_bindir}/moose

pushd build
# test_streamer fails randomly when quitting moose every once in a while.
ctest --output-on-failure -V -E test_streamer
popd

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -c \
    'import moose; element = moose.Neutral("/yyy"); print(element.path)'

%global _docdir_fmt %{name}

%files
%{_bindir}/moose
%{_libdir}/libmoose.so
%license LICENSE
%doc README.md

%files -n python3-%{name}
%{python3_sitearch}/moose
%{python3_sitearch}/rdesigneur
%{python3_sitearch}/pymoose-*egg-info
%license LICENSE
%doc README.md

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-9
- Add missing libmoose.so (#1754997)

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.4-8
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-7
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-3
- Subpackage python2-moose has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 28 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-2
- Rebuild because the package was not tagged properly

* Tue Aug 14 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.4-1
- Switch source back to use "moose-core" instead of "moose"
- Update to latest version
- Actually run the tests and look at the output

* Tue Aug  7 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.3-1
- Update to latest version, fix packaging (#1604882)
- Libmubml seems to be gone
- Add some dependencies useful for tests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.19.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-0.18.beta.2.git0e12e41
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.17.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.2-0.16.beta.2.git0e12e41
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.15.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.14.beta.2.git0e12e41
- Rebuild for gsl-2.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.13.beta.2.git0e12e41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-0.12.beta.2.git0e12e41
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 3.0.2-0.11.beta.2.git0e12e41
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-0.10.beta.2.git0e12e41
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar  7 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 3.0.2-0.9.beta.2.git0e12e41
- Restore patch that removes broken shared linking

* Mon Mar  7 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 3.0.2-0.8.beta.2.git0e12e41
- Update to git snapshot
- Add python3 subpackage

* Tue Feb 23 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-0.7.beta.2
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-0.6.beta.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-0.5.beta.2
- Rebuild for hdf5 1.8.16

* Sun Dec 13 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.4.beta.2
- Fix permissions on files in debuginfo subpackage
- Tweak python package generation

* Sun Dec 13 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.3.beta.2
- Fix build on i686

* Sat Dec 12 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.2.beta.2
- Remove obsolete cxx11 fix
- Use chrpath --delete

* Wed Dec  9 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.2-0.1.beta.2
- Initial packaging
