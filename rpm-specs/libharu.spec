%global gittag0 RELEASE_2_3_0RC3

Name:           libharu
Version:        2.3.0
Release:        12%{?dist}
Summary:        C library for generating PDF files
License:        zlib with acknowledgement
URL:            http://libharu.org
# not available. rebuilt from ZIP in this package
Source0:        https://github.com/libharu/${name}/archive/%{gittag0}/%{name}-%{version}-rc3.tar.gz
Patch0:         libharu-RELEASE_2_3_0_cmake.patch
Patch1:         libharu-2.3.0-triangleshading.patch
Patch2:         libharu-2.3.0-smallnumber.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel

%description
libHaru is a library for generating PDF files. 
It is free, open source, written in ANSI C and cross platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{gittag0}
# fix cmake build
%patch0 -p1 -b .cmake
# github #157 pull request
%patch1 -p1 -b .triangleshading
# github #187 pull request
%patch2 -p1 -b .smallnumber

%build
%cmake -DLIBHPDF_STATIC=NO

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README
%{_libdir}/libhpdf.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/libhpdf.so

%changelog
* Sat Aug 01 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.0-12
- Fix for new cmake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.0-9
- Update to RC3
- Apply 157 and 187 upstream github pull requests. See rhbz #1833318

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.3.0-1
- Update to new 2.3.0.
- Drop png15 patch.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 30 2016 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 2.2.1-8
- Fix BR: glibc-headers -> gcc (RHBZ #1230474).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Tom Callaway <spot@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- Fix compile with libpng 1.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.0-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 23 2010 Alex71 <nyrk71@gmail.com> 2.1.0-2
- put libhpdf.so in the devel package and libhpdf-2.1.0.so in the main one
- removed duplicated README and CHANGES from devel package
- fixed "E: empty-debuginfo-package" with --enable-debug flag in configure
- removed INSTALL file
- added demo/ directory in doc (devel only) as doc 
* Sat Mar 20 2010 Alex71 <nyrk71@gmail.com> 2.1.0-1
- First release for Fedora
