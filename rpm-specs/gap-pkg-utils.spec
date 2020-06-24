%global pkgname utils

Name:           gap-pkg-%{pkgname}
Version:        0.69
Release:        2%{?dist}
Summary:        Utility functions for GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/utils/
Source0:        https://github.com/gap-packages/utils/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-polycyclic

Requires:       gap-pkg-autodoc
Requires:       gap-pkg-polycyclic

%description
The Utils package provides a collection of utility functions gleaned
from many packages.

%package doc
Summary:        GAP utils documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg/%{pkgname}
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{CHANGES.md,LICENSE.txt,README.md,scripts,.*.yml,.releases}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec  2 2019 Jerry James <loganjerry@gmail.com> - 0.69-1
- Version 0.69

* Fri Nov 22 2019 Jerry James <loganjerry@gmail.com> - 0.68-1
- Version 0.68

* Thu Sep  5 2019 Jerry James <loganjerry@gmail.com> - 0.67-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 0.64-1
- New upstream version

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 0.61-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 0.53-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 0.49-1
- New upstream version

* Wed Nov  8 2017 Jerry James <loganjerry@gmail.com> - 0.48-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb  9 2017 Jerry James <loganjerry@gmail.com> - 0.46-1
- New upstream version, now needs polycyclic

* Wed Jan 18 2017 Jerry James <loganjerry@gmail.com> - 0.44-1
- New upstream version

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 0.43-1
- New upstream version

* Wed Oct 19 2016 Jerry James <loganjerry@gmail.com> - 0.42-1
- New upstream version

* Tue May  3 2016 Jerry James <loganjerry@gmail.com> - 0.40-1
- Initial RPM
