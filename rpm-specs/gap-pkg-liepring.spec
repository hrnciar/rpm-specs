%global pkgname liepring

Name:           gap-pkg-%{pkgname}
Version:        1.9.2
Release:        3%{?dist}
Summary:        Database and algorithms for Lie p-rings

License:        GPLv2+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-liering
BuildRequires:  tth

Requires:       gap-pkg-liering

%description
The main object of the LiePRing package is to provide access to the
nilpotent Lie rings of order p^n for p>2 and n<=7.

%package doc
Summary:        LiePRing documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix paths
sed -i 's,\.\./\.\./\.\./,/usr/lib/gap/,' doc/make_doc

# Fix a bibliographic reference
sed -i 's/Khu/&98/' doc/lieprings-theory.tex

%build
ln -s %{_gap_dir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/make_doc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/notes/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim6/notes/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/2gen/notes/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/3gen/notes/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/4gen/notes/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/5gen/notes/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/notes/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim6/notes/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/2gen/notes/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/3gen/notes/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/4gen/notes/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/5gen/notes/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/notes/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim6/notes/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/2gen/notes/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/3gen/notes/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/4gen/notes/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/dim7/5gen/notes/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 1.9.2-1
- Initial RPM
