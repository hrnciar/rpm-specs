%global pkgname gbnp

Name:           gap-pkg-%{pkgname}
Version:        1.0.3
Release:        12%{?dist}
Summary:        Computing Gröbner bases of noncommutative polynomials

License:        LGPLv2+
URL:            http://mathdox.org/gbnp/
Source0:        http://mathdox.org/products/%{pkgname}/GBNP-%{version}.tar.gz
# Fix malformed LaTeX
Patch0:         %{name}-doc.patch
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  tex-urlbst

Requires:       gap-core

%description
GBNP provides GAP algorithms for computing Gröbner bases of
non-commutative polynomials with coefficients from a field implemented in
GAP, and some variations, such as a weighted and truncated version and a
tracing facility.

The word algorithm is interpreted loosely: in general one cannot expect
such an algorithm to terminate, as it would imply solvability of the
word problem for finitely presented (semi)groups.

%package doc
Summary:        GBNP documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}

# Help GAP find its files
sed -i 's,\\\\\\\(.*\) ,"%{_gap_dir}\1",;s/eval //' scripts/workspace
sed -i 's,\\\\;,%{_gap_dir};,' scripts/makedepend scripts/workspace
sed -i "s,-r,-l '%{_gap_dir};%{_builddir}/%{pkgname}/build' &,;s/eval //" \
    scripts/gapscript

%build
make %{?_smp_mflags} doc

%install
# We install test files for use by GAP's internal test suite runner.
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{.depend,Changelog,COPYRIGHT,GNUmakefile,README*,TODO}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{build,scripts}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,in,ind,log,new,out,pnr,tex}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/nmo/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/examples
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/TODO
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/examples/{head.txt,makedepend,GNUmakefile,TODO,txt2xml.sed}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/lib/{gbnp-uses.sed,OPTIONS,STRUCTURE,TODO}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/test/{.depend,GNUmakefile,nmo,txt2xml.sed}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/version/README.in

%check
make tests

%files
%doc Changelog README
%license COPYRIGHT doc/LGPL
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.0.3-9
- Rebuild for gap 4.10.0
- Add -doc patch to fix malformed LaTeX

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul  1 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-3
- Make -doc own the main package directory
- Do not package the .tex source files
- Explain why the test filees are installed

* Mon Jun  6 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-2
- Add a -doc subpackage
- Exclude more files from the binary RPM

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Initial RPM
