Name:		packmol
Version:	20.010
Release:	2%{?dist}
Summary:	Packing optimization for molecular dynamics simulations
License:	MIT
URL:		http://m3g.iqm.unicamp.br/packmol/home.shtml
Source0:	https://github.com/mcubeg/packmol/archive/%{version}/packmol-%{version}.tar.gz
# CMake file for compiling project, sent upstream.
Source1:	packmol-CMakeLists.txt

BuildRequires:	cmake
BuildRequires:	gcc-gfortran

%description
Packmol creates an initial point for molecular dynamics simulations by
packing molecules in defined regions of space. The packing guarantees
that short range repulsive interactions do not disrupt the
simulations.

The great variety of types of spatial constraints that can be
attributed to the molecules, or atoms within the molecules, makes it
easy to create ordered systems, such as lamellar, spherical or tubular
lipid layers.

The user must provide only the coordinates of one molecule of each
type, the number of molecules of each type and the spatial constraints
that each type of molecule must satisfy.

The package is compatible with input files of PDB, TINKER, XYZ and
MOLDY formats.


%prep
%setup -q
cp -a %{SOURCE1} CMakeLists.txt
find . -name \*.o -delete

%build
export FC=gfortran

mkdir objdir
cd objdir
%cmake .. 
make %{?_smp_mflags} VERBOSE=1
cd ..

%install
rm -rf %{buildroot}
install -D -p -m 755 objdir/packmol %{buildroot}%{_bindir}/packmol
install -D -p -m 755 solvate.tcl %{buildroot}%{_bindir}/packmol_solvate

%files
%doc AUTHORS LICENSE
%{_bindir}/packmol
%{_bindir}/packmol_solvate

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 20.010-1
- Update to 20.010.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 18.013-1
- Update to 18.013.
- License changes to MIT.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 15.217-3
- Rebuilt for libgfortran soname bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 15.217-1
- Update to 15.217.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.243-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.243-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.243-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 05 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 13.243-1
- Update to 13.243.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2.023-1
- Update to 1.1.2.023.

* Sat Jan 21 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2.017-1
- Update to 1.1.2.017.

* Tue Sep 27 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1.258-1
- Initial release.
