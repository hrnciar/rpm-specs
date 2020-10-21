%{?mingw_package_header}

%global pkgname tesseract

#global commit 87635c1ecb2ddba0fa1484e57680090b8bb7ac87
#global shortcommit %(c=%{commit}; echo ${c:0:7})
#global pre beta.4

Name:          mingw-%{pkgname}
Version:       4.1.1
Release:       3%{?pre:.%pre}%{?commit:.git%{shortcommit}}%{?dist}
Summary:       MinGW Windows tesseract-ocr library

License:       ASL 2.0
BuildArch:     noarch
URL:           https://github.com/tesseract-ocr/%{name}
%if 0%{?commit:1}
Source0:       https://github.com/tesseract-ocr/tesseract/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:       https://github.com/tesseract-ocr/tesseract/archive/%{version}%{?pre:-%pre}/%{pkgname}-%{version}%{?pre:-%pre}.tar.gz
%endif

BuildRequires: automake autoconf libtool autoconf-archive

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-leptonica
BuildRequires: mingw32-libgomp

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-leptonica
BuildRequires: mingw64-libgomp


%description
MinGW Windows tesseract-ocr library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows tesseract-ocr library

%description -n mingw32-%{pkgname}
MinGW Windows tesseract-ocr library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows tesseract-ocr library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows tesseract-ocr library.


%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows tesseract-ocr library tools
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
MinGW Windows tesseract-ocr library tools.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows tesseract-ocr library

%description -n mingw64-%{pkgname}
MinGW Windows tesseract-ocr library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows tesseract-ocr library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows tesseract-ocr library.


%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows tesseract-ocr library tools
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
MinGW Windows tesseract-ocr library tools.


%{?mingw_debug_package}


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{pkgname}-%{commit}
%else
%autosetup -p1 -n %{pkgname}-%{version}%{?pre:-%pre}
%endif


%build
autoreconf -i
%mingw_configure --disable-openmp
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

# Delete *.la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Delete man files
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libtesseract-4.dll
%{mingw32_includedir}/tesseract/
%{mingw32_libdir}/libtesseract.dll.a
%{mingw32_libdir}/pkgconfig/tesseract.pc
%{mingw32_datadir}/tessdata/

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libtesseract.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libtesseract-4.dll
%{mingw64_includedir}/tesseract/
%{mingw64_libdir}/libtesseract.dll.a
%{mingw64_libdir}/pkgconfig/tesseract.pc
%{mingw64_datadir}/tessdata/

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libtesseract.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Sandro Mani <manisandro@gmail.com> - 4.1.1-1
- Update to 4.1.1

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 4.1.0-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Sandro Mani <manisandro@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Sandro Mani <manisandro@gmail.com> - 4.0.0-1
- Update to 4.0.0

* Mon Oct 08 2018 Sandro Mani <manisandro@gmail.com> - 4.0.0-0.4.beta.4
- BR: mingw{32,64}-libgomp

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 4.0.0-0.3.beta.4
- Update to 4.0.0-beta.4

* Sat Aug 25 2018 Sandro Mani <manisandro@gmail.com> - 3.05.02-1
- Update to 3.05.02

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.05.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 3.05.01-1
- Update to 3.05.01

* Tue Feb 21 2017 Sandro Mani <manisandro@gmail.com> - 3.05.00-1
- Update to 3.05.00

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.04.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Sandro Mani <manisandro@gmail.com> - 3.04.01-1
- Update to 3.04.01

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.04.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 3.04.00-3
- Rebuild (leptonica)

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 3.04.00-2
- Rebuild (leptonica)

* Tue Oct 06 2015 Sandro Mani <manisandro@gmail.com> - 3.04.00-1
- Update to 3.04.00

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 04 2014 Sandro Mani <manisandro@gmail.com> - 3.03-0.1.rc1
- Update to 3.03-rc1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Sandro Mani <manisandro@gmail.com> - 3.02.02-3
- Fix Source0 URL

* Sun May 19 2013 Sandro Mani <manisandro@gmail.com> - 3.02.02-2
- Remove mingw_build_win32/64 macros
- Properly version mingw32-filesystem BuildRequires

* Wed May 08 2013 Sandro Mani <manisandro@gmail.com> - 3.02.02-1
- Initial Fedora package
