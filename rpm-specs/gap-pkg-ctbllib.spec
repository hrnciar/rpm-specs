%global pkgname ctbllib

# When bootstrapping a new architecture, there is no gap-pkg-spinsym package
# yet.  We need it to run tests, but it needs this package to function at all.
# Therefore, do the following:
# 1. Build this package in bootstrap mode.
# 2. Build gap-pkg-spinsym
# 4. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap-pkg-%{pkgname}
Version:        1.3.1
Release:        2%{?dist}
Summary:        GAP Character Table Library

License:        GPLv2+
URL:            http://www.math.rwth-aachen.de/~Thomas.Breuer/%{pkgname}/
Source0:        http://www.math.rwth-aachen.de/~Thomas.Breuer/%{pkgname}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-browse-doc
BuildRequires:  gap-pkg-cohomolo
BuildRequires:  gap-pkg-smallgrp-doc
%if %{without bootstrap}
BuildRequires:  gap-pkg-spinsym
%endif
BuildRequires:  gap-pkg-tomlib-doc
BuildRequires:  netpbm-progs
BuildRequires:  parallel
BuildRequires:  procps
BuildRequires:  tex(epic.sty)

Requires:       gap-pkg-atlasrep

Recommends:     gap-pkg-browse
Recommends:     gap-pkg-primgrp
Recommends:     gap-pkg-smallgrp
Recommends:     gap-pkg-tomlib
Recommends:     gap-pkg-spinsym
Recommends:     gap-pkg-transgrp

%description
This package provides the Character Table Library by Thomas Breuer.

%package doc
Summary:        Character Table Library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-browse-doc
Requires:       gap-pkg-smallgrp-doc
Requires:       gap-pkg-tomlib-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Remove spurious executable bit
chmod a-x doc/utils.xml

%build
# Link to main GAP documentation
smallgrpdir=$(ls -1d %{_gap_dir}/pkg/SmallGrp*)
cp -a %{_gap_dir}/doc ../../doc
ln -s $smallgrpdir ..
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s $smallgrpdir ../pkg
cd doc2
gap -l "$PWD/../..;%{_gap_dir}" < makedocrel.g
cd -
cd doc
gap -l "$PWD/../..;%{_gap_dir}" < makedocrel.g
cd -
rm -fr ../SmallGrp* ../../doc ../pkg

# Remove the build directory from the documentation
sed -i "s,$PWD/doc/\.\./\.\./pkg,../..,g" doc/*.html
sed -i "s,$PWD/doc2/\.\./\.\./pkg,../..,g" doc2/*.html

# Compress large tables
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tbl

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{gap3,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/tst/*~
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc{,2}/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
# Basic installation test
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" << EOF
ReadPackage( "ctbllib", "tst/testinst.g" );
EOF

%if %{without bootstrap}
# Somewhat less basic test.  Skip the interactive tests.
# Do not run testall.g.  It takes several days to run.
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
sed -i '/BrowseCTblLibInfo();/d' gap4/ctbltocb.g tst/docxpl.tst{,~}
gap -l "$PWD/..;%{_gap_dir}" < tst/testauto.g
rm -fr ../pkg
%endif

%files
%doc README.md
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Version 1.3.1

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0
- Drop all patches
- Add bootstrap mode to guard test that needs spinsym

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.2.2-13
- Rebuild for gap 4.10.0
- Add -generators patch to work around incompatibility with gap 4.10.0
- Add -test patch to fix problems with the tests
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-7
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-5
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 30 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-3
- Use redirection to force check script to terminate

* Thu Jan 29 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-2
- Use _smp_mflags when compressing

* Fri Jan 16 2015 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- Initial RPM
