%global pkgname  laguna

Name:           gap-pkg-%{pkgname}
Version:        3.9.3
Release:        3%{?dist}
Summary:        Lie AlGebras and UNits of group Algebras

License:        GPLv2+
URL:            https://gap-packages.github.io/laguna/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-sophus

Requires:       gap-core

Recommends:     gap-pkg-sophus

%description
The LAGUNA package replaces the LAG package and provides functionality
for calculation of the normalized unit group of the modular group
algebra of the finite p-group and for investigation of Lie algebra
associated with group algebras and other associative algebras.

%package doc
Summary:        LAGUNA documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# Fix end of line encodings
sed -i 's/\r/\n/g' doc/{manual.bib,theory.xml}

%build
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "%{_gap_dir};$PWD/.." < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{ChangeLog,COPYING,README.md,scripts}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc ChangeLog README.md
%license COPYING
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 3.9.3-1
- New upstream version

* Tue Feb 19 2019 Jerry James <loganjerry@gmail.com> - 3.9.2-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 3.9.1-3
- Rebuild for gap 4.10.0
- Drop -test patch, not needed with gap 4.10
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec  8 2018 Jerry James <loganjerry@gmail.com> - 3.9.1-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Jerry James <loganjerry@gmail.com> - 3.9.0-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Jerry James <loganjerry@gmail.com> - 3.8.0-1
- Initial RPM
