Summary: IMA/EVM support utilities
Name: ima-evm-utils
Version: 1.2.1
Release: 3%{?dist}
License: GPLv2
Url:  http://linux-ima.sourceforge.net/
Source: http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: m4
BuildRequires: asciidoc
BuildRequires: libxslt
BuildRequires: openssl-devel
BuildRequires: keyutils-libs-devel
Requires: tss2

%description
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

%package devel
Summary: Development files for %{name}

%description devel
This package provides the header files for %{name}

%prep
%setup -q

%build
mkdir -p m4
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -type f -name "*.la" -print -delete

%ldconfig_scriptlets

%files devel
%{_pkgdocdir}/*.sh
%{_includedir}/*
%{_libdir}/libimaevm.so

%files
%doc ChangeLog README AUTHORS
%license COPYING
%{_bindir}/*
# if you need to bump the soname version, coordinate with dependent packages
%{_libdir}/libimaevm.so.1
%{_libdir}/libimaevm.so.1.0.0
%{_mandir}/man1/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Bruno E. O. Meneguele <bmeneg@redhat.com> - 1.2.1-2
- Add pull request to correct lib soname version, wich was bumped to 1.0.0

* Wed Jul 31 2019 Bruno E. O. Meneguele <bmeneg@redhat.com> - 1.2.1-1
- Rebase to upstream v1.2.1
- Remove both patches that were already solved in upstream version
- Add runtime dependency of tss2 to retrieve PCR bank data from TPM2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.1-4
- Add patch to remove dependency from libattr-devel package

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.1-2
- Remove libtool files
- Run ldconfig scriptlets after un/installing
- Add -devel subpackage to handle include files and examples
- Disable any static file in the package

* Fri Feb 16 2018 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.1-1
- New upstream release
- Support for OpenSSL 1.1 was added directly to the source code in upstream,
  thus removing specific patch for it
- Docbook xsl stylesheet updated to a local path

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-4
- Switch to %%ldconfig_scriptlets

* Fri Dec 01 2017 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.0-3
- Add OpenSSL 1.1 API support for the package, avoiding the need of
  compat-openssl10-devel package

* Mon Nov 20 2017 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.0-2
- Adjusted docbook xsl path to match the correct stylesheet
- Remove only *.la files, considering there aren't any *.a files

* Tue Sep 05 2017 Bruno E. O. Meneguele <brdeoliv@redhat.com> - 1.0-1
- New upstream release
- Add OpenSSL 1.0 compatibility package, due to issues with OpenSSL 1.1
- Remove libtool files
- Run ldconfig after un/installation to update *.so files
- Add -devel subpackage to handle include files and examples

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.9-3
- Fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 31 2014 Avesh Agarwal <avagarwa@redhat.com> - 0.9-1
- New upstream release
- Applied a patch to fix man page issues.
- Updated spec file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 27 2013 Vivek Goyal <vgoyal@redhat.com> - 0.6-1
- Initial package
