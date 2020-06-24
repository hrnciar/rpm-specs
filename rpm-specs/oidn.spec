Name:		oidn
Version:	1.2.1
Release:	1%{?dist}
Summary:	Library of denoising filters for images rendered with ray tracing

License:	ASL 2.0
URL:		https://openimagedenoise.github.io/
Source0:	https://github.com/OpenImageDenoise/%{name}/releases/download/v%{version}/%{name}-%{version}.src.tar.gz

# Library only available of x86_64 arch
ExclusiveArch:	x86_64

BuildRequires:	cmake >= 3.13.0
BuildRequires:	gcc-c++
BuildRequires:	ispc
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(tbb)
BuildRequires:	redhat-rpm-config

%description
An open source library of high-performance, high-quality denoising
filters for images rendered with ray tracing.

%package	libs
Summary:	Libraries for %{name}

%description	libs
The %{name}-libs package contains shared library for %{name}.

%package        devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	docs
Summary:	Documentation for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildArch:	noarch

%description	docs
The %{name}-docs package contains documentation for %{name}.

%prep
%autosetup

%build
%cmake -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
	.
%make_build

%install
%make_install

# Remove duplicated documentation
rm -rf %{buildroot}%{_docdir}/OpenImageDenoise

%files
%license LICENSE.txt
%doc CHANGELOG.md 
%{_bindir}/%{name}{Denoise,Test,Benchmark}

%files libs
%{_libdir}/cmake/OpenImageDenoise
%{_libdir}/libOpenImageDenoise.so.*

%files docs
%doc README.md readme.pdf 

%files devel
%{_includedir}/OpenImageDenoise
%{_libdir}/libOpenImageDenoise.so

%changelog
* Tue Jun 16 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Fri Apr 10 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0
- Add ispc and redhat-rpm-config depedencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sat Aug 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0
- Use pkgconfig for Python 3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Tue Apr 02 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-4
- Use spaces on line 47
- Make -doc subpackage noarch
- Make -doc subpackage requiring main package

* Mon Apr 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-3
- Move versioned so-files to libs subpackage
- Move unversioned so-files to devel subpackage

* Mon Apr 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-2
- Add subpackage for large doc files
- Move .so files to devel subpackage
- Fix library path
- Remove unneeded clearance

* Sun Mar 31 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 0.8.2-1
- Initial packaging
