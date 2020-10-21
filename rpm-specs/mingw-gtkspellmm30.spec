%{?mingw_package_header}

%global pkgname gtkspellmm30

Name:          mingw-%{pkgname}
Version:       3.0.5
Release:       12%{?dist}
Summary:       MinGW Windows GtkSpellmm library
License:       GPLv2+
BuildArch:     noarch
URL:           http://gtkspell.sourceforge.net/
Source0:       http://downloads.sourceforge.net/gtkspell/gtkspellmm-%{version}.tar.xz

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-glibmm24
BuildRequires: mingw32-gtkmm30
BuildRequires: mingw32-gtkspell3

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-glibmm24
BuildRequires: mingw64-gtkmm30
BuildRequires: mingw64-gtkspell3


%description
MinGW Windows GtkSpellmm library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GtkSpellmm library

%description -n mingw32-%{pkgname}
MinGW Windows GtkSpellmm library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows GtkSpellmm library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows GtkSpellmm library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GtkSpellmm library

%description -n mingw64-%{pkgname}
MinGW Windows GtkSpellmm library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows GtkSpellmm library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows GtkSpellmm library.


%{?mingw_debug_package}


%prep
%autosetup -n gtkspellmm-%{version}


%build
%if 0%{?fedora} == 23
export MINGW32_CFLAGS="%mingw32_cflags -std=c++11"
export MINGW32_CXXFLAGS="%mingw32_cflags -std=c++11"
export MINGW64_CFLAGS="%mingw64_cflags -std=c++11"
export MINGW64_CXXFLAGS="%mingw64_cflags -std=c++11"
%endif
%mingw_configure --disable-documentation --enable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libgtkspellmm-3.0-0.dll
%{mingw32_includedir}/gtkspellmm-3.0/
%{mingw32_libdir}/gtkspellmm-3.0/
%{mingw32_libdir}/libgtkspellmm-3.0.dll.a
%{mingw32_libdir}/pkgconfig/gtkspellmm-3.0.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libgtkspellmm-3.0.a

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libgtkspellmm-3.0-0.dll
%{mingw64_includedir}/gtkspellmm-3.0/
%{mingw64_libdir}/gtkspellmm-3.0/
%{mingw64_libdir}/libgtkspellmm-3.0.dll.a
%{mingw64_libdir}/pkgconfig/gtkspellmm-3.0.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libgtkspellmm-3.0.a


%changelog
* Wed Aug 12 13:40:29 GMT 2020 Sandro Mani <manisandro@gmail.com> - 3.0.5-12
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.0.5-9
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Sandro Mani <manisandro@gmail.com> - 3.0.5-3
- Rebuild (glibmm24)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Sandro Mani <manisandro@gmail.com> - 3.0.5-1
- Update to 3.0.5

* Tue Apr 05 2016 Sandro Mani <manisandro@gmail.com> - 3.0.4-2
- Respin

* Sun Apr 03 2016 Sandro Mani <manisandro@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.3-4
- Rebuild against latest mingw-gcc

* Thu Mar 26 2015 Sandro Mani <manisandro@gmail.com> - 3.0.3-3
- Use license macro for the COPYING file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-3
- Rebuild again to really resolve InterlockedCompareExchange regression in mingw32 libraries

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.2-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Tue Jun 04 2013 Sandro Mani <manisandro@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Sun May 19 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-2
- Remove mingw_build_win32/64 macros
- Properly version mingw32-filesystem BuildRequires

* Wed May 08 2013 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Initial package
