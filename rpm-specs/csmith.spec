Name:    csmith
Version: 2.3.0
Release: 5%{?dist}
Summary: Tool to generate random C programs for compiler testing

# Most of the source code is under BSD while few header files are GPLv2+ and LGPLv2+
License: BSD and GPLv2+ and LGPLv2+
URL:     http://embed.cs.utah.edu/csmith/
Source0: http://embed.cs.utah.edu/csmith/%{name}-%{version}.tar.gz
Patch1:  csmith-2.1.0-remove-custom-headers.patch

BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: m4
BuildRequires: autoconf
BuildRequires: perl-generators

%description
Csmith is a tool that can generate random C programs that 
statically and dynamically conform to the C99 standard. It is 
useful for stress-testing compilers, static analyzers, and 
other tools that process C code

%package devel
Summary:        Header files and libraries for Csmith development
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel 
The %{name}-devel package contains the header files
and libraries for use with the Csmith package.

%prep
%setup -q
%patch1 -p1 -b .fix

%build
autoconf -f -i
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name *.a  -exec rm -f {} \;
find %{buildroot} -name *.la -exec rm -f {} \;
find %{buildroot} -name test_csmith.pl -exec rm -f {} \;
rm -f %{buildroot}%{_bindir}/compiler_test.in
rm -rf %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%license COPYING
%doc doc/probabilities.txt scripts/compiler_test.in
%doc AUTHORS ChangeLog README TODO
%{_bindir}/compiler_test.pl
%{_bindir}/csmith
%{_bindir}/launchn.pl
%{_libdir}/libcsmith.so.0*

%files devel
%{_includedir}/%{name}-%{version}
%{_libdir}/libcsmith.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Robin Lee <cheeselee@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 04 2015 Mukundan Ragavan - 2.2.0-1
- Update to version 2.2.0
- removed powerpc64 patch - upstreamed

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.1.0-10
- Perl 5.18 rebuild

* Sat Apr 20 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-9
- Use autoconf for ARM

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Dan Horák <dan[at]danny.cz> - 2.1.0-7
- fix build on all arches by adding fallback implementation for getting initial seed

* Mon Nov 19 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-6
- Removed BuildRoot tag
- Add multiple license comment
- Remove /usr/share/doc/csmith directory

* Mon Oct 29 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-5
- Update docdir

* Sat Jun 02 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-4
- Use system header files.

* Thu Dec 01 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-3
- Removed test_csmith.pl from the package.

* Sat Nov 26 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-2
- Move compiler_test.in to doc.
- Apply patch to build for ppc64.
- Added licenses.

* Wed Nov 23 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 2.1.0-1 
- Initial build.

