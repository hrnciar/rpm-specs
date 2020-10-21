%global __cmake_in_source_build 1
Name: libsquish
Version: 1.15
Release: 7%{?dist}
URL: https://sourceforge.net/projects/libsquish/
Summary: Open source DXT compression library
License: MIT
Source0: http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
Patch0:  libsquish-cmake_install.patch
BuildRequires: gcc-c++ cmake

%package devel
Summary: Development files for Open source DXT compression library
Requires: %{name}%{_isa} = %{version}-%{release}

%description
The libSquish library compresses images with the DXT standard
(also known as S3TC). This standard is mainly used by OpenGL and
DirectX for the lossy compression of RGBA textures.

%description devel
The libsquish-devel package contains files needed for developing or compiling
applications which use DXT compression.

%prep
%autosetup -c libsquish-%{version}

%build
%cmake . -DBUILD_SQUISH_WITH_SSE2=OFF
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc ChangeLog.txt
%{_libdir}/*.so.0.0

%files devel
%doc README.txt
%{_libdir}/*.so
%{_includedir}/*

%changelog
* Tue Aug 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.15-7
- Fix FTBFS.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15-2
- Review fixes.

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15-1
- Initial package.
