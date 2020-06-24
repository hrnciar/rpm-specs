# NOTE: We should really put the exam directory into the -doc subpackage, but
# there are test functions embedded in the main part of the package that refer
# to symbols defined in files in exam.  The result is that splitting exam out
# into -doc causes GAP to issue errors about undefined global symbols when
# loading polenta.

%global pkgname polenta

Name:           gap-pkg-%{pkgname}
Version:        1.3.9
Release:        3%{?dist}
Summary:        Polycyclic presentations for matrix groups

License:        GPLv2+
URL:            http://gap-packages.github.io/polenta/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-aclib
BuildRequires:  gap-pkg-alnuth-doc
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crystcat
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-radiroot

Requires:       gap-pkg-alnuth
Requires:       gap-pkg-polycyclic
Requires:       gap-pkg-radiroot

Recommends:     gap-pkg-aclib

%description
The Polenta package provides methods to compute polycyclic presentations
of matrix groups (finite or infinite).  As a by-product, this package
gives some functionality to compute certain module series for modules of
solvable groups.  For example, if G is a rational polycyclic matrix
group, then we can compute the radical series of the natural Q[G]-module
Q^d.

%package doc
Summary:        Polenta documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-alnuth-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{CHANGES,LICENSE,README.md,TODO}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/.cvsignore
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
# POLENTA.tst and POLENTA2.tst require more memory than some koji builders have
# available, so we disable them.  The maintainer should run them on a machine
# with a minimum of 16 GB of RAM prior to updating to a new version.
sed -ri 's/"POLENTA2?\.tst"/#&/' tst/testall.g

gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README.md TODO
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 1.3.9-2
- Fix -doc subpackage dependency on alnuth

* Sat Oct  5 2019 Jerry James <loganjerry@gmail.com> - 1.3.9-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.3.8-5
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  8 2018 Jerry James <loganjerry@gmail.com> - 1.3.8-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec  9 2016 Jerry James <loganjerry@gmail.com> - 1.3.7-1
- New upstream version (bz 1403107)

* Fri May  6 2016 Jerry James <loganjerry@gmail.com> - 1.3.6-1
- Initial RPM
