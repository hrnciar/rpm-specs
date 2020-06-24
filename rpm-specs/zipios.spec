Name:           zipios
Version:        2.2.1.0
Release:        3%{?dist}
# Most of the project is under LGPLv2+ but two source filesa are GPLv2+ so the
# combined work is GPLv2+.
License:        GPLv2+
Summary:        C++ library for reading and writing Zip files

URL:            https://snapwebsites.org/project/zipios
Source0:        https://github.com/Zipios/Zipios/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++ libstdc++-devel
BuildRequires:  catch1-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  cppunit-devel
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  doxygen
# For man page generation
BuildRequires:  help2man


%description
Zipios is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

Note: This is nearly a complete rewrite of the 1.x series by a new upstream.
The previous version is depreciated but still supported as zipios++.


%package devel
Summary:        Header files for zipios
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       zlib-devel
Requires:       cmake

%description devel
The header files are only needed for development of programs using %{name}.

Note: This is nearly a complete rewrite of the 1.x series by a new upstream.
The previous version is depreciated but still supported as zipios++.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Developer documentation for %{name}.


%prep
%autosetup -n Zipios-%{version}
sed -i "s/\-std=c++11//g" CMakeLists.txt


%build
rm -rf build && mkdir build && pushd build
%cmake -DCATCH_INCLUDE_DIR=%{_includedir}/catch \
       -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules \
       -DBUILD_ZIPIOS_TESTS=FALSE \
       ../
make %{?_smp_mflags}


%install
pushd build
%make_install
# Create man pages
mkdir -p %{buildroot}%{_mandir}/man1
for bin in appendzip dosdatetime zipios; do
    help2man -s 1 -N tools/$bin > %{buildroot}%{_mandir}/man1/$bin.1
done
popd


%check
# Catch based testing is broken on gcc 6
# https://sourceforge.net/p/zipios/bugs/9/
# Test executable no longer compiles with gcc 7
# https://bugzilla.redhat.com/show_bug.cgi?id=1424569
# https://sourceforge.net/p/zipios/bugs/10/
#pushd build
#make run_zipios_tests


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%exclude %{_pkgdocdir}/html/
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*.1*

%files devel
%{_libdir}/*.so
%{_datadir}/cmake/ZipIos/
%{_includedir}/%{name}
%{_mandir}/man3/*

%files doc
%{_pkgdocdir}/html/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.1-4
- catch → catch1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-1
- Update to latest upstream release.
- Disable unit testing until catch works with gcc 6.

* Mon Oct 19 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-5
- Use system catch now that it's available.

* Wed Sep 16 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-4
- Add cmake as requirement to devel subpackage.
- Fix references to documentation for directory ownership.
- Fix documentation install to be compliant with the packaging guidelines.
- Make doc subpackage only require the main package.
- Add help2man to build requirements to generate man pages.
- Update %%{_pkgdocdir} in %%files to fix directory ownership.

* Fri Aug 28 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-2
- Update license tag to GPLv2+.
- Fix dist tag.
- Add note to description how this package differs from zipios++.

* Mon May 11 2015 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-1
- Initial packaging.
