Name:      libicu65
Version:   65.1
Release:   2%{?dist}
Summary:   Compat package with icu libraries

License:   MIT and UCD and Public Domain
URL:       http://site.icu-project.org/
Source0:   https://github.com/unicode-org/icu/releases/download/release-65-1/icu4c-65_1-src.tgz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: doxygen, autoconf, python3

# Fix the build on s390x
Patch0: icu-64.1-data_archive_generation.patch
Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch

# Explicitly conflict with older icu packages that ship libraries
# with the same soname as this compat package
Conflicts: libicu < 66

%description
Compatibility package with icu libraries ABI version 65.


%{!?endian: %global endian %(%{__python} -c "import sys;print (0 if sys.byteorder=='big' else 1)")}
# " this line just fixes syntax highlighting for vim that is confused by the above and continues literal


%prep
%autosetup -p1 -n icu


%build
pushd source
autoconf
CFLAGS='%optflags -fno-strict-aliasing'
CXXFLAGS='%optflags -fno-strict-aliasing'
# Endian: BE=0 LE=1
%if ! 0%{?endian}
CPPFLAGS='-DU_IS_BIG_ENDIAN=1'
%endif

#rhbz856594 do not use --disable-renaming or cope with the mess
OPTIONS='--with-data-packaging=library --disable-samples'
%if 0%{?debugtrace}
OPTIONS=$OPTIONS' --enable-debug --enable-tracing'
%endif
%configure $OPTIONS

#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

# more verbosity for build.log
sed -i -r 's|(PKGDATA_OPTS = )|\1-v |' data/Makefile

make %{?_smp_mflags} VERBOSE=1


%install
make %{?_smp_mflags} -C source install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*

# Remove files that aren't needed for the compat package
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/icu/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_sbindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/icu/
rm -rf $RPM_BUILD_ROOT%{_mandir}


%files
%license LICENSE
%{_libdir}/*.so.*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 65.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Pete Walter <pwalter@fedoraproject.org> - 65.1-1
- Initial packaging
