%global pkgname radiroot

Name:           gap-pkg-%{pkgname}
Version:        2.8
Release:        6%{?dist}
Summary:        Compute radicals for roots of solvable rational polynomials

License:        GPL+
URL:            https://gap-packages.github.io/radiroot/
Source0:        https://github.com/gap-packages/radiroot/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Fix out of order lines in an example
Patch0:         %{name}-example.patch
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  gap-pkg-alnuth
BuildRequires:  tth

Requires:       gap-pkg-alnuth

%description
This package can compute and display an expression by radicals for the
roots of a solvable, rational polynomial.  Related to this it is
possible to create the Galois group and the splitting field of a
rational polynomial.

%package doc
Summary:        Radiroot documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Fix link to main GAP bibliography file and delete obsolete reference
sed -i 's,/doc/manual,&bib.xml,;/doc\/ext/d' doc/manual.tex

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
ln -s %{_gap_dir}/pkg/GAPDoc ../gapdoc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc} ../gapdoc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{doc/make_doc,CHANGES,GPL,README,scripts}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README
%license GPL
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}/htm/
%{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/htm/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 2.8-4
- Rebuild for gap 4.10.0
- Add -example patch
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Jerry James <loganjerry@gmail.com> - 2.8-1
- New upstream version
- New URLs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 2.7-5
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 2.7-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Jerry James <loganjerry@gmail.com> - 2.7-1
- Initial RPM (bz 1206367)
