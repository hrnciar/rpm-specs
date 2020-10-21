%global pkgname groupoids

Name:           gap-pkg-%{pkgname}
Version:        1.68
Release:        3%{?dist}
Summary:        Groupoids, group graphs, and groupoid graphs

License:        GPLv2+
URL:            http://gap-packages.github.io/groupoids/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-fga
BuildRequires:  gap-pkg-semigroups
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-fga
Requires:       gap-pkg-utils

Recommends:     gap-pkg-semigroups

%description
The Groupoids package provides functions for computation with finite
groupoids and their morphisms.

The first part is concerned with the standard constructions for
connected groupoids, and for groupoids with more than one component.
Groupoid morphisms are also implemented, and recent work includes the
implementation of automorphisms of a finite, connected groupoid: by
permutation of the objects; by automorphism of the root group; and by
choice of rays to each object.  The automorphism group of such a
groupoid is also computed, together with an isomorphism of a quotient of
permutation groups.

The second part implements graphs of groups and graphs of groupoids.  A
graph of groups is a directed graph with a group at each vertex and with
isomorphisms between subgroups on each arc.  This construction enables
normal form computations for free products with amalgamation, and for
HNN extensions, when the vertex groups come with their own rewriting
systems.

%package doc
Summary:        Groupoids documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE.txt,scripts,.*.yml,*.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep  5 2019 Jerry James <loganjerry@gmail.com> - 1.68-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.67-1
- New upstream version

* Tue Apr 16 2019 Jerry James <loganjerry@gmail.com> - 1.65-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.63-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 1.55-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jerry James <loganjerry@gmail.com> - 1.54-1
- Name change from gap-pkg-gpd to gap-pkg-groupoids
