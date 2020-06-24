%global		with_snapshot	0
%global		with_examples	0
#%%global		prerelease	beta
#%%global		commit		40b9aca2668f443cae6bfbfa7cc5a354f1087011
#%%global		shortcommit	%%(c=%%{commit}; echo ${c:0:7})

Name:		embree
Version:	3.10.0
Release:	2%{?dist}
Summary:	Collection of high-performance ray tracing kernels developed at Intel

License:	ASL 2.0
URL:		https://embree.github.io
%if %{with_snapshot}
Source:		https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{version}-%{shortcommit}.tar.gz
%else
Source:		https://github.com/%{name}/%{name}/archive/v%{version}%{?prerelease:%{-prerelease}.0}.tar.gz#/%{name}-%{version}%{?prerelease:-%{prerelease}.0}.tar.gz
%endif

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	giflib-devel
BuildRequires:	ispc
%if 0%{?fedora} >= 32
BuildRequires:	pkgconfig(glut)
%else
BuildRequires:	pkgconfig(freeglut)
%endif
BuildRequires:	pkgconfig(glfw3)
BuildRequires:	pkgconfig(xmu)
# Optional dependencies needed for examples
%if %{with_examples}
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(OpenImageIO)
%endif
BuildRequires:	pkgconfig(tbb)

# Use 64bit architectures because of SSE2 and up
ExclusiveArch:	x86_64

%description
A collection of high-performance ray tracing kernels intended to graphics 
application engineers that want to improve the performance of their application.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
 applications that use %{name}.

%if %{with_examples}
%package	examples
Summary:	Example of application using %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	examples
The %{name}-examples package contains sample binaries using %{name}.
%endif

%prep
%if %{with_snapshot}
%autosetup -n %{name}-%{commit}
%else 
%autosetup -n %{name}-%{version}%{?prerelease:-%{prerelease}.0}
%endif

mkdir %{_target_platform}

%build
pushd %{_target_platform} 
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=Release \
	-DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
	-DEMBREE_TUTORIALS=OFF \
	..
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

# Relocate doc files
mv %{buildroot}%{_docdir}/%{name}3 %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/LICENSE.txt

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md readme.pdf third-party-programs-TBB.txt third-party-programs.txt
%{_libdir}/lib%{name}3.so.3
%{_libdir}/lib%{name}3.so.3.*
%{_mandir}/man3/*

%files devel
%{_libdir}/lib%{name}3.so
%{_includedir}/%{name}3/
%{_libdir}/cmake/%{name}-%{version}/

%if %{with_examples}
%files examples
%{_bindir}/%{name}3/*
%endif

%changelog
* Tue Jun 09 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.10.0-2
- Rebuild for ispc 1.13.0 and Blender 2.83.0

* Mon May 11 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0 (#1834394)

* Fri Apr 10 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Wed Feb 05 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1792573)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0 (#1747113)

* Wed Sep 25 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.1-2
- Drop renaming libraries parameter on cmake

* Sat Sep 07 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1
- Rebuild for ispc 1.12.0

* Tue Aug 20 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.0-1
- Update to 3.6.0

* Sat Aug 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.6.0-0.1.beta
- Update to 3.6.0-beta.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.2-2
- Rebuilt for ispc 1.11.0

* Fri Mar 22 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.2-1
- Update to 3.5.2
- Rebuilt for ispc 1.10.0
- Disable tutorials

* Sat Mar 02 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0
- Add glfw dependency

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2.40b9acagit
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.0.0-1.40b9acagit
- Upstream snapshot compile fix for gcc 8
- Optimize spec file

* Fri Mar 02 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Luya Tshimbalanga  <luya@fedoraproject.org> - 3.0.0-0.1.beta
- Update to 3.0.0-beta.0
- Add manual directory

* Wed Jan 17 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.17.2-1
- Update to 2.17.2 (#1512896)

* Wed Oct 25 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.17.0-2
- Rebase to more current snapshot for LLVM 5.0 support

* Thu Sep 21 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.17.0-1
- Update to 2.17.0 (#1494058)

* Tue Aug 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16.5-1
- Update to 2.16.5 (#1481678)

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 2.16.4-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16.4-1
- Update to 2.16.4 (#1466767)

* Thu Jun 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.16.2-1
- Update to 2.16.2 (#1459537)

* Wed May 17 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.16.0-1
- New upstream release

* Tue Mar 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.0-2
- Honor Fedora compilation flags again (rhbz#1436075)

* Wed Mar 22 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.15.0-1
- New upstream release

* Thu Mar 16 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.14.0-3
- Rebuild for ispc

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 09 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.14.0-1
- New upstream release
- Drop patch as the fix is included upstream

* Thu Jan 19 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.13.0-3
- Patch fixing initialization code of the rayStreamFilters sent by upstream (rhbz#1414611)

* Thu Jan 19 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 2.13.0-2
- Workaround lowering max_ISA to avx on non-Intel CPU (rhbz#1414611)

* Tue Nov 22 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 2.13.0-1
- Upstream update

* Tue Oct 18 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.12.0-1
- Upstream update addressing larger memory consumption

* Sat Sep 24 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.11.0-1
- Latest upstream update

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> 2.10.0-8
- Rebuild for tbb 2017

* Thu Aug 25 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-7
- Used ExclusiveArch for 64bit Architecture

* Sun Aug 21 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-6
- Located flags before cmake
- Used libexecdir for subpackages examples
- Pleased rpmlint
- Added examples subpackages

* Sat Aug 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-5
- Silenced all warning message in build
- Added %%check line
- Added examples subpackages

* Sat Aug 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> 2.10.0-4
- Added ispc dependency
- Removed ExclusiveArch
- Enabled ispc and tutorials

* Fri Aug 12 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 2.10.0-3
- Use ExclusiveArch tag for 64 bits architectures
- Adjust the lines of descriptions
- Fix bin path
- Add freeglut dependency from upstream

* Sat Aug 6 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 2.10.0-2
- Fixed mixed use space and tabs errors
- Shorten the line of description
- Exclude i686 architecture

* Thu Aug 4 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 2.10.0-1
- Initial build
