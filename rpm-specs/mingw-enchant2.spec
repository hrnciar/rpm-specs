%{?mingw_package_header}

%global pkgname enchant2

Name:          mingw-%{pkgname}
Version:       2.2.8
Release:       1%{?snap}%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       LGPLv2+
BuildArch:     noarch
URL:           https://github.com/AbiWord/enchant
Source0:       https://github.com/AbiWord/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz


BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-glib2
BuildRequires: mingw32-hunspell

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-glib2
BuildRequires: mingw64-hunspell


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n enchant-%{version}


%build
MINGW32_CONFIGURE_ARGS="--with-hunspell-dir=%{mingw32_datadir}/myspell" \
MINGW64_CONFIGURE_ARGS="--with-hunspell-dir=%{mingw64_datadir}/myspell" \
%mingw_configure --disable-static --without-hspell --enable-relocatable

MINGW32_MAKE_ARGS="pkgdatadir=%{mingw32_datadir}/enchant-2" \
MINGW64_MAKE_ARGS="pkgdatadir=%{mingw64_datadir}/enchant-2" \
%mingw_make %{?_smp_mflags}


%install
MINGW32_MAKE_ARGS="pkgdatadir=%{mingw32_datadir}/enchant-2" \
MINGW64_MAKE_ARGS="pkgdatadir=%{mingw64_datadir}/enchant-2" \
%mingw_make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

# Drop the man-pages
rm -rf %{buildroot}%{mingw32_datadir}/man
rm -rf %{buildroot}%{mingw64_datadir}/man


%files -n mingw32-%{pkgname}
%license COPYING.LIB
%{mingw32_bindir}/enchant-lsmod-2.exe
%{mingw32_bindir}/enchant-2.exe
%{mingw32_bindir}/libenchant-2.dll
%{mingw32_includedir}/enchant-2/
%dir %{mingw32_libdir}/enchant-2/
%{mingw32_libdir}/enchant-2/enchant_hunspell.dll
%{mingw32_libdir}/enchant-2/enchant_hunspell.dll.a
%{mingw32_libdir}/libenchant-2.dll.a
%{mingw32_libdir}/pkgconfig/enchant-2.pc
%{mingw32_datadir}/enchant-2/

%files -n mingw64-%{pkgname}
%license COPYING.LIB
%{mingw64_bindir}/enchant-lsmod-2.exe
%{mingw64_bindir}/enchant-2.exe
%{mingw64_bindir}/libenchant-2.dll
%{mingw64_includedir}/enchant-2/
%dir %{mingw64_libdir}/enchant-2/
%{mingw64_libdir}/enchant-2/enchant_hunspell.dll
%{mingw64_libdir}/enchant-2/enchant_hunspell.dll.a
%{mingw64_libdir}/libenchant-2.dll.a
%{mingw64_libdir}/pkgconfig/enchant-2.pc
%{mingw64_datadir}/enchant-2/


%changelog
* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 2.2.8-1
- Update to 2.2.8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.2.7-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Sun Sep 15 2019 Sandro Mani <manisandro@gmail.com> - 2.2.7-1
- Update to 2.2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Sandro Mani <manisandro@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Fri Jun 28 2019 Sandro Mani <manisandro@gmail.com> - 2.2.4-2
- Add patch to fix memory leaks (#1718084)
- Pass --without-hspell

* Tue Jun 18 2019 Sandro Mani <manisandro@gmail.com> - 2.2.4-1
- Update to 2.2.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 2.2.3-4
- Rebuild (hunspell)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Sandro Mani <manisandro@gmail.com> - 2.2.3-1
- Update to 2.2.3

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Thu Dec 14 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-2
- Add patch to fix FSF addresses

* Wed Dec 13 2017 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Initial package
