Name:           getdp
Version:        3.3.0
Release:        4%{?dist}
Summary:        General Environment for the Treatment of Discrete Problems

License:        GPLv2+
URL:            http://www.geuz.org/getdp/
Source0:        http://www.geuz.org/getdp/src/%{name}-%{version}-source.tgz

BuildRequires:  cmake
BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  arpack-devel
BuildRequires:  gmsh-devel
BuildRequires:  gsl-devel
BuildRequires:  lapack-devel blas-devel openblas-devel
BuildRequires:  python3-devel
BuildRequires:  petsc-devel
BuildRequires:  SuperLU-devel
BuildRequires:  libX11-devel
BuildRequires:  metis-devel
BuildRequires:  hdf5-devel
BuildRequires:  cgnslib-devel

# GPLv3+, some fortran files in contrib/pewe, some git version
Provides:       bundled(pewe)

%description
GetDP is an open source finite element solver using mixed elements to
discretize de Rham-type complexes in one, two and three dimensions. The main
feature of GetDP is the closeness between the input data defining discrete
problems (written by the user in ASCII data files) and the symbolic mathematical
expressions of these problems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}-source

# remove bundled libs
find contrib/ -mindepth 1 -maxdepth 1 -type d -not \( -name pewe \) -prune -exec rm -vrf {} ';'

# fix lib -> lib64 for petsc detection
sed -i 's|${ENV_PETSC_ARCH}/lib|${ENV_PETSC_ARCH}/%_lib|g' CMakeLists.txt

%build
mkdir build
pushd build/
  %cmake ../ \
    -DENABLE_MULTIHARMONIC=ON \
    -DENABLE_NX=OFF           \
    -DENABLE_OPENMP=ON        \
    -DENABLE_SLEPC=OFF        \
    -DENABLE_SPARSKIT=OFF     \
    -DENABLE_BUILD_SHARED=ON  \
    -DENABLE_BUILD_DYNAMIC=ON
  %make_build
popd

%install
%make_install -C build

# remove auto-installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
pushd build/
  ctest -VV
popd

%ldconfig_scriptlets

%files
%license LICENSE.txt CREDITS.txt
%{_bindir}/%{name}
%{_libdir}/libgetdp.so.3.3
%{_libdir}/libgetdp.so.3.3.0
%{_mandir}/man1/%{name}.1*

%files devel
%doc demos
%{_includedir}/%{name}.h
%{_libdir}/libgetdp.so

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-4
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Sandro Mani <manisandro@gmail.com> - 3.3.0-3
- Rebuild (petsc), add missing BRs

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Mon Nov 11 2019 Sandro Mani <manisandro@gmail.com> - 3.2.0-6
- Rebuild (petsc)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-5
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.2.0-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Sandro Mani <manisandro@gmail.com> - 2.11.3-8
- Rebuild (gmsh)

* Tue Jan 22 2019 Sandro Mani <manisandro@gmail.com> - 2.11.3-7
- Rebuild (gmsh)

* Mon Jan 21 2019 Richard Shaw <hobbes1069@gmail.com> - 2.11.3-6
- Rebuild for gmsh 4.1.1.

* Sun Sep 02 2018 Sandro Mani <manisandro@gmail.com> - 2.11.3-5
- Rebuild (gmsh)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.3-2
- Switch to %%ldconfig_scriptlets

* Mon Nov 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.3-1
- Update to 2.11.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.11.2-1
- Update to 2.11.2

* Thu Jun 15 2017 Sandro Mani <manisandro@gmail.com> - 2.11.1-2
- Rebuild (gmsh)

* Mon May 29 2017 Sandro Mani <manisandro@gmail.com> - 2.11.1-1
- Update to 2.11.1 (RHBZ #1450617)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May 11 2017 Sandro Mani <manisandro@gmail.com> - 2.11.0-3
- Rebuild (gmsh)

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.11.0-2
- Rebuilt for libgfortran soname bump

* Wed Jan 04 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.11.0-1
- Update to 2.11.0 (RHBZ #1409937)

* Sun Dec 11 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.10.0-3
- Rebuild for gmsh 2.15

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.10.0-2
- Rebuild (gmsh)

* Mon Oct 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.10.0-1
- Update to 2.10.0 (RHBZ #1383102)

* Sun Aug 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.9.2-1
- Update to 2.9.2

* Tue Jul 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.9.0-1
- Update to 2.9.0 (RHBZ #1354698)

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.8.0-1
- Update to 2.8.0 (RHBZ #1315030)

* Tue Feb 23 2016 Orion Poplawski <orion@cora.nwra.com> - 2.7.0-3
- Rebuild for gsl 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.7.0-1
- Initial package
