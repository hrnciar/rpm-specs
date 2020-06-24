%global pkgname factint
%global upname  FactInt

Name:           gap-pkg-%{pkgname}
Version:        1.6.3
Release:        2%{?dist}
Summary:        Advanced methods for factoring integers

License:        GPLv2+
URL:            https://gap-packages.github.io/%{upname}/
Source0:        https://github.com/gap-packages/%{upname}/releases/download/v%{version}/%{upname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
FactInt provides implementations of the following methods for factoring
integers:
- Pollard's p-1
- Williams' p+1
- Elliptic Curves Method (ECM)
- Continued Fraction Algorithm (CFRAC)
- Multiple Polynomial Quadratic Sieve (MPQS)
FactInt also makes use of Richard P. Brent's tables of known factors of
integers of the form bk+/-1 for "small" b.

The ECM method is suited best for finding factors which are neither too
small (i.e. have less than about 12 decimal digits) nor too close to the
square root of the number to be factored.  The MPQS method is designed
for factoring products of two primes of comparable orders of magnitude.
CFRAC is the historical predecessor of the MPQS method.  Pollard's p-1
and Williams' p+1 are useful for finding factors p such that all prime
factors of p-1 (respectively p+1) are "small", e.g. smaller than 1000000.
All factoring methods implemented in this package are probabilistic.  In
particular the time needed by the ECM method depends largely on luck.

FactInt provides a general-purpose factorization routine which uses an
appropriate combination of the methods mentioned above, the Pollard Rho
routine which is implemented in the GAP Library and a variety of tricks
for special cases to obtain a good average performance for "arbitrary"
integers.  At the user's option, FactInt provides detailed information
about the progress of the factorization process.

%package doc
Summary:        FactInt documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{upname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/{CHANGES,LICENSE,README.md,scripts,.*.yml}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- Version 1.6.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.6.2-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  9 2018 Jerry James <loganjerry@gmail.com> - 1.6.2-1
- New upstream version
- New URLs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 1.6.0-1
- New upstream version
- New URLs

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Jerry James <loganjerry@gmail.com> - 1.5.4-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May  3 2016 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- Initial RPM
