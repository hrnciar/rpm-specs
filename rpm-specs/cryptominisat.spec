Name:           cryptominisat
Version:        5.7.1
Release:        3%{?dist}
Summary:        SAT solver

License:        MIT
URL:            http://www.msoos.org/
Source0:        https://github.com/msoos/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Change the CMake files to not change Fedora build flags
Patch0:         %{name}-cmake.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gperftools-devel
BuildRequires:  help2man
BuildRequires:  pkgconfig(m4ri)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
CryptoMiniSat is a modern, multi-threaded, feature-rich, simplifying SAT
solver. Highlights:
- Instance simplification at every point of the search (inprocessing)
- Over 100 configurable parameters to tune to specific needs
- Collection of statistical data to MySQL database + javascript-based
  visualization of it
- Clean C++ and python interfaces

%package devel
Summary:        Header files for developing with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       m4ri-devel%{?_isa}
Requires:       tbb-devel%{?_isa}
Requires:       cmake-filesystem

%description devel
Header files for developing applications that use %{name}.

%package libs
Summary:        Cryptominisat library

%description libs
The %{name} library.

%package -n python3-%{name}
Summary:        Python 3 interface to %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 interface to %{name}.

%prep
%autosetup -p0

# Fix the library install path
if [ "%{_libdir}" = "%{_prefix}/lib64" ]; then
  sed -i 's,${dir}/lib,&64,g' cmake/FindPkgMacros.cmake
fi

# Fix the python install
sed -ri 's|install |&--root %{buildroot} |' python/CMakeLists.txt

%build
%cmake . -DCMAKE_INSTALL_LIBDIR=%{_lib}
%make_build

%install
%make_install

# Move cmake files to where they should go
if [ "%{_lib}" = "lib64" ]; then
  mv %{buildroot}%{_prefix}/lib/cmake %{buildroot}%{_libdir}
  sed -i 's|%{_prefix}/lib/|%{_libdir}/|' \
      %{buildroot}%{_libdir}/cmake/cryptominisat5/*.cmake
fi

%files
%doc README.markdown
%{_bindir}/cryptominisat5
%{_bindir}/cryptominisat5_simple
%{_mandir}/man1/cryptominisat5*

%files devel
%{_includedir}/cryptominisat5/
%{_libdir}/libcryptominisat5.so
%{_libdir}/cmake/cryptominisat5/

%files libs
%doc AUTHORS
%license LICENSE.txt
%{_libdir}/libcryptominisat5.so.5.7

%files -n python3-%{name}
%doc python/README.rst
%license python/LICENSE
%{python3_sitearch}/pycryptosat*

%changelog
* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 5.7.1-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.7.1-2
- Rebuilt for Python 3.9

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 5.7.1-1
- Version 5.7.1

* Sat Apr 25 2020 Jerry James <loganjerry@gmail.com> - 5.7.0-1
- Version 5.7.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jerry James <loganjerry@gmail.com> - 5.6.8-5
- Rebuild for m4ri 20200125

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 5.6.8-4
- Rebuild for m4ri 20200115

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.6.8-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Jerry James <loganjerry@gmail.com> - 5.6.8-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 5.6.6-3
- Rebuilt for Boost 1.69

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 5.6.6-2
- Fix FTBFS with latest cmake release

* Mon Dec 24 2018 Jerry James <loganjerry@gmail.com> - 5.6.6-1
- New upstream release

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 5.6.5-1
- New upstream release
- Drop the python2 subpackage

* Wed Aug  8 2018 Jerry James <loganjerry@gmail.com> - 5.6.4-1
- New upstream release

* Sat Jul 21 2018 Jerry James <loganjerry@gmail.com> - 5.6.3-4
- Add Obsoletes and Provides for cryptominisat4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.6.3-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Jerry James <loganjerry@gmail.com> - 5.6.3-1
- New upstream release
- License change to MIT
- Add python3 subpackage

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 5.0.1-2
- Rebuilt for Boost 1.66

* Sat Nov 25 2017 Jerry James <loganjerry@gmail.com> - 5.0.1-1
- Update to major version 5

* Sat Sep 23 2017 Jerry James <loganjerry@gmail.com> - 2.9.11-6
- Update the mariadb BR (bz 1493618)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 2.9.11-1
- New upstream release

* Sat Mar  5 2016 Jerry James <loganjerry@gmail.com> - 2.9.10-3
- post/postun scripts are for libs, not the main package

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep  4 2015 Jerry James <loganjerry@gmail.com> - 2.9.10-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.9.9-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 2.9.9-4
- Use license macro

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Jerry James <loganjerry@gmail.com> - 2.9.9-1
- New upstream release

* Mon Sep 23 2013 Jerry James <loganjerry@gmail.com> - 2.9.8-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Jerry James <loganjerry@gmail.com> - 2.9.6-1
- New upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 2.9.5-1
- New upstream release
- Project files now carry the MIT license

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Jerry James <loganjerry@gmail.com> - 2.9.3-1
- New upstream version

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-2
- Rebuilt for c++ ABI breakage

* Mon Jan 23 2012 Jerry James <loganjerry@gmail.com> - 2.9.2-1
- New upstream version
- Man page is now upstream
- All patches have been applied upstream
- Tests have been removed from the source distribution

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 2.9.1-3
- Rebuild for GCC 4.7

* Mon Dec 19 2011 Dan Horák <dan[at]danny.cz> - 2.9.1-2
- FPU handling is x86 specific
- set library path so the test is run

* Wed Dec  7 2011 Jerry James <loganjerry@gmail.com> - 2.9.1-1
- Initial RPM
