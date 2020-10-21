%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

name:		libtopology
Version:	0.3
Release:	28%{?dist}
Summary:	CPU Topology library

License:	LGPLv2
URL:		http://libtopology.ozlabs.org/
BuildRequires:	gcc

Source0:	http://libtopology.ozlabs.org/releases/%{name}-%{version}.tar.gz

%description
Libtopology is a library for discovering the hardware topology on Linux
systems.

%package devel
Summary:	CPU Topology library development package
Requires:	%{name} = %{version}-%{release}

%description devel
Development package for libtopology.

%package doc
Summary:	CPU Topology library documentation package
Requires:	%{name} = %{version}-%{release}
BuildRequires:	doxygen
BuildArch:	noarch

%description doc
Documentation and sample programs for libtopology.

%prep
%setup -q -n %{name}-%{version}

%build
make	CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}
make	doc

%check
make	CFLAGS="%{optflags} -fPIC" test

%install
rm -rf %{buildroot}
make	inst_libdir="%{buildroot}/%{_prefix}/%{_lib}" \
	inst_includedir="%{buildroot}/%{_includedir}" \
	install

mkdir -p %{buildroot}/%{_pkgdocdir}/{examples,doc}
cp -p COPYING README %{buildroot}/%{_pkgdocdir}/
cp -p programs/*.c %{buildroot}/%{_pkgdocdir}/examples/
cp -p include/compat.h %{buildroot}/%{_pkgdocdir}/examples/
# We shouldn't package fonts.  They're not required.
[ -e doc/generated/latex/FreeSans.ttf ] && rm doc/generated/latex/FreeSans.ttf 
cp -pr doc/generated/* %{buildroot}/%{_pkgdocdir}/doc/

%ldconfig_scriptlets libs

%files
%{_libdir}/libtopology.so.0
%{_libdir}/libtopology.so.0.3
%dir %{_pkgdocdir}/
%{_pkgdocdir}/COPYING

%files devel 
%{_includedir}/topology.h
%{_libdir}/libtopology.so

%files doc 
%{_pkgdocdir}/README
%{_pkgdocdir}/examples/
%{_pkgdocdir}/doc/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Tony Breeds <tony@bakeyournoodle.com> - 0.3-24
- Add gcc into BuildRoot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Tony Breeds <tony@bakeyournoodle.com> - 0.3-22
- Updated to remove \%defattr as per packaging standards

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov  9 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.3-13
- Install docs to %%{_pkgdocdir} where available (#993838).
- Fix bogus date in %%changelog.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 tony@bakeyournoodle.com - 0.3-7
- Fix FTBS problem (#511641)
- Also split documentation into (noarch) subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 30 2008 Tony Breeds <tony@bakeyournoodle.com> 0.3-4
- Conform with the new font packageing guidelines (#477415)

* Wed Nov 12 2008 Tony Breeds <tony@bakeyournoodle.com> 0.3-0.3
- Add BuildRequires for doxygen to the -devel package.

* Mon Nov 10 2008 Tony Breeds <tony@bakeyournoodle.com> 0.3-0.2
- move docs from seperate package into -devel
- use correct licence
- use cp -p for install

* Wed Oct 22 2008 Tony Breeds <tony@bakeyournoodle.com> 0.3-0.1
- Initial RPM package for Fedora
