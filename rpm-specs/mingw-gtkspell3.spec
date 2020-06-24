%{?mingw_package_header}

%global pkgname gtkspell3

Name:          mingw-%{pkgname}
Version:       3.0.10
Release:       5%{?dist}
Summary:       MinGW Windows GtkSpell3 library
License:       GPLv2+
BuildArch:     noarch
URL:           http://gtkspell.sourceforge.net/
Source0:       http://downloads.sourceforge.net/gtkspell/%{pkgname}-%{version}.tar.xz

BuildRequires: intltool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-enchant2
BuildRequires: mingw32-gettext
BuildRequires: mingw32-gtk3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-enchant2
BuildRequires: mingw64-gettext
BuildRequires: mingw64-gtk3


%description
MinGW Windows GtkSpell3 library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GtkSpell3 library

%description -n mingw32-%{pkgname}
MinGW Windows GtkSpell3 library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows GtkSpell3 library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows GtkSpell3 library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GtkSpell3 library

%description -n mingw64-%{pkgname}
MinGW Windows GtkSpell3 library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows GtkSpell3 library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows GtkSpell3 library.


%{?mingw_debug_package}


%prep
%autosetup -n %{pkgname}-%{version}


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%mingw_find_lang %{pkgname}


%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.lang
%license COPYING
%{mingw32_bindir}/libgtkspell3-3-0.dll
%{mingw32_includedir}/gtkspell-3.0/
%{mingw32_libdir}/libgtkspell3-3.dll.a
%{mingw32_libdir}/pkgconfig/gtkspell3-3.0.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libgtkspell3-3.a

%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.lang
%license COPYING
%{mingw64_bindir}/libgtkspell3-3-0.dll
%{mingw64_includedir}/gtkspell-3.0/
%{mingw64_libdir}/libgtkspell3-3.dll.a
%{mingw64_libdir}/pkgconfig/gtkspell3-3.0.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libgtkspell3-3.a


%changelog
* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 3.0.10-5
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Sandro Mani <manisandro@gmail.com> - 3.0.10-1
- Update to 3.0.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Sandro Mani <manisandro@gmail.com> - 3.0.9-1
- Update to 3.0.9

* Sun Apr 03 2016 Sandro Mani <manisandro@gmail.com> - 3.0.8-1
- Update to 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Sandro Mani <manisandro@gmail.com> - 3.0.7-1
- Update to 3.0.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Sandro Mani <manisandro@gmail.com> - 3.0.6-1
- Update to 3.0.6

* Sat Apr 19 2014 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Thu Sep 26 2013 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.3-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Tue May 21 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-3
- Fix source url

* Sun May 19 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-2
- Remove mingw_build_win32/64 macros
- Properly version mingw32-filesystem BuildRequires

* Wed May 08 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Initial package
