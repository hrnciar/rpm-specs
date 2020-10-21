%global pkgname alnuth

# When bootstrapping a new architecture, there is no gap-pkg-radiroot package
# yet.  It is only needed by this package to run some tests, but it requires
# this package to funtion at all.  Therefore, do this:
# 1. Build this package in bootstrap mode
# 2. Build gap-pkg-radiroot
# 3. Build this package in non-bootstrap mode
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        3.1.2
Release:        2%{?dist}
Summary:        Algebraic number theory for GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/alnuth/
Source0:        https://github.com/gap-packages/alnuth/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-polycyclic
%if %{without bootstrap}
BuildRequires:  gap-pkg-radiroot
%endif
BuildRequires:  pari-gp
BuildRequires:  tth

Requires:       gap-pkg-polycyclic
Requires:       pari-gp

%description
Alnuth is an extension for the computer algebra system GAP and forms
part of a standard installation.  The functionality of Alnuth lies in
ALgebraic NUmber THeory.  It provides an interface from GAP to certain
number theoretic functions from the computer algebra system PARI/GP.
Most computations with Alnuth rely on this interface.

%package doc
Summary:        Alnuth documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{doc/make_doc,CHANGES.md,GPL,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.*.yml,scripts}

%if %{without bootstrap}
%check
# Tests that depend on RadiRoot will fail during a bootstrap build.
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g
%endif

%files
%doc CHANGES.md README.md
%license GPL
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 3.1.2-1
- Version 3.1.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 3.1.1-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 3.1.0-5
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 3.0.0-6
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov  6 2015 Jerry James <loganjerry@gmail.com> - 3.0.0-4
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  2 2015 Jerry James <loganjerry@gmail.com> - 3.0.0-2
- Rebuild with radiroot

* Wed Mar 25 2015 Jerry James <loganjerry@gmail.com> - 3.0.0-1
- Initial RPM (bz 1205905)
