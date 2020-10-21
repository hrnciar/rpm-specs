%{?mingw_package_header}

%global pkgname pcre2

Name:          mingw-%{pkgname}
Version:       10.35
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD
URL:           http://www.pcre.org/
Source:        ftp://ftp.pcre.org/pub/pcre/%{pkgname}-%{version}.tar.gz

## Patches taken from native package ##
# Do no set RPATH if libdir is not /usr/lib
Patch0:        pcre2-10.10-Fix-multilib.patch

## MinGW specific patches ##
# Fix implicitly defined functions due to overly relaxed platform detection in macros
Patch100:      pcre2-10.23-mingw.patch


BuildArch:     noarch

BuildRequires: automake autoconf libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-readline

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-readline


%description
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Because of multilib patch
libtoolize --copy --force
autoreconf -vif


%build
%mingw_configure \
    --enable-jit \
    --enable-pcre2grep-jit \
    --disable-bsr-anycrlf \
    --disable-coverage \
    --disable-ebcdic \
    --disable-fuzz-support \
    --disable-never-backslash-C \
    --enable-newline-is-lf \
    --enable-pcre2-8 \
    --enable-pcre2-16 \
    --enable-pcre2-32 \
    --enable-pcre2grep-callout \
    --enable-pcre2grep-jit \
    --disable-pcre2grep-libbz2 \
    --disable-pcre2grep-libz \
    --disable-pcre2test-libedit \
    --enable-pcre2test-libreadline \
    --disable-rebuild-chartables \
    --enable-shared \
    --enable-stack-for-recursion \
    --enable-static \
    --enable-unicode \
    --disable-valgrind
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{mingw32_datadir}/doc/*
rm -rf %{buildroot}%{mingw64_datadir}/doc/*
rm -rf %{buildroot}%{mingw32_datadir}/man/*
rm -rf %{buildroot}%{mingw64_datadir}/man/*

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Fix spurious-executable-perm
chmod 0644 %{buildroot}%{mingw32_libdir}/*.dll.a
chmod 0644 %{buildroot}%{mingw64_libdir}/*.dll.a


# Win32
%files -n mingw32-%{pkgname}
%license LICENCE
%{mingw32_bindir}/pcre2grep.exe
%{mingw32_bindir}/pcre2test.exe
%{mingw32_bindir}/pcre2-config
%{mingw32_bindir}/libpcre2-8-0.dll
%{mingw32_bindir}/libpcre2-16-0.dll
%{mingw32_bindir}/libpcre2-32-0.dll
%{mingw32_bindir}/libpcre2-posix-2.dll
%{mingw32_libdir}/libpcre2-8.dll.a
%{mingw32_libdir}/libpcre2-16.dll.a
%{mingw32_libdir}/libpcre2-32.dll.a
%{mingw32_libdir}/libpcre2-posix.dll.a
%{mingw32_libdir}/pkgconfig/libpcre2-*.pc
%{mingw32_includedir}/pcre2.h
%{mingw32_includedir}/pcre2posix.h

%files -n mingw32-%{pkgname}-static
%license LICENCE
%{mingw32_libdir}/libpcre2-8.a
%{mingw32_libdir}/libpcre2-16.a
%{mingw32_libdir}/libpcre2-32.a
%{mingw32_libdir}/libpcre2-posix.a

# Win64
%files -n mingw64-%{pkgname}
%license LICENCE
%{mingw64_bindir}/pcre2grep.exe
%{mingw64_bindir}/pcre2test.exe
%{mingw64_bindir}/pcre2-config
%{mingw64_bindir}/libpcre2-8-0.dll
%{mingw64_bindir}/libpcre2-16-0.dll
%{mingw64_bindir}/libpcre2-32-0.dll
%{mingw64_bindir}/libpcre2-posix-2.dll
%{mingw64_libdir}/libpcre2-8.dll.a
%{mingw64_libdir}/libpcre2-16.dll.a
%{mingw64_libdir}/libpcre2-32.dll.a
%{mingw64_libdir}/libpcre2-posix.dll.a
%{mingw64_libdir}/pkgconfig/libpcre2-*.pc
%{mingw64_includedir}/pcre2.h
%{mingw64_includedir}/pcre2posix.h

%files -n mingw64-%{pkgname}-static
%license LICENCE
%{mingw64_libdir}/libpcre2-8.a
%{mingw64_libdir}/libpcre2-16.a
%{mingw64_libdir}/libpcre2-32.a
%{mingw64_libdir}/libpcre2-posix.a


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 09 2020 Sandro Mani <manisandro@gmail.com> - 10.35-1
- Update to 10.35

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Sandro Mani <manisandro@gmail.com> - 10.34-1
- Update to 10.34

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 10.33-3
- Rebuild (readline)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Sandro Mani <manisandro@gmail.com> - 10.33-1
- Update to 10.33

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Sandro Mani <manisandro@gmail.com> - 10.32-1
- Update to 10.32

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Sandro Mani <manisandro@gmail.com> - 10.31-1
- Update to 10.31

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Sandro Mani <manisandro@gmail.com> - 10.30-1
- Update to 10.30

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Sandro Mani <manisandro@gmail.com> - 10.23-2
- Remove duplicate listed files in %%files
- Add %%license to static packages

* Wed Jun 14 2017 Sandro Mani <manisandro@gmail.com> - 10.23-1
- Initial package
