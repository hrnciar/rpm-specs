%define cobvers 3.1

Name:           gnucobol
Version:        3.1
Release:        3%{?dist}
Summary:        COBOL compiler

License:        GPLv2+ and LGPLv2+

URL:            http://www.opencobol.org
#Source0:        http://downloads.sourceforge.net/open-cobol/%{name}/%{name}-%{cobvers}.tar.gz
# https://svn.code.sf.net/p/open-cobol/code/trunk - r3645 - 3.1 prerelease
Source0:        gnucobol.tar.gz
ExcludeArch:    ppc64le

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  readline-devel
BuildRequires:  libdb-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  help2man
BuildRequires:  texinfo

Requires:       gcc
Requires:       glibc-devel
Requires:       gmp-devel
Requires:       libcob = %{version}

%description
COBOL compiler, which translates COBOL
programs to C code and compiles them using GCC.

%package -n libcob
Summary:        GnuCOBOL runtime library

%description -n libcob
%{summary}.
Runtime libraries for GnuCOBOL

%prep
#%%autosetup -n %%{name}-%%{cobvers}-dev
%autosetup -nopen-cobol-code

%build
./autogen.sh
%configure

%make_build

iconv -c --to-code=UTF-8 ChangeLog > ChangeLog.new
mv ChangeLog.new ChangeLog

%install
make install DESTDIR=%{buildroot}
find %{buildroot}/%{_libdir} -type f -name "*.*a" -exec rm -f {} ';'
rm -rf %{buildroot}/%{_infodir}/dir

#%%find_lang %{name}

%check
make check CLFAGS="%optflags -O"

#%%files -f %%{name}.lang
%files
%license COPYING.DOC
%doc AUTHORS ChangeLog
%doc NEWS README THANKS
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_bindir}/gcdiff
%{_includedir}/*
%{_libdir}/%{name}
%{_libdir}/libcob.so
%{_datadir}/gnucobol
%{_infodir}/gnucobol.info.*
%{_mandir}/man1/cobc.1.*
%{_mandir}/man1/cobcrun.1.*
%{_mandir}/man1/cob-config.1.*


%files -n libcob
%license COPYING.LESSER
%{_libdir}/libcob.so.5*
%{_libdir}/gnucobol/CBL_OC_DUMP.so

%changelog
* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-3
- Review fixes.

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-2
- Review fixes.

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-1
- 3.1 nightly.

* Mon Apr 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0-0.rc1.1
- Initial release, adapted from open-cobol spec.
