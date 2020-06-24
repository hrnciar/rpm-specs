%{?mingw_package_header}

%global pkgname vulkan-headers
%global srcname Vulkan-Headers

#global commit 634e3658d6fa8f95f9062a3a7831d5567baf0eb3
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          mingw-%{pkgname}
Version:       1.2.135.0
Release:       1%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       ASL 2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/sdk-%{version}/%{srcname}-%{version}.tar.gz
%endif

BuildRequires: cmake
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}
Obsoletes:     mingw32-vulkan

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}
Obsoletes:     mingw64-vulkan

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.



%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{srcname}-%{commit}
%else
%autosetup -p1 -n %{srcname}-sdk-%{version}
%endif


%build
%mingw_cmake
%mingw_make


%install
%mingw_make DESTDIR=%{buildroot} install


%files -n mingw32-%{pkgname}
%license LICENSE.txt
%{mingw32_includedir}/vulkan/
%{mingw32_datadir}/vulkan/

%files -n mingw64-%{pkgname}
%license LICENSE.txt
%{mingw64_includedir}/vulkan/
%{mingw64_datadir}/vulkan/


%changelog
* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 1.2.135.0-1
- Update to 1.2.135.0

* Sun Feb 02 2020 Sandro Mani <manisandro@gmail.com> - 1.2.131.1-1
- Update to 1.2.131.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.126.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Sandro Mani <manisandro@gmail.com> - 1.1.126.0-1
- Update to 1.1.126.0

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 1.1.114.0-1
- Update to 1.1.114.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 1.1.108.0-1
- Update to 1.1.108.0

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 1.1.106.0-1
- Update to 1.1.106.0

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 1.1.101.0-1
- Update to 1.1.101.0

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 1.1.97.0-1
- Update to 1.1.97.0

* Mon Feb 04 2019 Sandro Mani <manisandro@gmail.com> - 1.1.82.0-3
- Obsolete mingw{32,64}-vulkan

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.82.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 1.1.82.0-1
- Updateto 1.1.82.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Sandro Mani <manisandro@gmail.com> - 1.1.77-1
- Update to 1.1.77

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 1.1.76-0.1.git634e365
- Initial package
