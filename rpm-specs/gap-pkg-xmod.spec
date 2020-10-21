%global pkgname XMod

Name:           gap-pkg-xmod
Version:        2.81
Release:        2%{?dist}
Summary:        Crossed Modules and Cat1-Groups for GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/xmod/
Source0:        https://github.com/gap-packages/xmod/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-crisp
BuildRequires:  gap-pkg-groupoids
BuildRequires:  gap-pkg-hap
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  gap-pkg-utils
BuildRequires:  tex(xy.sty)

Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-crisp
Requires:       gap-pkg-groupoids
Requires:       gap-pkg-hap
Requires:       gap-pkg-smallgrp
Requires:       gap-pkg-utils

%description
This package allows for computation with crossed modules, cat1-groups,
morphisms of these structures, derivations of crossed modules and the
corresponding sections of cat1-groups.  Experimental functions for
crossed squares are now included.  In October 2015 a new section on
isoclinism of crossed modules was added.

%package doc
Summary:        XMod documentation
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
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{CHANGES.md,LICENSE.txt,README.md,scripts,.*.yml}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jerry James <loganjerry@gmail.com> - 2.81-1
- Version 2.81

* Tue May  5 2020 Jerry James <loganjerry@gmail.com> - 2.79-1
- Version 2.79

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 2.77-1
- Version 2.77
- Add gap-pkg-crisp BR and R to avoid incorrect test results

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 2.73-1
- New upstream version

* Wed Feb 13 2019 Jerry James <loganjerry@gmail.com> - 2.72-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Jerry James <loganjerry@gmail.com> - 2.64-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 Jerry James <loganjerry@gmail.com> - 2.59-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec  3 2016 Jerry James <loganjerry@gmail.com> - 2.58-1
- New upstream version
- New URLs

* Fri Sep 30 2016 Jerry James <loganjerry@gmail.com> - 2.56-1
- Initial RPM
