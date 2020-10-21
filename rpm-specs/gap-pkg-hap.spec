# TODO: This package wants homology, if the Pascal issues can be resolved:
# http://ljk.imag.fr/membres/Jean-Guillaume.Dumas/Homology/

%global pkgname hap

# When bootstrapping a new architecture, the hapcryst package is not yet
# available.  Therefore:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-hapcryst.
# 3. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        1.26
Release:        2%{?dist}
Summary:        Homological Algebra Programming for GAP
BuildArch:      noarch

License:        GPLv2+
URL:            https://gap-packages.github.io/hap/
Source0:        https://github.com/gap-packages/hap/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Change from the old nql package name to the new lpres name
Patch0:         %{name}-lpres.patch
# Fix a clash between this package and the HAPprime package
Patch1:         %{name}-happrime.patch
# Adapt to polymake 4
Patch2:         %{name}-polymake4.patch

BuildRequires:  asymptote
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-congruence
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-edim
BuildRequires:  gap-pkg-fga
%if %{without bootstrap}
BuildRequires:  gap-pkg-hapcryst
%endif
BuildRequires:  gap-pkg-laguna
BuildRequires:  gap-pkg-lpres
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-polymaking
BuildRequires:  gap-pkg-singular
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  perl-generators
BuildRequires:  xdg-utils

Requires:       coreutils
Requires:       gap-pkg-aclib
Requires:       gap-pkg-crystcat
Requires:       gap-pkg-fga
Requires:       gap-pkg-nq
Requires:       gap-pkg-polycyclic
Requires:       xdg-utils

Recommends:     asymptote
Recommends:     gap-pkg-congruence
Recommends:     gap-pkg-edim
Recommends:     gap-pkg-lpres
Recommends:     gap-pkg-polymaking
Recommends:     gap-pkg-singular

Suggests:       gap-pkg-hapcryst
Suggests:       gap-pkg-xmod
Suggests:       graphviz
Suggests:       ImageMagick
Suggests:       openssh-clients

%description
HAP is a homological algebra library for use with the GAP computer
algebra system, and is still under development.  Its initial focus is on
computations related to the cohomology of groups.  Both finite and
infinite groups are handled, with emphasis on integral coefficients.

Recent additions include some functions for computing homology of
crossed modules and simplicial groups, and also some functions for
handling simplicial complexes, cubical complexes and regular
CW-complexes in the context of topological data analysis.

%package doc
Summary:        HAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Change the path to the perl executable
sed -i.orig 's,/usr/local/bin/perl,%{_bindir}/perl,' lib/PolyComplexes/prog
fixtimestamp lib/PolyComplexes/prog
chmod 0755 lib/PolyComplexes/prog

# Don't force the web browser to be firefox
sed -i.orig 's/"firefox"/"xdg-open"/' lib/externalSoftware.gap
fixtimestamp lib/externalSoftware.gap

# Remove obsolete files
find . \( -name \*keep\* -o -name \*working\* -o -name \*.bak -o -name \*.swp \) -delete
rm -fr lib/*/*old* www/SideLinks/About/*OLD*
rm -f lib/Functors/*.ancient lib/GOuterGroups/*.trial

# Clean up documentation to force complete rebuild
cd doc
./clean
cd tutorial
./clean
cd ../..

# Fix end of line encoding
sed -i.orig 's/\r//' www/SideLinks/{HAPpagestyles,SantiagoStyles}.css
fixtimestamp www/SideLinks/HAPpagestyles.css
fixtimestamp www/SideLinks/SantiagoStyles.css

# Remove incorrect executable bits
chmod a-x www/SideLinks/About/aboutCrossedMods

%build
# Build the documentation
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{compile*,README.md,uncompile*,updateAll.sh}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/.{idl.ilg,idl.ind,ind,tex}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/{clean,rd.sh}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/tutorial/clean
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/CompiledGAP

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8

# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Now we can run the actual test
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g
%endif

%files
%doc README.md
%license www/copyright/*.html
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May  5 2020 Jerry James <loganjerry@gmail.com> - 1.26-1
- Version 1.26

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.25-1
- Version 1.25
- New URLs
- Drop upstreamed -doc patch

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 1.24-3
- Add -polymake4 patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Jerry James <loganjerry@gmail.com> - 1.24-1
- Version 1.24

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 1.21-1
- New upstream release
- Drop -dims patch; upstream fixed it another way

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Jerry James <loganjerry@gmail.com> - 1.19-2
- Changes due to gap-pkg-singular becoming available

* Wed Feb  6 2019 Jerry James <loganjerry@gmail.com> - 1.19-1
- New upstream release
- Add -dims and -lpres patches
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb  3 2018 Jerry James <loganjerry@gmail.com> - 1.12.5-1
- New upstream release

* Wed Sep  6 2017 Jerry James <loganjerry@gmail.com> - 1.12.0-1
- New upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jerry James <loganjerry@gmail.com> - 1.11.14-1
- New upstream release
- Use upstream's 3-part version scheme
- Suggest the hapcryst and xmod packages

* Tue Aug 16 2016 Jerry James <loganjerry@gmail.com> - 1.11-2
- Switch crystcat from Recommends to Requires

* Fri Aug  5 2016 Jerry James <loganjerry@gmail.com> - 1.11-1
- Initial RPM
