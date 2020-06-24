%{?mingw_package_header}
%global commit 2ad0492fb00919d99500f1da74abf5ad3c870e4e
%global shortcommit %(c=%{commit}; echo ${c:0:7})


%global pkgname spirv-headers
%global srcname SPIRV-Headers

Name:          mingw-%{pkgname}
Version:       1.5.1
Release:       3%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       MIT
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
%if 0%{?commit:1}
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/KhronosGroup/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
%endif


BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95


%description
MinGW Windows %{pkgname}


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.



%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{srcname}-%{commit}
%else
%autosetup -p1 -n %{srcname}-%{version}
%endif


%build
# Nothing to build


%install
install -d %{buildroot}%{mingw32_includedir}/
install -d %{buildroot}%{mingw64_includedir}/
cp -a include/spirv %{buildroot}%{mingw32_includedir}/spirv
cp -a include/spirv %{buildroot}%{mingw64_includedir}/spirv


%files -n mingw32-%{pkgname}
%{mingw32_includedir}/spirv/

%files -n mingw64-%{pkgname}
%{mingw64_includedir}/spirv/


%changelog
* Wed Apr 22 2020 Sandro Mani <manisandro@gmail.com> - 1.5.1-3.git2ad0492
- Update to git 2ad0492

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2.gitaf64a9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Sandro Mani <manisandro@gmail.com> - 1.5.1-1-gitaf64a9e
- Update to 1.5.1 (git af64a9e)

* Wed Jul 31 2019 Sandro Mani <manisandro@gmail.com> - 1.4.1-3.gite4322e3
- Update to git e4322e3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Sandro Mani <manisandro@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 1.3.3.git03a0815
- Update to git 03a0815

* Mon Feb 11 2019 Sandro Mani <manisandro@gmail.com> - 1.3-3.git8bea0a2
- Update to git 8bea0a2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2.gitff684ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Sandro Mani <manisandro@gmail.com> - 1.3-1.gitff684ff
- git ff684ff is actually a version 1.3 snapshot

* Mon Jul 30 2018 Sandro Mani <manisandro@gmail.com> - 1.2-0.3.gitff684ff
- Update to git ff684ff

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.2.git12f8de9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Sandro Mani <manisandro@gmail.com> - 1.2-0.1.git12f8de9
- Initial package
