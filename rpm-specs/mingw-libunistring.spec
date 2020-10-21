%{?mingw_package_header}

Name: mingw-libunistring
Version: 0.9.10
Release: 4%{?dist}
Summary: MinGW port of GNU Unicode string library
License: GPLV2+ or LGPLv3+
Url: http://www.gnu.org/software/libunistring/
Source0: http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz

BuildArch: noarch

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package -n mingw32-libunistring
Summary: %{summary}

%description -n mingw32-libunistring
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package -n mingw64-libunistring
Summary: %{summary}

%description -n mingw64-libunistring
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%{?mingw_debug_package}

%prep
%setup -q -n libunistring-%{version}

%build
%mingw_configure \
    --disable-static \
    --disable-rpath

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{mingw32_infodir}/dir
rm -f $RPM_BUILD_ROOT%{mingw64_infodir}/dir

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Move staged docs so not picked up by %%doc in main package
mv $RPM_BUILD_ROOT%{mingw32_datadir}/doc/libunistring __doc
mv $RPM_BUILD_ROOT%{mingw64_datadir}/doc/libunistring __doc

%files -n mingw32-libunistring
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{mingw32_bindir}/libunistring-2.dll
%{mingw32_includedir}/*.h
%{mingw32_includedir}/unistring
%{mingw32_infodir}/libunistring.info*
%{mingw32_libdir}/libunistring.dll.a

%files -n mingw64-libunistring
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{mingw64_bindir}/libunistring-2.dll
%{mingw64_includedir}/*.h
%{mingw64_includedir}/unistring
%{mingw64_infodir}/libunistring.info*
%{mingw64_libdir}/libunistring.dll.a

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.9.10-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Aug 15 2019 Fabiano Fidêncio <fidencio@redhat.com> - 0.9.10-1
- Initial version
