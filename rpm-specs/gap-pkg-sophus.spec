%global pkgname sophus

Name:           gap-pkg-%{pkgname}
Version:        1.24
Release:        6%{?dist}
Summary:        Computing in nilpotent Lie algebras

License:        GPLv2+
URL:            https://gap-packages.github.io/sophus/
Source0:        https://github.com/gap-packages/sophus/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp

Requires:       gap-core
Requires:       gap-pkg-autpgrp

%description
The Sophus package is written to compute with nilpotent Lie algebras
over finite prime fields.  Using this package, you can compute the
cover, the list of immediate descendants, and the automorphism group of
such Lie algebras.  You can also test if two such Lie algebras are
isomorphic.

The immediate descendant function of the package can be used to classify
small-dimensional nilpotent Lie algebras over a given field.  For
instance, the package author obtained a classification of nilpotent Lie
algebras with dimension at most 9 over F_2; see
http://www.sztaki.hu/~schneider/Research/SmallLie.

%package doc
Summary:        Sophus documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{CHANGES.md,LICENSE,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/gap/.\#*

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" tst/testall.g

%files
%doc README CHANGES.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.24-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Jerry James <loganjerry@gmail.com> - 1.24-1
- New upstream version
- New URLs
- Upstream now includes a license file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Jerry James <loganjerry@gmail.com> - 1.23-1
- Initial RPM
