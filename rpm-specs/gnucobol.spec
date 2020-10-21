%define cobvers 3.1

Name:           gnucobol
Version:        3.1
Release:        7.rc1%{?dist}.2
Summary:        COBOL compiler

License:        GPLv3+ and LGPLv3+ and GFDL

URL:            https://www.gnu.org/software/gnucobol/
Source0:        https://alpha.gnu.org/gnu/gnucobol/gnucobol-%{version}-rc1.tar.gz
Source1:        https://alpha.gnu.org/gnu/gnucobol/gnucobol-%{version}-rc1.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source3:        https://www.itl.nist.gov/div897/ctg/suites/newcob.val.Z

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
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  perl-interpreter
BuildRequires:  libxml2-devel
# For rc2
#BuildRequires:  json-c-devel

Requires:       gcc
Requires:       glibc-devel
Requires:       gmp-devel
Requires:       libcob = %{version}

%description
COBOL compiler, which translates COBOL
programs to C code and compiles them using GCC.

%package -n libcob
Summary:        GnuCOBOL runtime library
License:        LGPLv3+

%description -n libcob
%{summary}.
Runtime libraries for GnuCOBOL

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n%{name}-%{version}-rc1
cp %{SOURCE3} tests/cobol85/

%build
%configure --with-db --with-libxml2 --with-curses=ncursesw

%make_build

iconv -c --to-code=UTF-8 ChangeLog > ChangeLog.new
mv ChangeLog.new ChangeLog

%install
make install DESTDIR=%{buildroot}
find %{buildroot}/%{_libdir} -type f -name "*.*a" -exec rm -f {} ';'
rm -rf %{buildroot}/%{_infodir}/dir

%find_lang %{name}

%check
(make check CFLAGS="%optflags -O" || make check TESTSUITEFLAGS="--recheck --verbose" || echo "Warning, unexpected results")
make test CFLAGS="%optflags -O"

%files -f %%{name}.lang
%license COPYING.DOC COPYING
%doc AUTHORS ChangeLog
%doc NEWS README THANKS
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
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
%{_libdir}/libcob.so.4*
%{_libdir}/gnucobol/CBL_OC_DUMP.so

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7.rc1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-7.rc1
- Re-add libxml2, specify optional flags.

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-6.rc1
- License, BuildRequire tweaks.

* Fri Jul 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-5.rc1
- Enable ppc64le, NIST tests.

* Thu Jul 02 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-4.rc1
- 3.1 rc1

* Wed Jun 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-3
- Review fixes.

* Wed May 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-2
- Review fixes.

* Fri Apr 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1-1
- 3.1 nightly.

* Mon Apr 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0-0.rc1.1
- Initial release, adapted from open-cobol spec.
