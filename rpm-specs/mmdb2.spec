Summary: Macromolecular coordinate library
Name: mmdb2
Version: 2.0.1
Release: 14%{?dist}
License: LGPLv3
URL: ftp://ftp.ccp4.ac.uk/opensource/
Source0: ftp://ftp.ccp4.ac.uk/opensource/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
MMDB is a macromolecular coordinate library, written by Eugene
Krissinel primarily for use by the collaborative computational project
4 (CCP4) group in the United Kingdom.  The Coordinate Library is
designed to assist CCP4 developers in working with coordinate files.

The Library features work with the primary file formats of the Protein
Data Bank (PDB), the PDB file format and the mmCIF file format.

The Library provides various high-level tools for working with
coordinate files, which include not only reading and writing, but also
orthogonal-fractional coordinate transforms, generation of symmetry
mates, editing the molecular structure and some others. The Library is
supposed as a general low-level tool for unifying the
coordinate-related operations.

This package contains the shared library components needed for programs
that have been compiled with the mmdb library. 

%package devel
Summary: Header files and library for developing programs with mmdb
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains libraries and header files needed for program
development using the macromolecular coordinate library.

%prep
%setup -q -n %{name}-%{version}
chmod 644 README COPYING AUTHORS

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README
%{_libdir}/libmmdb2.so.0.0.0
%{_libdir}/libmmdb2.so.0

%files devel
%{_libdir}/libmmdb2.so
%{_includedir}/mmdb2/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 26 2014 Tim Fenn <tim.fenn@gmail.com> - 2.0.1-3
- edit obsoletes to prevent breakage on rawhide

* Sun Nov 2 2014 Tim Fenn <tim.fenn@gmail.com> - 2.0.1-2
- spec file clean ups/modernization

* Sun Sep 21 2014 Tim Fenn <tim.fenn@gmail.com> - 2.0.1-1
- Initial build
